(()=>{const menu=document.querySelector('.menu-toggle');const nav=document.querySelector('.site-nav');if(menu&&nav){menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close menu':'Open menu')});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}))}document.querySelectorAll('[data-year]').forEach(e=>e.textContent=String(new Date().getFullYear()));})();
/* Play documentary clips only when visible; respect reduced-motion settings. */
(()=>{const clips=[...document.querySelectorAll('video.source-video')];if(!clips.length||window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;if(!('IntersectionObserver' in window))return;const observer=new IntersectionObserver(entries=>{entries.forEach(({target,isIntersecting})=>{if(isIntersecting){const p=target.play();if(p&&typeof p.catch==='function')p.catch(()=>{})}else{target.pause()}})},{threshold:0.45});clips.forEach(video=>observer.observe(video))})();

/* True documentary video backgrounds: play while visible, pause offscreen,
   respect reduced motion and data-saving settings. */
(()=>{
  const clips=[...document.querySelectorAll("video.geofrontier-bg-video")];
  if(!clips.length)return;
  const reduced=window.matchMedia("(prefers-reduced-motion: reduce)");
  const constrained=Boolean(navigator.connection&&navigator.connection.saveData);
  const pauseAll=()=>clips.forEach(video=>video.pause());
  if(reduced.matches||constrained){pauseAll();return;}
  const playSafely=(video)=>{
    if(document.hidden)return;
    video.muted=true;
    const promise=video.play();
    if(promise&&typeof promise.catch==="function")promise.catch(()=>{});
  };
  if("IntersectionObserver" in window){
    const observer=new IntersectionObserver(entries=>{
      entries.forEach(({target,isIntersecting})=>{
        if(isIntersecting&&!document.hidden)playSafely(target);
        else target.pause();
      });
    },{threshold:0.12,rootMargin:"100px 0px 100px 0px"});
    clips.forEach(video=>observer.observe(video));
  }else{clips.slice(0,1).forEach(playSafely);}
  document.addEventListener("visibilitychange",()=>{
    if(document.hidden)pauseAll();
    else clips.forEach(video=>{
      const rect=video.getBoundingClientRect();
      if(rect.bottom>0&&rect.top<window.innerHeight)playSafely(video);
    });
  });
  if(typeof reduced.addEventListener==="function"){
    reduced.addEventListener("change",event=>{if(event.matches)pauseAll()});
  }
})();

/* Draft-only client enquiry helper: local clipboard action, no data submission. */
(()=>{
 const button=document.querySelector("[data-copy-enquiry]");
 const status=document.querySelector("[data-copy-enquiry-status]");
 if(!button||!status)return;
 const brief=[
  "Hello, I would like to discuss a possible GeoFrontier Analytics project.",
  "",
  "Organisation / role: ",
  "Area of interest (general location only): ",
  "Decision or problem to address: ",
  "Existing data or official information: ",
  "Type of support: climate evidence / InSAR screening / flood map / GIS / GNSS / training / other",
  "Desired output and approximate timeframe: ",
  "",
  "I can share additional technical details after we agree a suitable private channel."
 ].join("\n");
 button.addEventListener("click",async()=>{
   try{
     if(navigator.clipboard&&window.isSecureContext)await navigator.clipboard.writeText(brief);
     else{
       const el=document.createElement("textarea");
       el.value=brief;el.style.cssText="position:fixed;left:-9999px;top:-9999px";
       document.body.appendChild(el);el.select();
       if(!document.execCommand("copy"))throw new Error("Clipboard access unavailable");
       el.remove();
     }
     status.textContent="Enquiry outline copied. Edit it before sending through LinkedIn.";
   }catch(e){status.textContent="Copy is unavailable in this browser. Please use the four-question brief below.";}
 });
})();
