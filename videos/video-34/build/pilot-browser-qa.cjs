// Read-only browser inspection, apart from screenshots/evidence under build/pilot-evidence.
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),crypto=require('node:crypto');
const puppeteer=require('C:/Users/LENOVO/AppData/Local/npm-cache/_npx/110f701c48e68d66/node_modules/puppeteer-core');
const PORT=Number(process.env.QA_PORT||8854);
const project=path.resolve(__dirname,'..'),ev=path.join(__dirname,'pilot-evidence');
const types={'.html':'text/html; charset=utf-8','.js':'application/javascript','.json':'application/json','.svg':'image/svg+xml','.wav':'audio/wav','.mp4':'video/mp4','.png':'image/png'};
const server=http.createServer((req,res)=>{
 const f=path.resolve(project,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
 if(!f.startsWith(project+path.sep)||!fs.existsSync(f)||!fs.statSync(f).isFile()){res.writeHead(404).end();return;}
 const n=fs.statSync(f).size;res.setHeader('Content-Type',types[path.extname(f)]||'application/octet-stream');
 if(req.headers.range){let [a,b]=req.headers.range.replace('bytes=','').split('-').map(Number);b=b||n-1;b=Math.min(b,n-1);res.writeHead(206,{'Accept-Ranges':'bytes','Content-Range':`bytes ${a}-${b}/${n}`,'Content-Length':b-a+1});fs.createReadStream(f,{start:a,end:b}).pipe(res);}
 else{res.setHeader('Content-Length',n);fs.createReadStream(f).pipe(res);}
});
const delay=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 console.log('QA: starting local evidence server');
 await new Promise(r=>server.listen(PORT,'127.0.0.1',r));
 console.log('QA: server listening; launching Chrome');
 const browser=await puppeteer.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true,userDataDir:path.join(__dirname,'pilot-browser-qa-profile-'+PORT),args:['--autoplay-policy=no-user-gesture-required']});
 const result={browser:await browser.version(),scenes:{},review:{}};
 console.log('QA: Chrome ready');
 try{
  for(const id of ['S03','S08']){
   const page=await browser.newPage();await page.setViewport({width:720,height:1280});const errors=[],failed=[];
   page.on('pageerror',e=>errors.push(e.message));page.on('console',e=>{if(e.type()==='error')errors.push(e.text());});page.on('response',r=>{if(r.status()>=400)failed.push([r.status(),r.url()]);});page.on('requestfailed',r=>failed.push([r.failure()?.errorText,r.url()]));
   await page.goto(`http://127.0.0.1:${PORT}/scenes/${id}/index.html`,{waitUntil:'networkidle0'});
   console.log('QA: loaded',id);
   const times=id==='S03'?[0,1.25,2.8,3.8,4.2,5.3,7.8,8.9]:[0,1.4,2.6,3.8,4.9,5.56];
   const samples=[];
   for(const t of times){
    await page.evaluate((id,t)=>{window.__timelines[id].seek(t,false);},id,t);await delay(50);
    await page.screenshot({path:path.join(ev,`${id}-${t.toFixed(2)}.png`)});
    samples.push(await page.evaluate(t=>({t,overflow:document.documentElement.scrollWidth>innerWidth,idsUnique:new Set([...document.querySelectorAll('[id]')].map(x=>x.id)).size===document.querySelectorAll('[id]').length,svgLoaded:!!document.querySelector('svg path'),vietnameseFontLoaded:document.fonts.check('80px Display')&&document.fonts.check('80px Editorial'),visibleHighlights:[...document.querySelectorAll('.highlight')].filter(e=>Number(getComputedStyle(e).opacity)>.9).map(e=>({text:e.textContent,box:e.getBoundingClientRect().toJSON()}))}),t));
   }
   const mid=id==='S03'?3.8:3.8;
   const capture=async t=>{await page.evaluate((id,t)=>{window.__timelines[id].seek(t,false);},id,t);await delay(50);return crypto.createHash('sha256').update(await page.screenshot()).digest('hex');};
   const forward=await capture(mid);await capture(0);await capture(times.at(-1));const backward=await capture(mid);
   let contact=null;
   if(id==='S08'){
    await page.evaluate(()=>{window.__timelines.S08.seek(5.4,false);});
    contact=await page.evaluate(()=>{
     const b=document.querySelector('#child-hand').getBBox(),m=document.querySelector('#child-hand').getCTM();const p=new DOMPoint(b.x+b.width/2,b.y+b.height/2).matrixTransform(m);
     const a=document.querySelector('#parent-near-arm'),q=new DOMPoint(418,872).matrixTransform(a.getCTM());
     return {childHandCenter:{x:p.x,y:p.y},parentWrist:{x:q.x,y:q.y},distance:Math.hypot(p.x-q.x,p.y-q.y),nearArmD:a.getAttribute('d'),lidTransform:document.querySelector('#laptop-position').getAttribute('transform')};
    });
   }
   await page.setViewport({width:360,height:640});await page.screenshot({path:path.join(ev,`${id}-mobile.png`)});
   result.scenes[id]={samples,seekPixelHashes:{forward,backward,equal:forward===backward},contact,errors,failed};await page.close();
  }
  if(!process.argv.includes('--source-only')){
   for(const width of [360,768,1280]){
    const page=await browser.newPage();await page.setViewport({width,height:900});let errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('console',e=>{if(e.type()==='error')errors.push(e.text());});
    await page.goto(`http://127.0.0.1:${PORT}/REVIEW.html`,{waitUntil:'networkidle0'});
    await page.waitForFunction(()=>[...document.querySelectorAll('video')].length===2&&[...document.querySelectorAll('video')].every(v=>v.readyState>=2));
    const playback=[];
    for(const id of ['S03','S08']){
     await page.evaluate(async id=>{const v=document.querySelector(`#video-${id}`);v.muted=true;await v.play();},id);await delay(650);
     playback.push(await page.evaluate(id=>{const v=document.querySelector(`#video-${id}`);const r={id,time:v.currentTime,duration:v.duration,width:v.videoWidth,height:v.videoHeight,playing:!v.paused,error:v.error?.message||null,dropped:v.getVideoPlaybackQuality?.().droppedVideoFrames};v.pause();return r;},id));
    }
    const completePlayback=[];
    if(width===1280){
     for(const id of ['S03','S08']){
      completePlayback.push(await page.evaluate(async id=>{
       const v=document.querySelector(`#video-${id}`);v.currentTime=0;v.muted=true;
       const ended=new Promise((resolve,reject)=>{v.addEventListener('ended',()=>resolve(true),{once:true});setTimeout(()=>reject(new Error('full playback timed out')),15000);});
       await v.play();await ended;return {id,ended:v.ended,time:v.currentTime,duration:v.duration,error:v.error?.message||null,quality:v.getVideoPlaybackQuality?.()};
      },id));
     }
    }
    result.review[width]={overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),playback,completePlayback,errors};
    await page.screenshot({path:path.join(ev,`REVIEW-${width}.png`),fullPage:true});await page.close();
   }
  }
 }finally{fs.writeFileSync(path.join(ev,process.argv.includes('--source-only')?'browser-source.json':'browser-final.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
