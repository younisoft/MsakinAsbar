(()=>{
 const reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)');
 const switches=[...document.querySelectorAll('[data-service]')];
 const chapters=[...document.querySelectorAll('[data-chapter]')];
 const stage=document.querySelector('.story-stage');
 const image=document.querySelector('#story-image');
 const labels=['الإسكان','النقل','الإعاشة','إدارة المرافق'];
 const images=[['assets/room.jpg','غرفة مجهّزة في مساكن أسبار'],['assets/team.jpg','صورة من بروفايل أسبار لفريق العمالة مع حافلة'],['assets/kitchen.jpg','المطبخ المركزي وتجهيزات إعداد الوجبات'],['assets/facilities-management.png','ممرات مساكن أسبار مع تجهيزات السلامة ومخرج الطوارئ']];
 let current=-1,manualUntil=0,frame=0;
 function activate(index){
  if(index===current)return;current=index;
  switches.forEach((button,i)=>{button.classList.toggle('active',i===index);button.setAttribute('aria-pressed',String(i===index))});
  chapters.forEach((chapter,i)=>chapter.classList.toggle('current',i===index));
  image.src=images[index][0];image.alt=images[index][1];
  document.querySelector('#story-type').textContent=labels[index];document.querySelector('#story-counter').textContent=`0${index+1} / 04`;
  stage.style.setProperty('--chapter-index',index);
 }
 switches.forEach((button,index)=>button.addEventListener('click',()=>{
  activate(index);manualUntil=performance.now()+1100;
  const offset=innerWidth<=760?stage.offsetHeight+96:120;
  window.scrollTo({top:Math.max(0,chapters[index].getBoundingClientRect().top+scrollY-offset),behavior:reducedMotion.matches?'instant':'smooth'});
 }));
 activate(0);
 // Reveal whole Arabic words, preserving shaping within each word and existing line breaks.
 if('IntersectionObserver' in window&&!reducedMotion.matches){
  const headings=[...document.querySelectorAll('.section h2,.care-band h2')];
  headings.forEach(heading=>{
   const walker=document.createTreeWalker(heading,NodeFilter.SHOW_TEXT);const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);
   let index=0;nodes.forEach(node=>{const fragment=document.createDocumentFragment();node.textContent.split(/(\s+)/).forEach(word=>{if(!word.trim()){fragment.append(document.createTextNode(word));return}const span=document.createElement('span');span.className='headline-word';span.style.setProperty('--word-index',index++);span.textContent=word;fragment.append(span)});node.replaceWith(fragment)});heading.classList.add('word-reveal');
  });
  const reveal=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');reveal.unobserve(entry.target)}}),{threshold:.12});headings.forEach(h=>reveal.observe(h));
 }
 const header=document.querySelector('.header');const hero=document.querySelector('.hero');const gallery=document.querySelector('.gallery');
 const rails=[...document.querySelectorAll('.chapter-rail a')];const navigation=[...document.querySelectorAll('.header nav a')];
 const sections=rails.map(a=>document.querySelector(a.getAttribute('href')));
 const steps=[...document.querySelectorAll('.journey-steps li')];
 function update(){
  frame=0;const height=innerHeight;const total=document.documentElement.scrollHeight-height;const y=scrollY;
  document.documentElement.style.setProperty('--scroll-progress',total>0?Math.min(1,y/total):0);
  header.classList.toggle('scrolled',y>20);
  if(!reducedMotion.matches&&innerWidth>760){
   document.documentElement.style.setProperty('--hero-depth',Math.min(48,Math.max(0,y*.07))+'px');
   const r=gallery.getBoundingClientRect();if(r.bottom>0&&r.top<height)gallery.style.setProperty('--gallery-depth',Math.max(-18,Math.min(18,(height*.5-r.top)*.045))+'px');
  }
  const stageRect=stage.getBoundingClientRect();
  if(performance.now()>manualUntil&&stageRect.top<height&&document.querySelector('.service-story').getBoundingClientRect().bottom>120){
   const focus=innerWidth<=760?stageRect.bottom+(height-stageRect.bottom)*.45:height*.53;
   let closest=0,distance=Infinity;chapters.forEach((chapter,i)=>{const r=chapter.getBoundingClientRect();const d=Math.abs((r.top+r.bottom)/2-focus);if(d<distance){closest=i;distance=d}});activate(closest);
  }
  let sectionIndex=0;sections.forEach((section,i)=>{if(section.getBoundingClientRect().top<height*.42)sectionIndex=i});
  rails.forEach((a,i)=>{a.classList.toggle('active',i===sectionIndex);if(i===sectionIndex)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')});
  navigation.forEach(a=>a.classList.toggle('current',a.getAttribute('href')===rails[sectionIndex].getAttribute('href')));
  steps.forEach(step=>{const r=step.getBoundingClientRect();if(r.top<height*.8)step.classList.add('in-view')});
 }
 function schedule(){if(!frame)frame=requestAnimationFrame(update)}
 window.addEventListener('scroll',schedule,{passive:true});window.addEventListener('resize',schedule,{passive:true});window.addEventListener('load',schedule);reducedMotion.addEventListener('change',()=>{document.documentElement.style.setProperty('--hero-depth','0px');gallery.style.setProperty('--gallery-depth','0px');document.querySelectorAll('.word-reveal').forEach(h=>h.classList.add('visible'));schedule()});update();
})();
