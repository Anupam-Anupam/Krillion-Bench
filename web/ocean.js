const $=selector=>document.querySelector(selector);
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
