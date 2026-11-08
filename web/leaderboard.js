'use strict';
const $ = (selector) => document.querySelector(selector);
const escapeHTML = (value) => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const palette = {openai:'#4de3ff',anthropic:'#ffb787',google:'#b6e897',moonshotai:'#ff79a5','x-ai':'#d3def5','z-ai':'#55e6bd',deepseek:'#8bafff',meta:'#dbabff',qwen:'#ffd166'};
const color = provider => palette[provider] || '#96a19a';
const providerName = p => ({openai:'OpenAI',anthropic:'Anthropic',google:'Google',moonshotai:'Moonshot','x-ai':'xAI','z-ai':'Z.ai',deepseek:'DeepSeek',meta:'Meta',qwen:'Qwen'}[p] || p);
const axes = {run_cost_usd:'LLM cost / run · USD', output_cost_usd:'Output cost / run · USD',output_tokens:'Output tokens / run',run_duration_s:'Elapsed time / run · seconds',daily_percentile:'Better than today’s players · %'};
const state = {data:null, query:'', weights:'all', view:'average', days:[], weightMetadata:{}, provider:'all', sort:'score', direction:-1, axis:'run_cost_usd', expanded:false};
const numeric = v => typeof v === 'number' && Number.isFinite(v) && v >= 0;
const count = v => v == null ? '—' : new Intl.NumberFormat('en-US',{maximumFractionDigits:0}).format(v);
const money = v => v == null ? '—' : v === 0 ? '$0.0000' : v < .0001 ? '$'+v.toFixed(6) : '$'+v.toFixed(4);
const duration = v => v == null ? '—' : v >= 60 ? `${Math.floor(Math.round(v)/60)}m ${Math.round(v)%60}s` : `${v.toFixed(1)}s`;
const costPrefix = basis => basis?.startsWith('partial_') ? (basis.includes('estimated') || basis.includes('mixed') ? '≥≈ ' : '≥ ') : basis === 'estimated' || basis === 'mixed' ? '≈ ' : '';
function basisText(basis) {
  return ({reported:'API-reported account charge',provider_reported:'Provider-reported output component',estimated:'Catalog estimate',mixed:'Mixed reported and estimated',partial_reported:'Partial reported charge',partial_provider_reported:'Partial provider output cost',partial_estimated:'Partial catalog estimate',partial_mixed:'Partial mixed accounting',unavailable:'Not recorded'})[basis] || 'Not recorded';
}
function metric(row,key) { if(key==='rank')return row.complete?scoreRank(row):null; return ['score','daily_percentile'].includes(key) ? row[key] : key === 'model' ? row.model : row.metrics[key]; }
function filteredRows(data) {
  return data.runs.filter(r => (state.weights === 'all' || (r.weight_access || state.weightMetadata[r.model]?.weight_access) === state.weights) &&
    (state.provider === 'all' || r.provider === state.provider) && `${r.model} ${r.name}`.toLowerCase().includes(state.query));
}
function visibleRows() { return filteredRows(state.data); }
function averageSnapshot() { return state.aggregate || averageDays(state.days); }
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
  return badge ? `<img class="rank-badge ${badge.key}" src="web/assets/images/krillion-${badge.key}.png" width="36" height="36" alt="${badge.label}, overall position ${position}" title="${badge.label} · overall position ${position}">` : '';
}
const scoreText = value => new Intl.NumberFormat('en-US',{maximumFractionDigits:0}).format(value);
function scoreMarkup(row) {
  return `<div class="score-bar"><div class="score-fill" style="width:${row.score/700*100}%"></div><span class="score-value">${scoreText(row.score)}<small>/ 700</small></span></div>`;
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
    return `<tr data-tier="${badge?.key||'none'}" class="${r.complete?'':'incomplete'}"><td class="rank">${scoreRank(r)}</td><td class="model-cell"><button class="model-button" data-model="${escapeHTML(r.model)}" ${state.view==='average'?'tabindex="-1" aria-disabled="true"':''} aria-label="${state.view==='average'?escapeHTML(r.model)+' average metrics':state.data.numeric_only?'View '+escapeHTML(r.model)+' daily report':'View '+escapeHTML(r.model)+' run details'}">${badgeMarkup(r)}<span><span class="model-name">${escapeHTML(display)}</span><span class="variant">${escapeHTML(providerName(r.provider))}${r.model.endsWith(':free')?' · free endpoint':''}${r.missed_rounds?' · '+r.missed_rounds+' missed':''}${r.scorecard_assisted?' · recovery':''}</span></span></button></td><td class="score-cell">${r.complete?scoreMarkup(r):`<span class="incomplete-label">${state.view==='average'?(r.status==='awaiting_first_run'?'Awaiting first run':r.model==='xingchen-agi/xing4.0-29b-a4b:free'?'Provider quota blocked':'No clean score'):'Run error'} <small>${state.view==='average'?'':escapeHTML(r.error_type || r.status)}</small></span>`}</td><td>${cost(m.run_cost_usd,m.cost_basis)}</td><td>${cost(m.output_cost_usd,m.output_cost_basis)}</td><td title="${state.view==='average'?(r.aggregate_stats?.output_tokens?.n??0)+' tested days with complete token usage':m.usage_calls+' of '+m.model_calls+' calls have usage'}">${tokens}</td><td>${duration(m.run_duration_s)}</td><td class="daily">${r.daily_percentile == null?'—':(r.aggregate_stats?r.daily_percentile.toFixed(2):r.daily_percentile)+'%'}</td></tr>`;
  }).join('') || '<tr><td colspan="8" class="empty">No models match these filters. Try another name or provider.</td></tr>';
  $('#row-count').textContent=`Showing ${rows.length} of ${matches.length}${matches.length===state.data.runs.length?' models':' matching models'}${state.view==='average'?' · average metrics only':state.data.numeric_only?' · click a model for its daily report':' · click a model to inspect its dive'}`;
  const expand=$('#expand-results');
  expand.hidden=matches.length<=5;
  expand.setAttribute('aria-expanded',String(state.expanded));
  expand.textContent=state.expanded?'Show fewer models ↑':`Show all ${matches.length} models ↓`;
  document.querySelectorAll('th[data-sort]').forEach(th=>{
    const selected=th.dataset.sort===state.sort;
    th.setAttribute('aria-sort',selected?(state.direction===-1?'descending':'ascending'):'none');
    th.querySelector('span').textContent=selected?(state.direction===-1?'↓':'↑'):'';
  });
  renderChart();
}

function renderChart() {
  const rows=filteredRows(averageSnapshot());
  const key=state.axis;
  const eligible=rows.filter(r=>r.complete && numeric(metric(r,key)) && (!key.includes('cost') || !r.metrics[key==='run_cost_usd'?'cost_basis':'output_cost_basis'].startsWith('partial_')) && (key!=='output_tokens'||r.metrics.usage_complete||r.aggregate_stats?.output_tokens?.n>0));
  $('#plot-direction').textContent=key==='daily_percentile'?'Higher score, higher placement ↗':'Higher score, lower '+({run_cost_usd:'cost',output_cost_usd:'output cost',output_tokens:'token use',run_duration_s:'time'}[key])+' ↖';
  $('#axis-label').textContent=axes[key];
  $('#chart-tooltip').hidden=true;
  if(!eligible.length){$('#chart').innerHTML='<p class="empty">No completed runs with this metric match your filters.</p>';$('#legend').innerHTML='';return;}
  const compact=window.matchMedia('(max-width:760px)').matches;
  const W=compact?420:1000,H=compact?300:310,L=46,R=25,T=24,B=38;
  const xmax=key==='daily_percentile'?100:Math.max(...eligible.map(r=>metric(r,key)),.0001)*1.1;
  const x=v=>L+v/xmax*(W-L-R),y=v=>H-B-v/700*(H-T-B);
  let svg=`<svg viewBox="0 0 ${W} ${H}" role="group" aria-label="Average Krillion score versus ${escapeHTML(axes[key])}. Each point shows average metrics.">`;
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
    svg+=`<circle class="plot-point" cx="${cx}" cy="${cy}" r="4.5" fill="${color(r.provider)}" data-model="${escapeHTML(r.model)}" aria-label="${escapeHTML(r.model)}, score ${scoreText(r.score)}, ${escapeHTML(formatted)}"><title>${escapeHTML(r.model)} · ${scoreText(r.score)} / 700 · ${escapeHTML(formatted)}</title></circle>`;
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
function readableRounds(rounds) { return rounds.map((round,i)=>`<section class="round-detail"><div class="round-meta"><span>ROUND ${i+1} / 7</span><span>${round.points==null?'UNSCORED':round.points+' PTS'}${round.rarity?' · '+escapeHTML(round.rarity):''}</span></div><h3>${escapeHTML(round.prompt)}</h3><table><thead><tr><th>Submitted answer</th><th>Outcome</th><th>Rarity</th><th>Clock</th></tr></thead><tbody>${round.submissions.length?round.submissions.map(s=>`<tr><td>${escapeHTML(s.answer)}</td><td class="${s.outcome==='accepted'?'accepted':s.outcome==='rejected'?'rejected':''}">${escapeHTML(s.outcome?.replaceAll('_',' '))}${s.suggested_answer?' → '+escapeHTML(s.suggested_answer):''}</td><td>${escapeHTML(s.rarity||'—')}</td><td>${s.timer==null?'—':escapeHTML(s.timer)+'s'}</td></tr>`).join(''):'<tr><td colspan="4">No recorded submission.</td></tr>'}</tbody></table>${round.interruptions?.length?`<p class="detail-notes">${round.interruptions.map(escapeHTML).join(', ')}</p>`:''}</section>`).join(''); }
let reportRequest = 0;
const reportCache = new Map();
async function openDetails(id) {
  if(state.view==='average')return;
  const r=state.data.runs.find(r=>r.model===id);if(!r)return;
  const request=++reportRequest;
  if(state.data.numeric_only){
    const day=state.data.date;
    const heading=`<h2 id="detail-title">${escapeHTML(r.model.split('/').slice(1).join('/'))}</h2><p class="detail-id">${escapeHTML(day)} · ${scoreText(r.score)} / 700</p>`;
    $('#detail-content').innerHTML=heading+'<p class="detail-notes" role="status">Loading verified report…</p>';
    $('#run-dialog').showModal();$('#run-dialog').scrollTop=0;
    try {
      const key=day+'/'+r.model;
      let report=reportCache.get(key);
      if(!report){
        const configResponse=await fetch('web/data/report-service.json', {cache:'no-cache'});
        if(!configResponse.ok)throw new Error('Service configuration unavailable.');
        const config=await configResponse.json();
        if(!config.endpoint)throw new Error('Report service is being connected. Please try again shortly.');
        const endpoint=new URL(config.endpoint);
        if(endpoint.protocol!=='https:')throw new Error('Invalid report service configuration.');
        const response=await fetch(endpoint.href.replace(/\/$/,'')+'/reports/'+encodeURIComponent(day)+'/'+encodeURIComponent(r.model), {credentials:'omit',signal:AbortSignal.timeout(60000)});
        if(!response.ok)throw new Error('Report temporarily unavailable. Please try again.');
        report=await response.json();
        if(report.model!==r.model||report.date!==day||report.score!==r.score||report.rounds?.length!==7||report.rounds.reduce((n,round)=>n+round.points,0)!==r.score||report.rounds.some(round=>!Array.isArray(round.submissions)))throw new Error('Report validation failed.');
        reportCache.set(key,report);
      }
      if(request!==reportRequest||state.view!=='daily'||state.data.date!==day||!$('#run-dialog').open)return;
      $('#detail-content').innerHTML=heading+readableRounds(report.rounds);
    } catch(error) {
      if(request!==reportRequest||state.view!=='daily'||state.data.date!==day||!$('#run-dialog').open)return;
      $('#detail-content').innerHTML=heading+'<p class="detail-notes" role="status">'+escapeHTML(error.message)+'</p>';
    }
    return;
  }
  const m=r.metrics;
  const item=(label,value,note='')=>`<div><dt>${label}</dt><dd>${escapeHTML(value)}${note?`<small>${escapeHTML(note)}</small>`:''}</dd></div>`;
  $('#detail-content').innerHTML=`<h2 id="detail-title">${escapeHTML(r.model.split('/')[1])}</h2><p class="detail-id">${escapeHTML(r.model)} · ${escapeHTML(state.data.date)}</p><dl class="detail-metrics">${item('VERIFIED SCORE',r.complete?r.score+' / 700':'No verified scorecard',r.complete?'Rank '+scoreRank(r):`${r.partial_points??0} partial points`)}${item('DAILY PLACEMENT',r.daily_percentile==null?'—':(r.aggregate_stats?r.daily_percentile.toFixed(2):r.daily_percentile)+'%','Better than today’s players')}${item('ELAPSED TIME',duration(m.run_duration_s),duration(m.inference_duration_s)+' in model calls')}${item('LLM COST',costPrefix(m.cost_basis)+money(m.run_cost_usd),basisText(m.cost_basis))}${item('OUTPUT COST',costPrefix(m.output_cost_basis)+money(m.output_cost_usd),basisText(m.output_cost_basis))}${item('OUTPUT TOKENS',(m.output_tokens==null||m.usage_complete?'':'≥ ')+count(m.output_tokens),`${m.usage_calls}/${m.model_calls} calls have usage`)}</dl><p class="detail-notes">${escapeHTML(r.status)}${r.error_type?' · '+escapeHTML(r.error_type):''} · ${r.rounds_scored}/7 rounds scored · ${r.recoveries} navigation recoveries · ${r.missed_rounds??0} missed questions.<br>${r.scorecard_assisted?'Final score collected after the agent stopped. Remaining questions expired naturally; the harness supplied no answers.<br>':''}Input tokens: ${count(m.input_tokens)}. Output price: ${m.pricing?.completion!=null?money(Number(m.pricing.completion)*1e6)+' / million tokens (saved catalog)':'not available'}. Browser costs excluded.</p>${r.issues?.length?`<section class="round-detail"><h3>Timeouts &amp; failure diagnostics</h3><ul>${r.issues.map(e=>`<li>${escapeHTML(e.round||'Run')} · ${escapeHTML(e.reason||e.category)}${e.http_status?' · HTTP '+escapeHTML(e.http_status):''}${e.provider_name?' · '+escapeHTML(e.provider_name):''}</li>`).join('')}</ul></section>`:''}${r.rounds.map((round,i)=>`<section class="round-detail"><div class="round-meta"><span>ROUND ${i+1} / 7</span><span>${round.points==null?'UNSCORED':round.points+' PTS'}${round.rarity?' · '+escapeHTML(round.rarity):''}</span></div><h3>${escapeHTML(round.prompt)}</h3><table><thead><tr><th>Submitted answer</th><th>Outcome</th><th>Rarity</th><th>Clock</th></tr></thead><tbody>${round.submissions.length?round.submissions.map(s=>`<tr><td>${escapeHTML(s.answer)}</td><td class="${s.outcome==='accepted'?'accepted':s.outcome==='rejected'?'rejected':''}">${escapeHTML(s.outcome?.replaceAll('_',' '))}${s.suggested_answer?' → '+escapeHTML(s.suggested_answer):''}</td><td>${escapeHTML(s.rarity||'—')}</td><td>${s.timer==null?'—':escapeHTML(s.timer)+'s'}</td></tr>`).join(''):'<tr><td colspan="4">No recorded submission.</td></tr>'}</tbody></table>${round.interruptions?.length?`<p class="detail-notes">${round.interruptions.map(escapeHTML).join(', ')}</p>`:''}</section>`).join('')}${r.rounds.length?'':'<p class="empty">No question was reached in this run.</p>'}`;
  $('#run-dialog').showModal();$('#run-dialog').scrollTop=0;
}
function validate(data) {
  if(data?.schema_version!==1 || !Array.isArray(data.runs)||!data.settings||!data.date)throw new Error('Choose a leaderboard.json exported by this harness.');
  if(data.aggregation==='archive_partial_mean'&&(data.runs.length!==100||data.target_games!==7500||data.verified_games!==data.runs.reduce((n,r)=>n+r.games,0)))throw new Error('Invalid provisional coverage.');
  if(data.runs.length>2000)throw new Error('This viewer supports up to 2,000 run entries.');
  const ids=new Set();
  for(const r of data.runs){
    if(typeof r.model!=='string'||typeof r.provider!=='string'||!r.metrics||!Array.isArray(r.rounds)||ids.has(r.model))throw new Error('The data contains an invalid or duplicate model.');
    ids.add(r.model);
    if(data.numeric_only&&(!r.report_object?.startsWith('campaigns/archive-75-20261106-v3/games/'+data.date+'/models/')||!r.report_object.endsWith('/report.json.gz')))throw new Error('Missing exact private report identity.');
    if(data.aggregation==='archive_partial_mean'){
      if(!data.provisional||!Number.isInteger(r.games)||r.games<0||r.games>75||r.rounds.length||r.complete!==(r.games>0))throw new Error('Invalid provisional average.');
      for(const key of ['score','daily_percentile','run_cost_usd','output_cost_usd','output_tokens','run_duration_s']){const stat=r.aggregate_stats?.[key];if(!stat||!Number.isInteger(stat.n)||stat.n<0||stat.n>r.games||(stat.mean!=null&&!numeric(stat.mean)))throw new Error('Invalid provisional metric.');}
    }
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
function displaySnapshot(data) {
  state.data=data;
  state.placements=new Map(data.runs.filter(r=>r.complete).sort((a,b)=>b.score-a.score||a.model.localeCompare(b.model)).map((r,i)=>[r.model,i+1]));
  state.expanded=false;
  $('#provider-filter').innerHTML='<option value="all">All providers</option>'+[...new Set(data.runs.map(r=>r.provider))].sort().map(p=>`<option value="${escapeHTML(p)}">${escapeHTML(providerName(p))}</option>`).join('');
  $('#provider-filter').value=state.provider;
  document.querySelectorAll('#view-filters button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===state.view)));
  $('#daily-controls').hidden=state.view!=='daily'||!state.days.length;
  $('#calendar-date').textContent=$('#day-filter').value;
  $('#view-note').hidden=state.view==='average';
  if(state.view!=='daily')closeCalendar(false);
  $('#view-note').textContent=data.aggregation==='archive_partial_mean'?`Provisional average · ${count(data.verified_games)} clean verified games · ${data.coverage.min}–${data.coverage.max} of 75 dates per model. Date coverage varies; this is not the final balanced comparison.`:state.view==='average'?(data.aggregation==='archive_mean'?`Average metrics across all ${data.games_per_model} tested days.`:`Average metrics across ${state.days.length} published tested ${state.days.length===1?'day · more days will appear after publication.':'days; available sample counts appear in model details.'}`):`Daily metrics for ${data.date}.`;
  document.querySelector('table caption').textContent=state.view==='average'?'Krillion provisional average metrics from clean verified scorecards.':state.data.numeric_only?'Krillion daily metrics from clean verified scorecards. Select a model for its daily report.':'Krillion daily benchmark results. Select a model for run details.';
  $('#snapshot').textContent=['archive_mean','archive_partial_mean','published_mean'].includes(data.aggregation)?`${data.date_start} – ${data.date_end}`:data.date;
  $('#aggregate-note').hidden=data.aggregation!=='archive_mean';
  $('#context-title').textContent=data.aggregation==='archive_partial_mean'?'Archive results so far.':state.view==='average'?`${data.games_per_model||state.days.length} tested daily ${data.games_per_model===1||state.days.length===1?'puzzle':'puzzles'}.`:'One daily puzzle.';
  $('#report-description').textContent=state.view==='average'?'Average shows numeric metrics only; rows and graph dots do not open reports.': state.data.numeric_only?'Select a model to inspect the questions, answers and points from its verified clean run for this date.':'Open any model to inspect its answers, rejections, rarity, and points.';
  $('#aggregate-note').textContent=data.aggregation==='archive_mean'?`Means across ${data.games_per_model} games`:'';
  const s=data.settings;
  const old=s.round_timeout_policy!=='continue';
  $('#configuration').textContent=data.aggregation==='archive_partial_mean'?data.protocol_amendments.join(' '):data.numeric_only?'Clean latest verified scorecards for this tested date. Models still awaiting a clean result are omitted. Five-word instruction amendment and authorized infrastructure replays are retained.':old?'This snapshot uses the original harness: 1,500 output tokens, an 18-second model-call limit, and stop-on-failure. It predates timeout recovery.':`This snapshot uses timeout recovery, ${s.max_output_tokens==null?'no harness output-token cap':s.max_output_tokens+' maximum output tokens'}, and ${s.model_retries??0} same-model retries. Navigation recovery: ${s.navigation_recovery??'unspecified'}. ${s.terminal_failure_policy?'Terminal failures use navigation-only collection of the actual final scorecard.':''}`;
  render();
}
// Average only published snapshots from the same tested configuration.
// The archive average uses its separately validated numeric snapshot.
function averageDays(days) {
  const base=days[0], keys=['score','daily_percentile','run_cost_usd','output_cost_usd','output_tokens','run_duration_s'];
  const models=[...new Set(days.flatMap(d=>d.runs.map(r=>r.model)))];
  const runs=models.map(model=>{
    const samples=days.flatMap(d=>d.runs.filter(r=>r.model===model&&r.complete));
    const original=days.flatMap(d=>d.runs).find(r=>r.model===model);
    const stats=Object.fromEntries(keys.map(key=>{
      const values=samples.filter(r=>!key.includes('cost')||!r.metrics[key==='run_cost_usd'?'cost_basis':'output_cost_basis'].startsWith('partial_')).filter(r=>key!=='output_tokens'||r.metrics.usage_complete).map(r=>metric(r,key)).filter(numeric);
      return [key,{n:values.length,mean:values.length?values.reduce((a,b)=>a+b,0)/values.length:null,ci95:null}];
    }));
    const metrics={...original.metrics,...Object.fromEntries(keys.filter(k=>!['score','daily_percentile'].includes(k)).map(k=>[k,stats[k].mean])),usage_complete:true};
    for(const [key,basis] of [['run_cost_usd','cost_basis'],['output_cost_usd','output_cost_basis']]){
      const bases=new Set(samples.filter(r=>numeric(r.metrics[key])&&!r.metrics[basis].startsWith('partial_')).map(r=>r.metrics[basis]));
      metrics[basis]=bases.size===1?[...bases][0]:bases.size?'mixed':'unavailable';
    }
    return {...original,complete:samples.length>0,score:stats.score.mean,daily_percentile:stats.daily_percentile.mean,metrics,games:samples.length,aggregate_stats:stats,score_ci95:null,rounds:[]};
  });
  const dates=days.map(d=>d.date).sort();
  return {...base,aggregation:'published_mean',date_start:dates[0],date_end:dates.at(-1),date:dates.at(-1),runs};
}
function selectView() {
  ++reportRequest;
  if($('#run-dialog').open)$('#run-dialog').close();
  displaySnapshot(state.view==='average'?(state.aggregate||averageDays(state.days)):state.days.find(d=>d.date===$('#day-filter').value)||state.days[0]);
}
function install(data) {
  validate(data);
  state.aggregate=['archive_mean','archive_partial_mean'].includes(data.aggregation)?data:(state.publishedAverage||null);
  state.days=state.publishedDays?[data,...state.publishedDays.map(validate)]:['archive_mean','archive_partial_mean'].includes(data.aggregation)?(data.daily_snapshots||[]).map(validate):[data,...(data.daily_snapshots||[]).map(validate)];
  if(new Set(state.days.map(d=>d.date)).size!==state.days.length)throw new Error('Duplicate daily snapshot.');
  if(!state.publishedDays&&state.days.some(d=>JSON.stringify(d.settings)!==JSON.stringify(state.days[0].settings)||JSON.stringify(d.source_sha256)!==JSON.stringify(state.days[0].source_sha256)))throw new Error('Daily snapshots must use the same tested configuration.');
  state.days.sort((a,b)=>b.date.localeCompare(a.date));
  state.view='average';
  $('#day-filter').innerHTML=state.days.map(d=>`<option value="${escapeHTML(d.date)}">${escapeHTML(d.date)}</option>`).join('');
  $('#view-filters [data-view="daily"]').disabled=!state.days.length;
  $('#view-filters [data-view="daily"]').title=state.days.length?'View a tested day':'Daily snapshots have not been published for this aggregate';
  selectView();
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
$('#model-filters').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;state.weights=b.dataset.weights;document.querySelectorAll('#model-filters button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render();});
$('#view-filters').addEventListener('click',e=>{const b=e.target.closest('button');if(!b||b.disabled)return;state.view=b.dataset.view;selectView();});
let calendarMonth='';
function closeCalendar(focus=true){$('#date-calendar').hidden=true;$('#calendar-toggle').setAttribute('aria-expanded','false');if(focus)$('#calendar-toggle').focus();}
function renderCalendar(){
  const [year,month]=calendarMonth.split('-').map(Number),first=new Date(year,month-1,1),days=new Date(year,month,0).getDate();
  const tested=new Set(state.days.map(d=>d.date)),selected=$('#day-filter').value;
  $('#calendar-month').textContent=first.toLocaleDateString('en-US',{month:'long',year:'numeric'});
  $('#calendar-days').innerHTML='<span></span>'.repeat(first.getDay())+Array.from({length:days},(_,i)=>{
    const date=calendarMonth+'-'+String(i+1).padStart(2,'0'),available=tested.has(date);
    return `<button type="button" data-date="${date}" ${available?'':'disabled'} ${date===selected?'aria-current="date"':''} aria-label="${date}${available?', tested scores available':', no tested scores'}">${i+1}</button>`;
  }).join('');
  const months=state.days.map(d=>d.date.slice(0,7)).sort();
  $('#calendar-prev').disabled=calendarMonth<=months[0];$('#calendar-next').disabled=calendarMonth>=months.at(-1);
}
$('#calendar-toggle').addEventListener('click',()=>{if(!$('#date-calendar').hidden){closeCalendar();return;}calendarMonth=$('#day-filter').value.slice(0,7);renderCalendar();$('#date-calendar').hidden=false;$('#calendar-toggle').setAttribute('aria-expanded','true');($('#calendar-days [aria-current]')||$('#calendar-days button:not(:disabled)')).focus();});
for(const [id,delta] of [['calendar-prev',-1],['calendar-next',1]])$('#'+id).addEventListener('click',()=>{const [y,m]=calendarMonth.split('-').map(Number),d=new Date(y,m-1+delta,1);calendarMonth=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0');renderCalendar();});
$('#calendar-days').addEventListener('click',e=>{const b=e.target.closest('button[data-date]');if(!b||b.disabled)return;$('#day-filter').value=b.dataset.date;selectView();closeCalendar();});
document.addEventListener('click',e=>{if(!e.target.closest('.date-picker'))closeCalendar(false);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('#date-calendar').hidden){e.preventDefault();closeCalendar();}});
$('#day-filter').addEventListener('change',selectView);
$('#chart-metrics').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;state.axis=b.dataset.metric;document.querySelectorAll('#chart-metrics button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));renderChart();});
document.querySelector('thead').addEventListener('click',e=>{const th=e.target.closest('[data-sort]');if(!th)return;const key=th.dataset.sort;state.direction=state.sort===key?-state.direction: ['score','daily_percentile'].includes(key)?-1:1;state.sort=key;render();});
$('#results').addEventListener('click',e=>{const b=e.target.closest('[data-model]');if(b)openDetails(b.dataset.model);});
$('#chart').addEventListener('pointerover',e=>{const b=e.target.closest('[data-model]');if(!b)return;const r=averageSnapshot().runs.find(r=>r.model===b.dataset.model);$('#chart-tooltip').textContent=`${r.model} · Average ${scoreText(r.score)} / 700 · ${axes[state.axis]}: ${state.axis.includes('cost')?costPrefix(r.metrics[state.axis==='run_cost_usd'?'cost_basis':'output_cost_basis'])+money(metric(r,state.axis)):count(metric(r,state.axis))}`;$('#chart-tooltip').hidden=false;});
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
$('#load-file').addEventListener('change',async e=>{const f=e.target.files[0];if(!f)return;try{if(f.size>15e6)throw new Error('Choose a JSON export smaller than 15 MB.');state.publishedDays=null;state.publishedAverage=null;install(JSON.parse(await f.text()));$('#load-status').textContent='Loaded '+f.name;}catch(err){$('#load-status').textContent=err.message;}e.target.value='';});
fetch('web/data/model-weights.json').then(r=>{if(!r.ok)throw new Error('Unable to load model weight metadata.');return r.json();}).then(metadata=>{state.weightMetadata=metadata.models;return fetch('web/data/archive-average.json?v=20261108-replacement').then(r=>{if(!r.ok)throw new Error('Unable to load verified averages.');return r.json();}).then(average=>{state.publishedAverage=validate(average);return fetch('web/data/archive-daily.json?v=20261108-daily-reports').then(r=>{if(!r.ok)throw new Error('Unable to load tested dates.');return r.json();}).then(d=>{state.publishedDays=d.daily_snapshots;return fetch('web/data/leaderboard-data.json');});});}).then(r=>{if(!r.ok)throw new Error('Unable to load leaderboard data.');return r.json();}).then(install).catch(e=>{$('#results').innerHTML=`<tr><td colspan="8" class="empty">${escapeHTML(e.message)} Serve this directory over HTTP, or use Load campaign.</td></tr>`;$('#snapshot').textContent='Data unavailable';});

window.addEventListener('resize',()=>{if(state.data)renderChart();});
