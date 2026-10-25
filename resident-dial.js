(()=>{
'use strict';
// Exact critically damped motion: weight and deceleration without overshoot.
function advanceDial(position,velocity,target,dt){
  const frequency=11;
  const offset=position-target;
  const impulse=(velocity+frequency*offset)*dt;
  const decay=Math.exp(-frequency*dt);
  return {position:target+(offset+impulse)*decay,velocity:(velocity-frequency*impulse)*decay};
}
const section=document.querySelector('#resident-comfort');
if(!section)return;
const deck=section.querySelector('.resident-deck');
const cards=[...deck.querySelectorAll('.resident-card')];
const mobile=matchMedia('(max-width:760px) and (min-height:620px)');
const reduced=matchMedia('(prefers-reduced-motion:reduce)');
const clamp=(n,min,max)=>Math.max(min,Math.min(max,n));
let enabled=false,track,stage,controls,ring,counter,buttons=[];
let position=0,velocity=0,target=0,raf=0,lastTime=0,start=0,travel=1,radius=240,selected=-1,top=98;
let resizeTimer=0,measuredWidth=0,viewportBasis=0;
function draw(){
  const interval=58;
  cards.forEach((card,i)=>{
    const angle=(i-position)*interval;
    const bounded=clamp(angle,-125,125);
    const radians=bounded*Math.PI/180;
    const x=Math.sin(radians)*radius;
    const y=(1-Math.cos(radians))*radius;
    const distance=Math.abs(angle);
    const scale=1-.1*Math.min(1,distance/80);
    card.style.transform=`translate(-50%,0) translate3d(${x.toFixed(3)}px,${y.toFixed(3)}px,0) rotate(${(bounded*.52).toFixed(3)}deg) scale(${scale.toFixed(4)})`;
    card.style.opacity=String(clamp(1-distance/150,0,1));
    card.style.zIndex=String(Math.max(1,100-Math.round(distance)));
  });
  ring.style.transform=`translateX(-50%) rotate(${(-position*interval).toFixed(3)}deg)`;
  const nearest=clamp(Math.round(position),0,cards.length-1);
  if(nearest!==selected){selected=nearest;counter.textContent=`0${nearest+1} / 0${cards.length}`;buttons.forEach((button,i)=>button.setAttribute('aria-pressed',String(i===nearest)))}
}
function tick(time){
  raf=0;
  if(!enabled||document.hidden)return;
  const dt=lastTime?Math.min((time-lastTime)/1000,.064):1/60;
  lastTime=time;
  const next=advanceDial(position,velocity,target,dt);
  position=clamp(next.position,0,cards.length-1);velocity=next.velocity;
  if(Math.abs(position-target)<.0004&&Math.abs(velocity)<.003){position=target;velocity=0;draw();lastTime=0;return}
  draw();raf=requestAnimationFrame(tick);
}
function requestTick(){if(enabled&&!raf&&!document.hidden){lastTime=0;raf=requestAnimationFrame(tick)}}
function readScroll(){
  if(!enabled)return;
  const next=clamp((scrollY+top-start)/travel,0,1)*(cards.length-1);
  if(Math.abs(next-target)<.00001)return;
  target=next;requestTick();
}
function measure(){
  if(!enabled)return;
  top=98;
  const viewport=document.documentElement.clientHeight;
  const stageHeight=Math.max(420,viewport-174);
  // Keep progress stable when the mobile address bar changes height.
  if(!viewportBasis||Math.abs(deck.clientWidth-measuredWidth)>1){viewportBasis=viewport;measuredWidth=deck.clientWidth}
  travel=(cards.length-1)*Math.max(280,viewportBasis*.55);
  radius=clamp(deck.clientWidth*.72,210,350);
  stage.style.height=`${stageHeight}px`;
  track.style.height=`${stageHeight+travel}px`;
  start=track.getBoundingClientRect().top+scrollY;
  readScroll();draw();
}
function choose(index){
  if(!enabled)return;
  const y=start-top+travel*index/(cards.length-1);
  window.scrollTo({top:y,behavior:'smooth'});
}
function enable(){
  if(enabled)return;
  enabled=true;position=0;velocity=0;target=0;selected=-1;
  track=document.createElement('div');track.className='resident-rotary-track';
  stage=document.createElement('div');stage.className='resident-dial-stage';
  deck.before(track);track.append(stage);stage.append(deck);
  ring=document.createElement('div');ring.className='resident-dial-ring';ring.setAttribute('aria-hidden','true');deck.prepend(ring);
  controls=document.createElement('div');controls.className='resident-dial-controls';
  const hint=document.createElement('p');hint.textContent='مرّر لتكتشف التفاصيل';
  counter=document.createElement('span');counter.className='resident-dial-counter';counter.dir='ltr';
  const nav=document.createElement('div');nav.className='resident-dial-buttons';nav.setAttribute('role','group');nav.setAttribute('aria-label','اختيار تفاصيل السكن');
  buttons=cards.map((card,i)=>{
    const button=document.createElement('button');button.type='button';button.textContent=`0${i+1}`;
    button.setAttribute('aria-label','عرض '+card.querySelector('h3').innerText.replace(/\s+/g,' ').trim());
    button.setAttribute('aria-pressed',String(i===0));
    button.addEventListener('click',()=>choose(i));nav.append(button);return button;
  });
  controls.append(hint,counter,nav);stage.append(controls);
  section.classList.add('has-rotary');deck.classList.add('entered');
  measure();position=target;draw();
  window.addEventListener('scroll',readScroll,{passive:true});
}
function disable(){
  if(!enabled)return;
  enabled=false;cancelAnimationFrame(raf);raf=0;lastTime=0;
  window.removeEventListener('scroll',readScroll);
  ring.remove();track.replaceWith(deck);
  section.classList.remove('has-rotary');
  cards.forEach(card=>{card.style.removeProperty('transform');card.style.removeProperty('opacity');card.style.removeProperty('z-index')});
  buttons=[];position=0;velocity=0;target=0;measuredWidth=0;viewportBasis=0;
}
function configure(){if(mobile.matches&&!reduced.matches)enable();else disable()}
mobile.addEventListener('change',configure);reduced.addEventListener('change',configure);
window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>{configure();measure()},120)},{passive:true});
window.addEventListener('load',measure);
document.fonts?.ready.then(measure);
document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(raf);raf=0;lastTime=0}else if(enabled){measure();requestTick()}});
configure();
})();
