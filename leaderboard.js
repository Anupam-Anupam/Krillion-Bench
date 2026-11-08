'use strict';
const $ = (selector) => document.querySelector(selector);
const escapeHTML = (value) => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const palette = {openai:'#4de3ff',anthropic:'#ffb787',google:'#b6e897',moonshotai:'#ff79a5','x-ai':'#d3def5','z-ai':'#55e6bd',deepseek:'#8bafff',meta:'#dbabff',qwen:'#ffd166'};
const color = provider => palette[provider] || '#96a19a';
const providerName = p => ({openai:'OpenAI',anthropic:'Anthropic',google:'Google',moonshotai:'Moonshot','x-ai':'xAI','z-ai':'Z.ai',deepseek:'DeepSeek',meta:'Meta',qwen:'Qwen'}[p] || p);
const axes = {run_cost_usd:'LLM cost / run · USD', output_cost_usd:'Output cost / run · USD',output_tokens:'Output tokens / run',run_duration_s:'Elapsed time / run · seconds',daily_percentile:'Better than today’s players · %'};
const state = {data:null, query:'', status:'all', provider:'all', sort:'score', direction:-1, axis:'run_cost_usd', expanded:false};
const numeric = v => typeof v === 'number' && Number.isFinite(v) && v >= 0;
const count = v => v == null ? '—' : new Intl.NumberFormat('en-US',{maximumFractionDigits:0}).format(v);
const money = v => v == null ? '—' : v === 0 ? '$0.0000' : v < .0001 ? '$'+v.toFixed(6) : '$'+v.toFixed(4);
const duration = v => v == null ? '—' : v >= 60 ? `${Math.floor(Math.round(v)/60)}m ${Math.round(v)%60}s` : `${v.toFixed(1)}s`;
const costPrefix = basis => basis?.startsWith('partial_') ? (basis.includes('estimated') || basis.includes('mixed') ? '≥≈ ' : '≥ ') : basis === 'estimated' || basis === 'mixed' ? '≈ ' : '';
function basisText(basis) {
  return ({reported:'API-reported account charge',provider_reported:'Provider-reported output component',estimated:'Catalog estimate',mixed:'Mixed reported and estimated',partial_reported:'Partial reported charge',partial_provider_reported:'Partial provider output cost',partial_estimated:'Partial catalog estimate',partial_mixed:'Partial mixed accounting',unavailable:'Not recorded'})[basis] || 'Not recorded';
}
function metric(row,key) { if(key==='rank')return row.complete?scoreRank(row):null; return ['score','daily_percentile'].includes(key) ? row[key] : key === 'model' ? row.model : row.metrics[key]; }
function visibleRows() {
  return state.data.runs.filter(r => (state.status === 'all' || r.complete === (state.status === 'complete')) &&
    (state.provider === 'all' || r.provider === state.provider) && `${r.model} ${r.name}`.toLowerCase().includes(state.query));
}
function orderedRows(rows) {
  return [...rows].sort((a,b) => {
    if (['score','rank'].includes(state.sort) && a.complete !== b.complete) return a.complete ? -1 : 1;
    const av=metric(a,state.sort),bv=metric(b,state.sort);
    if (av == null && bv != null) return 1;
    if (bv == null && av != null) return -1;
    const compare=typeof av === 'string' ? av.localeCompare(bv) : (av ?? 0)-(bv ?? 0);
    return compare*state.direction || a.model.localeCompare(b.model);
  });
}
function scoreRank(row) { return row.complete ? 1 + state.data.runs.filter(r=>r.complete && r.score > row.score).length : '—'; }
// Badge placement is global and independent of filters or the selected metric.
function badgeForPosition(position) {
  if (!Number.isInteger(position) || position < 1 || position > 100) return null;
  if (position === 1) return {key:'krillion', label:'Krillion'};
  if (position <= 10) return {key:'deepcut', label:'Deep Cut'};
  if (position <= 25) return {key:'rare', label:'Rare'};
  if (position <= 50) return {key:'schooler', label:'Schooler'};
  return {key:'plankton', label:'Plankton'};
}
function badgeMarkup(row) {
  const position=state.placements.get(row.model), badge=badgeForPosition(position);
  return badge ? `<img class="rank-badge ${badge.key}" src="krillion-${badge.key}.png" width="36" height="36" alt="${badge.label}, overall position ${position}" title="${badge.label} · overall position ${position}">` : '';
}
const scoreText = value => new Intl.NumberFormat('en-US',{maximumFractionDigits:1}).format(value);
function scoreMarkup(row) {
  const interval=row.score_ci95;
  const label=interval?`95% CI ${scoreText(interval[0])}–${scoreText(interval[1])}`:'';
  return `<div class="score-bar${interval?' with-interval':''}"><div class="score-fill" style="width:${row.score/700*100}%"></div><span class="score-value">${scoreText(row.score)}<small>/ 700</small></span>${interval?`<span class="score-interval" aria-hidden="true" style="left:${interval[0]/700*100}%;width:${(interval[1]-interval[0])/700*100}%"></span>`:''}</div>${interval?`<span class="score-ci-label">${label}</span>`:''}`;
}
function openAggregateDetails(row) {
  const labels={score:'MEAN SCORE',daily_percentile:'MEAN DAILY %',run_cost_usd:'MEAN LLM COST',output_cost_usd:'MEAN OUTPUT COST',output_tokens:'MEAN OUTPUT TOKENS',run_duration_s:'MEAN TIME'};
  const format=(key,v)=>v==null?'—':key.includes('cost')?money(v):key==='run_duration_s'?duration(v):scoreText(v)+(key==='daily_percentile'?'%':'');
  $('#detail-content').innerHTML=`<h2 id="detail-title">${escapeHTML(row.model.split('/').slice(1).join('/'))}</h2><p class="detail-id">${escapeHTML(row.model)} · ${row.games} archived games</p><dl class="detail-metrics">${Object.entries(labels).map(([key,label])=>{const stat=row.aggregate_stats[key];return `<div><dt>${label}</dt><dd>${format(key,stat.mean)}<small>${stat.n} of ${row.games} games${stat.ci95?` · 95% CI ${format(key,stat.ci95[0])}–${format(key,stat.ci95[1])}`:''}</small></dd></div>`;}).join('')}</dl><p class="detail-notes">${escapeHTML(state.data.date_start)} through ${escapeHTML(state.data.date_end)}. Each model plays the same archived games once. Score includes timed-out questions. Intervals use 10,000 bootstrap resamples of game dates and describe variation across games, not repeated trials of one game. Metrics with unavailable or partial records exclude those records and show their sample count. Individual answers and trajectories are stored privately.</p>`;
  $('#run-dialog').showModal();$('#run-dialog').scrollTop=0;
}
function render() {
  const matches=orderedRows(visibleRows());
  const rows=state.expanded?matches:matches.slice(0,5);
  $('#results').innerHTML=rows.map(r=>{
    const m=r.metrics;
    const badge=badgeForPosition(state.placements.get(r.model));
    const display=r.model.split('/').slice(1).join('/');
    const cost=(value,basis)=>`<span title="${escapeHTML(basisText(basis))}">${escapeHTML(costPrefix(basis)+money(value))}</span>`;
    const tokens=m.output_tokens == null ? '—' : `${r.games||m.usage_complete?'':'≥ '}${count(m.output_tokens)}`;
    return `<tr data-tier="${badge?.key||'none'}" class="${r.complete?'':'incomplete'}"><td class="rank">${scoreRank(r)}</td><td class="model-cell"><button class="model-button" data-model="${escapeHTML(r.model)}" aria-label="View ${escapeHTML(r.model)} run details">${badgeMarkup(r)}<span><span class="model-name">${escapeHTML(display)}</span><span class="variant">${escapeHTML(providerName(r.provider))}${r.model.endsWith(':free')?' · free endpoint':''}${r.missed_rounds?' · '+r.missed_rounds+' missed':''}${r.scorecard_assisted?' · recovery':''}</span></span></button></td><td class="score-cell">${r.complete?scoreMarkup(r):`<span class="incomplete-label">Run error <small>${escapeHTML(r.error_type || r.status)}</small></span>`}</td><td>${cost(m.run_cost_usd,m.cost_basis)}</td><td>${cost(m.output_cost_usd,m.output_cost_basis)}</td><td title="${m.usage_calls} of ${m.model_calls} calls have usage">${tokens}</td><td>${duration(m.run_duration_s)}</td><td class="daily">${r.daily_percentile == null?'—':(r.games?r.daily_percentile.toFixed(2):r.daily_percentile)+'%'}</td></tr>`;
  }).join('') || '<tr><td colspan="8" class="empty">No models match these filters. Try another name or provider.</td></tr>';
  $('#row-count').textContent=`Showing ${rows.length} of ${matches.length}${matches.length===state.data.runs.length?' models':' matching models'} · click a model to inspect its dive`;
  const expand=$('#expand-results');
  expand.hidden=matches.length<=5;
  expand.setAttribute('aria-expanded',String(state.expanded));
  expand.textContent=state.expanded?'Show fewer models ↑':`Show all ${matches.length} models ↓`;
  document.querySelectorAll('th[data-sort]').forEach(th=>{
    const selected=th.dataset.sort===state.sort;
    th.setAttribute('aria-sort',selected?(state.direction===-1?'descending':'ascending'):'none');
    th.querySelector('span').textContent=selected?(state.direction===-1?'↓':'↑'):'';
  });
  renderChart(matches);
}
function renderChart(rows) {
  const key=state.axis;
  const eligible=rows.filter(r=>r.complete && numeric(metric(r,key)) && (!key.includes('cost') || !r.metrics[key==='run_cost_usd'?'cost_basis':'output_cost_basis'].startsWith('partial_')) && (key!=='output_tokens'||r.metrics.usage_complete||state.data.aggregation==='archive_mean'));
  $('#plot-direction').textContent=key==='daily_percentile'?'Higher score, higher placement ↗':'Higher score, lower '+({run_cost_usd:'cost',output_cost_usd:'output cost',output_tokens:'token use',run_duration_s:'time'}[key])+' ↖';
  $('#axis-label').textContent=axes[key];
  $('#chart-tooltip').hidden=true;
  if(!eligible.length){$('#chart').innerHTML='<p class="empty">No completed runs with this metric match your filters.</p>';$('#legend').innerHTML='';return;}
  const compact=window.matchMedia('(max-width:760px)').matches;
  const W=compact?420:1000,H=compact?300:310,L=46,R=25,T=24,B=38;
  const xmax=key==='daily_percentile'?100:Math.max(...eligible.map(r=>metric(r,key)),.0001)*1.1;
  const x=v=>L+v/xmax*(W-L-R),y=v=>H-B-v/700*(H-T-B);
  let svg=`<svg viewBox="0 0 ${W} ${H}" role="group" aria-label="Krillion score versus ${escapeHTML(axes[key])}. Each point opens run details.">`;
  for(let v=0;v<=700;v+=100) svg+=`<line class="gridline" x1="${L}" y1="${y(v)}" x2="${W-R}" y2="${y(v)}"/><text class="axis-text" x="${L-10}" y="${y(v)+4}" text-anchor="end">${v}</text>`;
  for(let i=0;i<=4;i++){
    const value=xmax*i/4;
    const label=key.includes('cost')?(value<.01?'$'+value.toFixed(3):'$'+value.toFixed(2)):key==='daily_percentile'?Math.round(value)+'%':count(value);
    svg+=`<line class="gridline" x1="${x(value)}" y1="${T}" x2="${x(value)}" y2="${H-B}"/><text class="axis-text" x="${x(value)}" y="${H-12}" text-anchor="middle">${label}</text>`;
  }
  const top=[...eligible].sort((a,b)=>b.score-a.score||a.model.localeCompare(b.model)).slice(0,compact?1:3);
  const occupied=[];
  for(const r of [...eligible].sort((a,b)=>a.score-b.score)){
    const cx=x(metric(r,key)),cy=y(r.score);
    const formatted=key.includes('cost')?costPrefix(r.metrics[key==='run_cost_usd'?'cost_basis':'output_cost_basis'])+money(metric(r,key)):key==='run_duration_s'?duration(metric(r,key)):count(metric(r,key))+(key==='daily_percentile'?'%':'');
    svg+=`<circle class="plot-point" cx="${cx}" cy="${cy}" r="4.5" fill="${color(r.provider)}" tabindex="0" role="button" data-model="${escapeHTML(r.model)}" aria-label="${escapeHTML(r.model)}, score ${scoreText(r.score)}, ${escapeHTML(formatted)}"><title>${escapeHTML(r.model)} · ${scoreText(r.score)} / 700 · ${escapeHTML(formatted)}</title></circle>`;
    if(top.includes(r)){
      let ly=cy-12;
      while(occupied.some(p=>Math.abs(p.x-cx)<155 && Math.abs(p.y-ly)<15))ly-=17;
      occupied.push({x:cx,y:ly});
      svg+=`<text class="dot-label" x="${cx}" y="${ly}" text-anchor="${cx>W-150?'end':'start'}" pointer-events="none">${escapeHTML(r.model.split('/')[1])}</text>`;
    }
  }
  $('#chart').innerHTML=svg+'</svg>';
  const providers=[...new Set(eligible.map(r=>r.provider))];
  $('#legend').innerHTML=providers.slice(0,8).map(p=>`<span><i style="background:${color(p)}"></i>${escapeHTML(providerName(p))}</span>`).join('')+(providers.length>8?`<span>+${providers.length-8} providers</span>`:'');
}
function openDetails(id) {
  const r=state.data.runs.find(r=>r.model===id);if(!r)return;
  if(state.data.aggregation==='archive_mean'){openAggregateDetails(r);return;}
  const m=r.metrics;
  const item=(label,value,note='')=>`<div><dt>${label}</dt><dd>${escapeHTML(value)}${note?`<small>${escapeHTML(note)}</small>`:''}</dd></div>`;
  $('#detail-content').innerHTML=`<h2 id="detail-title">${escapeHTML(r.model.split('/')[1])}</h2><p class="detail-id">${escapeHTML(r.model)} · ${escapeHTML(state.data.date)}</p><dl class="detail-metrics">${item('VERIFIED SCORE',r.complete?r.score+' / 700':'No verified scorecard',r.complete?'Rank '+scoreRank(r):`${r.partial_points??0} partial points`)}${item('DAILY PLACEMENT',r.daily_percentile==null?'—':(r.games?r.daily_percentile.toFixed(2):r.daily_percentile)+'%','Better than today’s players')}${item('ELAPSED TIME',duration(m.run_duration_s),duration(m.inference_duration_s)+' in model calls')}${item('LLM COST',costPrefix(m.cost_basis)+money(m.run_cost_usd),basisText(m.cost_basis))}${item('OUTPUT COST',costPrefix(m.output_cost_basis)+money(m.output_cost_usd),basisText(m.output_cost_basis))}${item('OUTPUT TOKENS',(m.output_tokens==null||m.usage_complete?'':'≥ ')+count(m.output_tokens),`${m.usage_calls}/${m.model_calls} calls have usage`)}</dl><p class="detail-notes">${escapeHTML(r.status)}${r.error_type?' · '+escapeHTML(r.error_type):''} · ${r.rounds_scored}/7 rounds scored · ${r.recoveries} navigation recoveries · ${r.missed_rounds??0} missed questions.<br>${r.scorecard_assisted?'Final score collected after the agent stopped. Remaining questions expired naturally; the harness supplied no answers.<br>':''}Input tokens: ${count(m.input_tokens)}. Output price: ${m.pricing?.completion!=null?money(Number(m.pricing.completion)*1e6)+' / million tokens (saved catalog)':'not available'}. Browser costs excluded.</p>${r.issues?.length?`<section class="round-detail"><h3>Timeouts &amp; failure diagnostics</h3><ul>${r.issues.map(e=>`<li>${escapeHTML(e.round||'Run')} · ${escapeHTML(e.reason||e.category)}${e.http_status?' · HTTP '+escapeHTML(e.http_status):''}${e.provider_name?' · '+escapeHTML(e.provider_name):''}</li>`).join('')}</ul></section>`:''}${r.rounds.map((round,i)=>`<section class="round-detail"><div class="round-meta"><span>ROUND ${i+1} / 7</span><span>${round.points==null?'UNSCORED':round.points+' PTS'}${round.rarity?' · '+escapeHTML(round.rarity):''}</span></div><h3>${escapeHTML(round.prompt)}</h3><table><thead><tr><th>Submitted answer</th><th>Outcome</th><th>Rarity</th><th>Clock</th></tr></thead><tbody>${round.submissions.length?round.submissions.map(s=>`<tr><td>${escapeHTML(s.answer)}</td><td class="${s.outcome==='accepted'?'accepted':s.outcome==='rejected'?'rejected':''}">${escapeHTML(s.outcome?.replaceAll('_',' '))}${s.suggested_answer?' → '+escapeHTML(s.suggested_answer):''}</td><td>${escapeHTML(s.rarity||'—')}</td><td>${s.timer==null?'—':escapeHTML(s.timer)+'s'}</td></tr>`).join(''):'<tr><td colspan="4">No recorded submission.</td></tr>'}</tbody></table>${round.interruptions?.length?`<p class="detail-notes">${round.interruptions.map(escapeHTML).join(', ')}</p>`:''}</section>`).join('')}${r.rounds.length?'':'<p class="empty">No question was reached in this run.</p>'}`;
  $('#run-dialog').showModal();$('#run-dialog').scrollTop=0;
}
function validate(data) {
  if(data?.schema_version!==1 || !Array.isArray(data.runs)||!data.settings||!data.date)throw new Error('Choose a leaderboard.json exported by this harness.');
  if(data.runs.length>2000)throw new Error('This viewer supports up to 2,000 run entries.');
  const ids=new Set();
  for(const r of data.runs){
    if(typeof r.model!=='string'||typeof r.provider!=='string'||!r.metrics||!Array.isArray(r.rounds)||ids.has(r.model))throw new Error('The data contains an invalid or duplicate model.');
    ids.add(r.model);
    if(data.aggregation==='archive_mean'){
      if(!Number.isInteger(r.games)||r.games<2||r.games!==data.games_per_model||r.rounds.length)throw new Error('Invalid aggregate game count or private trajectory included.');
      const ci=r.score_ci95;
      if(!Array.isArray(ci)||ci.length!==2||!ci.every(numeric)||ci[0]>ci[1]||ci[1]>700)throw new Error('Invalid score confidence interval.');
      for(const key of ['score','daily_percentile','run_cost_usd','output_cost_usd','output_tokens','run_duration_s']){
        const stat=r.aggregate_stats?.[key];
        if(!stat||!Number.isInteger(stat.n)||stat.n<0||stat.n>r.games||(stat.mean!=null&&!numeric(stat.mean)))throw new Error('Invalid aggregate metric.');
        if(stat.ci95!=null&&(!Array.isArray(stat.ci95)||stat.ci95.length!==2||!stat.ci95.every(numeric)||stat.ci95[0]>stat.ci95[1]))throw new Error('Invalid metric confidence interval.');
      }
    }

    if(typeof r.complete!=='boolean'||(r.complete&&(!numeric(r.score)||r.score>700))||(!r.complete&&r.score!==null))throw new Error('Invalid score or completion status.');
    if(r.daily_percentile!=null&&(!numeric(r.daily_percentile)||r.daily_percentile>100||!r.complete))throw new Error('Invalid daily placement.');
    for(const key of Object.keys(axes).filter(k=>k!=='daily_percentile'))if(r.metrics[key]!=null&&!numeric(r.metrics[key]))throw new Error('Invalid metric value.');
    for(const key of ['cost_basis','output_cost_basis'])if(typeof r.metrics[key]!=='string')throw new Error('Missing accounting provenance.');
    for(const key of ['rounds_scored','recoveries','missed_rounds','partial_points'])if(r[key]!=null&&!numeric(r[key]))throw new Error('Invalid run count.');
    for(const key of ['usage_calls','model_calls','input_tokens','reasoning_tokens','inference_duration_s'])if(r.metrics[key]!=null&&!numeric(r.metrics[key]))throw new Error('Invalid usage count.');
    if(r.issues!=null&&(!Array.isArray(r.issues)||r.issues.some(x=>!x||typeof x!=='object')))throw new Error('Invalid diagnostics.');
    if(r.rounds.some(x=>!Array.isArray(x.submissions)||(x.points!=null&&!numeric(x.points))))throw new Error('Invalid answer log.');
  }
  return data;
}
function install(data) {
  state.data=validate(data);
  state.placements=new Map(data.runs.filter(r=>r.complete).sort((a,b)=>b.score-a.score||a.model.localeCompare(b.model)).map((r,i)=>[r.model,i+1]));
  state.query='';state.status='all';state.provider='all';state.sort='score';state.direction=-1;state.expanded=false;
  $('#search').value='';$('#provider-filter').innerHTML='<option value="all">All providers</option>'+[...new Set(data.runs.map(r=>r.provider))].sort().map(p=>`<option value="${escapeHTML(p)}">${escapeHTML(providerName(p))}</option>`).join('');
  document.querySelectorAll('#status-filters button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.status==='all')));
  $('#snapshot').textContent=data.aggregation==='archive_mean'?`${data.date_start} – ${data.date_end}`:data.date;
  $('#aggregate-note').hidden=data.aggregation!=='archive_mean';
  $('#context-title').textContent=data.aggregation==='archive_mean'?`${data.games_per_model} daily puzzles.`:'One daily puzzle.';
  $('#report-description').textContent=data.aggregation==='archive_mean'?'Open a model to inspect its aggregate metrics, sample counts, and confidence intervals. Individual answers and trajectories are stored privately.': 'Open any model to inspect its answers, rejections, rarity, and points.';
  $('#aggregate-note').textContent=data.aggregation==='archive_mean'?`Means across ${data.games_per_model} games · score whiskers show 95% confidence intervals`:'';
  const s=data.settings;
  const old=s.round_timeout_policy!=='continue';
  $('#configuration').textContent=old?'This snapshot uses the original harness: 1,500 output tokens, an 18-second model-call limit, and stop-on-failure. It predates timeout recovery.':`This snapshot uses timeout recovery, ${s.max_output_tokens==null?'no harness output-token cap':s.max_output_tokens+' maximum output tokens'}, and ${s.model_retries??0} same-model retries. Navigation recovery: ${s.navigation_recovery??'unspecified'}. ${s.terminal_failure_policy?'Terminal failures use navigation-only collection of the actual final scorecard.':''}`;
  render();
}
$('#expand-results').addEventListener('click',()=>{
  state.expanded=!state.expanded;
  render();
  // Keep the collapse control reachable when removing rows shortens the page.
  const button=$('#expand-results'), bounds=button.getBoundingClientRect();
  if(bounds.top<0||bounds.bottom>window.innerHeight)button.scrollIntoView({block:'center',behavior:'instant'});
});
$('#search').addEventListener('input',e=>{state.query=e.target.value.trim().toLowerCase();render();});
$('#provider-filter').addEventListener('change',e=>{state.provider=e.target.value;render();});
$('#status-filters').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;state.status=b.dataset.status;document.querySelectorAll('#status-filters button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render();});
$('#chart-metrics').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;state.axis=b.dataset.metric;document.querySelectorAll('#chart-metrics button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));renderChart(visibleRows());});
document.querySelector('thead').addEventListener('click',e=>{const th=e.target.closest('[data-sort]');if(!th)return;const key=th.dataset.sort;state.direction=state.sort===key?-state.direction: ['score','daily_percentile'].includes(key)?-1:1;state.sort=key;render();});
$('#results').addEventListener('click',e=>{const b=e.target.closest('[data-model]');if(b)openDetails(b.dataset.model);});
$('#chart').addEventListener('click',e=>{const b=e.target.closest('[data-model]');if(b)openDetails(b.dataset.model);});
$('#chart').addEventListener('keydown',e=>{if(['Enter',' '].includes(e.key)&&e.target.dataset.model){e.preventDefault();openDetails(e.target.dataset.model);}});
$('#chart').addEventListener('pointerover',e=>{const b=e.target.closest('[data-model]');if(!b)return;const r=state.data.runs.find(r=>r.model===b.dataset.model);$('#chart-tooltip').textContent=`${r.model} · ${scoreText(r.score)} / 700 · ${axes[state.axis]}: ${state.axis.includes('cost')?costPrefix(r.metrics[state.axis==='run_cost_usd'?'cost_basis':'output_cost_basis'])+money(metric(r,state.axis)):count(metric(r,state.axis))}`;$('#chart-tooltip').hidden=false;});
$('#chart').addEventListener('pointerleave',()=>{$('#chart-tooltip').hidden=true;});
$('#close-dialog').addEventListener('click',()=>$('#run-dialog').close());
$('#run-dialog').addEventListener('click',e=>{if(e.target===$('#run-dialog')){const r=e.target.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)e.target.close();}});
$('#metric-info').addEventListener('click',()=>{$('#metric-definitions').open=true;$('#metric-definitions').scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});});
function setCalm(calm) {
  document.body.classList.toggle('calm',calm);
  $('#theme').setAttribute('aria-pressed',String(calm));
  $('#theme').setAttribute('aria-label',calm?'Enable ocean effects':'Reduce ocean effects');
  $('#theme').title=calm?'Enable ocean effects':'Reduce ocean effects';
}
$('#theme').addEventListener('click',()=>{
  const calm=!document.body.classList.contains('calm');setCalm(calm);
  try{localStorage.setItem('krillion-calm',String(calm));}catch{}
  scheduleOcean();
});
try{setCalm(localStorage.getItem('krillion-calm')==='true');}catch{}
const motionPreference=window.matchMedia('(prefers-reduced-motion: reduce)');
let oceanFrame=0;
function updateOcean() {
  oceanFrame=0;
  const maxScroll=document.documentElement.scrollHeight-window.innerHeight;
  const progress=maxScroll>0?Math.min(1,Math.max(0,window.scrollY/maxScroll)):0;
  const still=motionPreference.matches||document.body.classList.contains('calm');
  const travel=Math.max(0,4800-window.innerHeight);
  $('#ocean-world').style.transform=`translate3d(0,${still?0:-progress*travel}px,0)`;
  $('#dive-depth').textContent=`${Math.round(progress*7000).toLocaleString('en-US')}m`;
  $('#dive-zone').textContent=progress<.06?'SURFACE':progress<.25?'SUNLIGHT':progress<.5?'MIDNIGHT':progress<.8?'ABYSSAL':'HADAL';
  $('#depth-marker').style.top=`${progress*100}%`;
}
function scheduleOcean(){if(!oceanFrame)oceanFrame=requestAnimationFrame(updateOcean);}
window.addEventListener('scroll',scheduleOcean,{passive:true});
window.addEventListener('resize',scheduleOcean);
motionPreference.addEventListener('change',scheduleOcean);
new ResizeObserver(scheduleOcean).observe(document.body);
scheduleOcean();
$('#download').addEventListener('click',()=>{if(!state.data)return;const url=URL.createObjectURL(new Blob([JSON.stringify(state.data,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='krillion-leaderboard.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
$('#load-button').addEventListener('click',()=>$('#load-file').click());
$('#load-file').addEventListener('change',async e=>{const f=e.target.files[0];if(!f)return;try{if(f.size>15e6)throw new Error('Choose a JSON export smaller than 15 MB.');install(JSON.parse(await f.text()));$('#load-status').textContent='Loaded '+f.name;}catch(err){$('#load-status').textContent=err.message;}e.target.value='';});
fetch('leaderboard-data.json').then(r=>{if(!r.ok)throw new Error('Unable to load leaderboard data.');return r.json();}).then(install).catch(e=>{$('#results').innerHTML=`<tr><td colspan="8" class="empty">${escapeHTML(e.message)} Serve this directory over HTTP, or use Load campaign.</td></tr>`;$('#snapshot').textContent='Data unavailable';});

window.addEventListener('resize',()=>{if(state.data)renderChart(visibleRows());});


// This endpoint contains aggregate counts only; private reports never reach the site.
let campaignProgress = null;
function renderCampaignProgress() {
  if (!campaignProgress) return;
  const p = campaignProgress;
  const age = Date.now() - Date.parse(p.updated_at);
  const stale = age > 600000 && ['running', 'draining'].includes(p.status);
  $('#campaign-progress').dataset.stale = String(stale);
  $('#campaign-progress-count').textContent = `${count(p.verified)} / ${count(p.total)} · ${(100*p.verified/p.total).toFixed(2)}%`;
  $('#campaign-progress-bar').value = p.verified;
  const status = {running:`${p.workers} workers · ${p.active} active at last update`,draining:`Finishing ${p.active} games before pausing`,paused:'Paused',needs_attention:'Paused for a health check',complete:'All games verified'}[p.status];
  $('#campaign-progress-state').textContent = stale ? 'Update delayed · showing last verified count' : status;
  $('#campaign-progress-time').textContent = `Updated ${new Date(p.updated_at).toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'})} · may lag up to 5 min`;
}
async function refreshCampaignProgress() {
  try {
    const url = 'https://raw.githubusercontent.com/Anupam-Anupam/Krillion-Bench/refs/heads/campaign-status/campaign-progress.json';
    const response = await fetch(url, {cache:'no-store', signal:AbortSignal.timeout(12000)});
    if (!response.ok) throw new Error('Progress unavailable');
    const p = await response.json();
    if (p.campaign !== 'archive-75-20261106-v3' || p.total !== 7500 ||
        ![p.verified,p.active,p.workers].every(Number.isInteger) || p.verified < 0 || p.verified > p.total ||
        p.active < 0 || p.active > p.workers || p.workers < 1 || p.workers > 20 ||
        !['running','draining','paused','needs_attention','complete'].includes(p.status) ||
        !Number.isFinite(Date.parse(p.updated_at))) throw new Error('Invalid progress');
    // A cache must never move an already displayed counter backward.
    if (!campaignProgress || Date.parse(p.updated_at) >= Date.parse(campaignProgress.updated_at)) campaignProgress = p;
    renderCampaignProgress();
  } catch {
    if (campaignProgress) renderCampaignProgress();
    else $('#campaign-progress-state').textContent = 'Progress temporarily unavailable';
  }
}
refreshCampaignProgress();
// The raw CDN caches for five minutes; label snapshot age explicitly.
setInterval(()=>{if(!document.hidden)refreshCampaignProgress();}, 60000);
setInterval(renderCampaignProgress, 15000);
