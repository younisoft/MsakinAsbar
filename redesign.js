(()=>{
'use strict';
document.documentElement.classList.remove('no-js');
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
// One script for both languages: English pages set <html lang="en" dir="ltr">.
const EN=document.documentElement.lang==='en',LTR=document.documentElement.dir==='ltr',t=(ar,en)=>EN?en:ar;
const menu=$('#mobile-menu'),menuButton=$('.menu-button');
function closeMenu(){menu.hidden=true;menuButton.setAttribute('aria-expanded','false');menuButton.setAttribute('aria-label',t('فتح القائمة','Open menu'))}
menuButton.addEventListener('click',()=>{const open=menu.hidden;menu.hidden=!open;menuButton.setAttribute('aria-expanded',String(open));menuButton.setAttribute('aria-label',open?t('إغلاق القائمة','Close menu'):t('فتح القائمة','Open menu'))});
menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!menu.hidden){closeMenu();menuButton.focus()}});
$('#year').textContent=new Date().getFullYear();
// Decode incoming photographs before swapping; a newer request always wins.
const photoRuns=new WeakMap();
async function replacePhoto(img,src,alt){const run=(photoRuns.get(img)||0)+1;photoRuns.set(img,run);const next=new Image();next.src=src;try{await next.decode()}catch{return}if(photoRuns.get(img)!==run)return;img.src=src;img.alt=alt;if(!reduced.matches)img.animate([{opacity:.3},{opacity:1}],{duration:400,easing:'ease-out'});}
const A=EN?'../assets/':'assets/';
const services=EN?[['Accommodation',A+'room-red-bedding.webp','A furnished room at Aspar Residences'],['Transport',A+'team.webp','Workers and an Aspar Residences transport bus'],['Catering',A+'kitchen.webp','The central kitchen and meal preparation equipment'],['Facilities management',A+'facilities-management.webp','Residence corridor with safety equipment and an emergency exit']]:[['الإسكان',A+'room-red-bedding.webp','غرفة مجهزة في مساكن أسبار'],['النقل',A+'team.webp','فريق العمالة وحافلة النقل من بروفايل أسبار'],['الإعاشة',A+'kitchen.webp','المطبخ المركزي وتجهيزات الوجبات'],['إدارة المرافق',A+'facilities-management.webp','ممرات السكن مع تجهيزات السلامة ومخرج الطوارئ']];
const tabs=$$('[data-service]'),panels=$$('.service-panel');let serviceIndex=0;
function selectService(index,focus=false){serviceIndex=index;tabs.forEach((tab,i)=>{tab.classList.toggle('active',i===index);tab.setAttribute('aria-selected',String(i===index));tab.tabIndex=i===index?0:-1});panels.forEach((panel,i)=>{panel.hidden=i!==index;panel.classList.toggle('panel-enter',i===index)});replacePhoto($('#story-image'),services[index][1],services[index][2]);$('#story-type').textContent=services[index][0];$('#story-counter').textContent=`0${index+1} / 04`;if(focus)tabs[index].focus()}
tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>selectService(i));tab.addEventListener('keydown',e=>{let next=i;const fwd=LTR?'ArrowRight':'ArrowLeft',back=LTR?'ArrowLeft':'ArrowRight';if(e.key===fwd)next=(i+1)%4;else if(e.key===back)next=(i+3)%4;else if(e.key==='Home')next=0;else if(e.key==='End')next=3;else return;e.preventDefault();selectService(next,true)})});
const plan=$('#plan-form'),quote=$('#quote-form'),planChecks=[...plan.querySelectorAll('[name=service]')];
function updatePlan(){const selected=planChecks.filter(c=>c.checked).length;$('#plan-status').textContent=EN?(selected===0?'Choose at least one service':selected===1?'1 service selected':`${selected} services selected`):(selected===0?'اختر خدمة واحدة على الأقل':selected===1?'خدمة واحدة مختارة':selected===2?'خدمتان مختارتان':`${selected} خدمات مختارة`);planChecks[0].setCustomValidity(selected?'':t('اختر خدمة واحدة على الأقل','Choose at least one service'))}
planChecks.forEach(c=>c.addEventListener('change',updatePlan));
$$('[data-add-service]').forEach(a=>a.addEventListener('click',()=>{planChecks[Number(a.dataset.addService)].checked=true;updatePlan()}));
plan.addEventListener('submit',e=>{e.preventDefault();updatePlan();if(!plan.reportValidity())return;const data=new FormData(plan);quote.elements.city.value=data.get('city');quote.elements.workers.value=data.get('workers');const chosen=data.getAll('service');quote.querySelectorAll('[name=service]').forEach(c=>c.checked=chosen.includes(c.value));$('#plan-recap').textContent=`${data.get('workers')} ${t('فرد','people')} · ${data.get('city')} · ${chosen.join(t('، ',', '))}`;$('#plan-recap').hidden=false;$('#contact').scrollIntoView({behavior:reduced.matches?'instant':'smooth',block:'start'});quote.elements.name.focus({preventScroll:true})});
quote.addEventListener('input',e=>{if(!['city','workers','service'].includes(e.target.name)||$('#plan-recap').hidden)return;const data=new FormData(quote);$('#plan-recap').textContent=`${data.get('workers')||'—'} ${t('فرد','people')} · ${data.get('city')||t('الموقع','Location')} · ${data.getAll('service').join(t('، ',', '))||t('اختر الخدمات','Choose services')}`});
quote.addEventListener('submit',e=>{e.preventDefault();const data=new FormData(quote);const selected=data.getAll('service'),note=$('#form-note');if(!selected.length){note.textContent=t('اختر خدمة واحدة على الأقل.','Choose at least one service.');quote.querySelector('[name=service]').focus();return}const message=(EN?['Hello Aspar Residences team, I would like a quote.',`Name: ${data.get('name')}`,`Company: ${data.get('company')}`,`City / work site: ${data.get('city')}`,`Number of workers: ${data.get('workers')}`,`Services needed: ${selected.join(', ')}`,data.get('notes')?`Additional details: ${data.get('notes')}`:'']:['مرحبًا فريق مساكن أسبار، أرغب في عرض سعر.',`الاسم: ${data.get('name')}`,`الشركة: ${data.get('company')}`,`المدينة / موقع العمل: ${data.get('city')}`,`عدد العمالة: ${data.get('workers')}`,`الخدمات المطلوبة: ${selected.join('، ')}`,data.get('notes')?`تفاصيل إضافية: ${data.get('notes')}`:'']).filter(Boolean).join('\n');const url='https://wa.me/966500558677?text='+encodeURIComponent(message);window.open(url,'_blank','noopener,noreferrer');note.replaceChildren(document.createTextNode(t('راجع طلبك في واتساب. ','Review your request in WhatsApp. ')));const fallback=document.createElement('a');fallback.href=url;fallback.target='_blank';fallback.rel='noopener';fallback.textContent=t('افتح الرسالة هنا','Open the message here');note.append(fallback)});
// Five stops in the everyday life tour; controls never move the page.
const photosAr=[
{file:A+'room-red-bedding.webp',alt:'غرفة سكن مجهزة بأسرّة وخزائن في مساكن أسبار',kicker:'غرف السكن',title:'هنا، ينتهي التعب.',copy:'أسرّة مجهّزة وخزائن للأغراض. مساحة مرتّبة للراحة بعد يوم العمل.'},
{file:A+'kitchen.webp',alt:'المطبخ المركزي وتجهيزات إعداد الوجبات',kicker:'المطبخ المركزي',title:'العناية، تبدأ من هنا.',copy:'مطبخ مركزي وتجهيزات لإعداد الوجبات. تفاصيل تدعم يوم فريقك.'},
{file:A+'lounge.webp',alt:'منطقة غسيل مشتركة مجهزة بغسالات وطاولات',kicker:'مناطق الغسيل',title:'ليوم أخفّ. وملابس أنظف.',copy:'منطقة مشتركة للغسيل، مجهّزة لتسهيل العناية بالملابس ضمن روتينهم اليومي.'},
{file:A+'private-bathroom.webp',alt:'صورة توضيحية مولّدة لحمّام خاص بغرفة السكن',kicker:'دورات المياه',title:'خصوصية، تكمّل الراحة.',copy:'حمّام خاص لكل غرفة. لأن الراحة تبدأ من تلبية الاحتياجات اليومية.'},
{file:A+'facilities-management.webp',alt:'ممرات مساكن أسبار مع تجهيزات السلامة ومخرج الطوارئ',kicker:'المرافق والممرات',title:'خلف الراحة، عناية مستمرة.',copy:'ممرات منظّمة، ونظافة وصيانة ومتابعة تحافظ على جاهزية المكان.'}];
const photosEn=[
{file:A+'room-red-bedding.webp',alt:'Residence room with bunk beds and lockers at Aspar Residences',kicker:'Residence rooms',title:'This is where the day’s fatigue ends.',copy:'Made-up beds and lockers for personal belongings. An orderly space to rest after work.'},
{file:A+'kitchen.webp',alt:'The central kitchen and meal preparation equipment',kicker:'Central kitchen',title:'Care starts here.',copy:'A central kitchen equipped for meal preparation. Details that support your team’s day.'},
{file:A+'lounge.webp',alt:'Shared laundry area with washing machines and tables',kicker:'Laundry areas',title:'A lighter day. Cleaner clothes.',copy:'A shared laundry area that makes caring for clothes part of an easy daily routine.'},
{file:A+'private-bathroom.webp',alt:'Illustrative generated image of a private room bathroom',kicker:'Bathrooms',title:'Privacy completes comfort.',copy:'A private bathroom for each room, because comfort starts with everyday needs.'},
{file:A+'facilities-management.webp',alt:'Aspar Residences corridors with safety equipment and an emergency exit',kicker:'Facilities and corridors',title:'Behind the comfort, constant care.',copy:'Orderly corridors, with cleaning, maintenance and follow-up that keep the place ready.'}];
const photos=EN?photosEn:photosAr;
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
  $('#gallery-count').setAttribute('aria-label',EN?`Stop ${currentPhoto+1} of ${photos.length}`:`المحطة ${currentPhoto+1} من ${photos.length}`);
  $('.life-progress').style.setProperty('--life-progress',`${(currentPhoto+1)/photos.length*100}%`);
  galleryZoom.setAttribute('aria-label',t('تكبير صورة ','Enlarge photo: ')+p.kicker);
  galleryButtons.forEach((button,j)=>{button.classList.toggle('active',j===currentPhoto);button.setAttribute('aria-pressed',String(j===currentPhoto))});
  if(focus)galleryButtons[currentPhoto].focus();
}
galleryButtons.forEach((button,i)=>{
  button.addEventListener('click',()=>selectPhoto(i));
  button.addEventListener('keydown',e=>{
    let next=i;
    if(e.key==='ArrowDown'||e.key===(LTR?'ArrowRight':'ArrowLeft'))next=i+1;
    else if(e.key==='ArrowUp'||e.key===(LTR?'ArrowLeft':'ArrowRight'))next=i-1;
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
