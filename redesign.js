(()=>{
'use strict';
document.documentElement.classList.remove('no-js');
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const menu=$('#mobile-menu'),menuButton=$('.menu-button');
function closeMenu(){menu.hidden=true;menuButton.setAttribute('aria-expanded','false');menuButton.setAttribute('aria-label','فتح القائمة')}
menuButton.addEventListener('click',()=>{const open=menu.hidden;menu.hidden=!open;menuButton.setAttribute('aria-expanded',String(open));menuButton.setAttribute('aria-label',open?'إغلاق القائمة':'فتح القائمة')});
menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!menu.hidden){closeMenu();menuButton.focus()}});
$('#year').textContent=new Date().getFullYear();
// Decode incoming photographs before swapping; a newer request always wins.
const photoRuns=new WeakMap();
async function replacePhoto(img,src,alt){const run=(photoRuns.get(img)||0)+1;photoRuns.set(img,run);const next=new Image();next.src=src;try{await next.decode()}catch{return}if(photoRuns.get(img)!==run)return;img.src=src;img.alt=alt;if(!reduced.matches)img.animate([{opacity:.3},{opacity:1}],{duration:400,easing:'ease-out'});}
const services=[['الإسكان','assets/room-red-bedding.webp','غرفة مجهزة في مساكن أسبار'],['النقل','assets/team.webp','فريق العمالة وحافلة النقل من بروفايل أسبار'],['الإعاشة','assets/kitchen.webp','المطبخ المركزي وتجهيزات الوجبات'],['إدارة المرافق','assets/facilities-management.webp','ممرات السكن مع تجهيزات السلامة ومخرج الطوارئ']];
const tabs=$$('[data-service]'),panels=$$('.service-panel');let serviceIndex=0;
function selectService(index,focus=false){serviceIndex=index;tabs.forEach((tab,i)=>{tab.classList.toggle('active',i===index);tab.setAttribute('aria-selected',String(i===index));tab.tabIndex=i===index?0:-1});panels.forEach((panel,i)=>{panel.hidden=i!==index;panel.classList.toggle('panel-enter',i===index)});replacePhoto($('#story-image'),services[index][1],services[index][2]);$('#story-type').textContent=services[index][0];$('#story-counter').textContent=`0${index+1} / 04`;if(focus)tabs[index].focus()}
tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>selectService(i));tab.addEventListener('keydown',e=>{let next=i;if(e.key==='ArrowLeft')next=(i+1)%4;else if(e.key==='ArrowRight')next=(i+3)%4;else if(e.key==='Home')next=0;else if(e.key==='End')next=3;else return;e.preventDefault();selectService(next,true)})});
const plan=$('#plan-form'),quote=$('#quote-form'),planChecks=[...plan.querySelectorAll('[name=service]')];
function updatePlan(){const selected=planChecks.filter(c=>c.checked).length;$('#plan-status').textContent=selected===0?'اختر خدمة واحدة على الأقل':selected===1?'خدمة واحدة مختارة':selected===2?'خدمتان مختارتان':`${selected} خدمات مختارة`;planChecks[0].setCustomValidity(selected?'':'اختر خدمة واحدة على الأقل')}
planChecks.forEach(c=>c.addEventListener('change',updatePlan));
$$('[data-add-service]').forEach(a=>a.addEventListener('click',()=>{planChecks[Number(a.dataset.addService)].checked=true;updatePlan()}));
plan.addEventListener('submit',e=>{e.preventDefault();updatePlan();if(!plan.reportValidity())return;const data=new FormData(plan);quote.elements.city.value=data.get('city');quote.elements.workers.value=data.get('workers');const chosen=data.getAll('service');quote.querySelectorAll('[name=service]').forEach(c=>c.checked=chosen.includes(c.value));$('#plan-recap').textContent=`${data.get('workers')} فرد · ${data.get('city')} · ${chosen.join('، ')}`;$('#plan-recap').hidden=false;$('#contact').scrollIntoView({behavior:reduced.matches?'instant':'smooth',block:'start'});quote.elements.name.focus({preventScroll:true})});
quote.addEventListener('input',e=>{if(!['city','workers','service'].includes(e.target.name)||$('#plan-recap').hidden)return;const data=new FormData(quote);$('#plan-recap').textContent=`${data.get('workers')||'—'} فرد · ${data.get('city')||'الموقع'} · ${data.getAll('service').join('، ')||'اختر الخدمات'}`});
quote.addEventListener('submit',e=>{e.preventDefault();const data=new FormData(quote);const selected=data.getAll('service'),note=$('#form-note');if(!selected.length){note.textContent='اختر خدمة واحدة على الأقل.';quote.querySelector('[name=service]').focus();return}const message=['مرحبًا فريق مساكن أسبار، أرغب في عرض سعر.',`الاسم: ${data.get('name')}`,`الشركة: ${data.get('company')}`,`المدينة / موقع العمل: ${data.get('city')}`,`عدد العمالة: ${data.get('workers')}`,`الخدمات المطلوبة: ${selected.join('، ')}`,data.get('notes')?`تفاصيل إضافية: ${data.get('notes')}`:''].filter(Boolean).join('\n');const url='https://wa.me/966500558677?text='+encodeURIComponent(message);window.open(url,'_blank','noopener,noreferrer');note.replaceChildren(document.createTextNode('راجع طلبك في واتساب. '));const fallback=document.createElement('a');fallback.href=url;fallback.target='_blank';fallback.rel='noopener';fallback.textContent='افتح الرسالة هنا';note.append(fallback)});
// Five stops in the everyday life tour; controls never move the page.
const photos=[
{file:'assets/room-red-bedding.webp',alt:'غرفة سكن مجهزة بأسرّة وخزائن في مساكن أسبار',kicker:'غرف السكن',title:'هنا، ينتهي التعب.',copy:'أسرّة مجهّزة وخزائن للأغراض. مساحة مرتّبة للراحة بعد يوم العمل.'},
{file:'assets/kitchen.webp',alt:'المطبخ المركزي وتجهيزات إعداد الوجبات',kicker:'المطبخ المركزي',title:'العناية، تبدأ من هنا.',copy:'مطبخ مركزي وتجهيزات لإعداد الوجبات. تفاصيل تدعم يوم فريقك.'},
{file:'assets/lounge.webp',alt:'منطقة غسيل مشتركة مجهزة بغسالات وطاولات',kicker:'مناطق الغسيل',title:'ليوم أخفّ. وملابس أنظف.',copy:'منطقة مشتركة للغسيل، مجهّزة لتسهيل العناية بالملابس ضمن روتينهم اليومي.'},
{file:'assets/private-bathroom.webp',alt:'صورة توضيحية مولّدة لحمّام خاص بغرفة السكن',kicker:'دورات المياه',title:'خصوصية، تكمّل الراحة.',copy:'حمّام خاص لكل غرفة. لأن الراحة تبدأ من تلبية الاحتياجات اليومية.'},
{file:'assets/facilities-management.webp',alt:'ممرات مساكن أسبار مع تجهيزات السلامة ومخرج الطوارئ',kicker:'المرافق والممرات',title:'خلف الراحة، عناية مستمرة.',copy:'ممرات منظّمة، ونظافة وصيانة ومتابعة تحافظ على جاهزية المكان.'}];
let currentPhoto=0;
const galleryButtons=$$('[data-photo]'),galleryImage=$('#gallery-image'),galleryZoom=$('.life-zoom');
function selectPhoto(i,focus=false){
  currentPhoto=(i+photos.length)%photos.length;
  const p=photos[currentPhoto],number=String(currentPhoto+1).padStart(2,'0');
  replacePhoto(galleryImage,p.file,p.alt);
  $('#gallery-kicker').textContent=p.kicker;
  $('#gallery-title').textContent=p.title;
  $('#gallery-copy').textContent=p.copy;
  $('#life-number').textContent=number;
  $('#gallery-count').innerHTML=number+' <span>/ 05</span>';
  $('#gallery-count').setAttribute('aria-label',`المحطة ${currentPhoto+1} من ${photos.length}`);
  $('.life-progress').style.setProperty('--life-progress',`${(currentPhoto+1)/photos.length*100}%`);
  galleryZoom.setAttribute('aria-label','تكبير صورة '+p.kicker);
  galleryButtons.forEach((button,j)=>{button.classList.toggle('active',j===currentPhoto);button.setAttribute('aria-pressed',String(j===currentPhoto))});
  if(focus)galleryButtons[currentPhoto].focus();
}
galleryButtons.forEach((button,i)=>{
  button.addEventListener('click',()=>selectPhoto(i));
  button.addEventListener('keydown',e=>{
    let next=i;
    if(e.key==='ArrowDown'||e.key==='ArrowLeft')next=i+1;
    else if(e.key==='ArrowUp'||e.key==='ArrowRight')next=i-1;
    else if(e.key==='Home')next=0;
    else if(e.key==='End')next=photos.length-1;
    else return;
    e.preventDefault();selectPhoto(next,true);
  });
});
$('[data-gallery-prev]').addEventListener('click',()=>selectPhoto(currentPhoto-1));
$('[data-gallery-next]').addEventListener('click',()=>selectPhoto(currentPhoto+1));
const dialog=$('.photo-dialog');
galleryZoom.addEventListener('click',()=>{const p=photos[currentPhoto];$('#dialog-image').src=p.file;$('#dialog-image').alt=p.alt;$('#dialog-caption').textContent=p.kicker;dialog.showModal()});
$('.dialog-close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target!==dialog)return;const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()});
// Animate once on entry; no motion is required to read the content.
let observer;
const revealTargets=$$('.plan-section,.services-heading,.service-tabs,.service-showcase,.about-copy,.about-visual,.resident-heading,.resident-deck,.resident-actions,.section-heading,.life-heading,.life-layout,.care-intro,.care-points>div,.journey-steps li,.faq-list,.quote-form');
if('IntersectionObserver' in window&&!reduced.matches){document.documentElement.classList.add('motion-ready');observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('entered','in-view');observer.unobserve(entry.target)}}),{threshold:.08});revealTargets.forEach((el,i)=>{el.setAttribute('data-enter','');if(el.matches('.journey-steps li,.care-points>div'))el.style.setProperty('--delay',`${i%4*70}ms`);observer.observe(el)})}
reduced.addEventListener('change',()=>{if(reduced.matches){document.documentElement.classList.remove('motion-ready');observer?.disconnect();revealTargets.forEach(el=>el.classList.add('entered'))}});
const links=$$('.header nav a');const sections=links.map(a=>$(a.getAttribute('href')));let ticking=false;
function updateScroll(){ticking=false;const total=document.documentElement.scrollHeight-innerHeight;document.documentElement.style.setProperty('--scroll-progress',total>0?Math.min(1,scrollY/total):0);$('.header').classList.toggle('scrolled',scrollY>20);let active=-1;sections.forEach((s,i)=>{const r=s.getBoundingClientRect();if(r.top<=180&&r.bottom>180)active=i});links.forEach((a,i)=>{a.classList.toggle('current',i===active);if(i===active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})}
function schedule(){if(!ticking){ticking=true;requestAnimationFrame(updateScroll)}}window.addEventListener('scroll',schedule,{passive:true});window.addEventListener('resize',schedule,{passive:true});updateScroll();
})();
