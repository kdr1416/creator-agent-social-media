const fs=require('fs'),path=require('path'),crypto=require('crypto'),{pathToFileURL}=require('url');
const puppeteer=require('C:/Users/LENOVO/AppData/Local/npm-cache/_npx/110f701c48e68d66/node_modules/puppeteer-core');
const root=__dirname;
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
(async()=>{
 const browser=await puppeteer.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true,userDataDir:path.resolve(root,'../../../../scratch/video34-core-r2-browser')});
 const frames=JSON.parse(fs.readFileSync(path.join(root,'frames.json'),'utf8')),results=[];
 try{
  const page=await browser.newPage();
  for(const item of frames){
   const errors=[],failed=[];const err=e=>errors.push(e.message),fail=r=>failed.push(r.url());
   page.on('pageerror',err);page.on('requestfailed',fail);
   await page.setViewport({width:1080,height:1920,deviceScaleFactor:1});
   await page.goto(pathToFileURL(path.join(root,item.id+'.html')).href,{waitUntil:'networkidle0'});
   await page.waitForFunction(()=>window.keyframeReady);
   const png=await page.screenshot({path:path.join(root,item.id+'.png')});
   const info=await page.evaluate(()=>({fonts:[document.fonts.check('72px Display'),document.fonts.check('72px Editorial')],text:[...document.querySelectorAll('text')].map(e=>{const b=e.getBBox(),r=e.getBoundingClientRect();return {text:e.textContent,bbox:{x:b.x,y:b.y,width:b.width,height:b.height},screen:{x:r.x,y:r.y,width:r.width,height:r.height},font:getComputedStyle(e).fontFamily}}),svgIds:[...document.querySelectorAll('svg [id]')].map(x=>x.id),width:innerWidth,height:innerHeight}));
   await page.evaluate(id=>{const t=window.__timelines[id];t.seek(0);t.seek(3);t.seek(0)},item.id);
   const repeated=await page.screenshot();
   await page.reload({waitUntil:'networkidle0'});await page.waitForFunction(()=>window.keyframeReady);
   const fresh=await page.screenshot();
   await page.setViewport({width:360,height:640,deviceScaleFactor:1});
   await page.reload({waitUntil:'networkidle0'});await page.waitForFunction(()=>window.keyframeReady);
   await page.screenshot({path:path.join(root,item.id+'-mobile.png')});
   results.push({id:item.id,...info,errors,failed,png_sha256:hash(png),repeat_identical:hash(png)===hash(repeated),fresh_identical:hash(png)===hash(fresh),duplicate_ids:info.svgIds.filter((x,i,a)=>a.indexOf(x)!==i)});
   page.off('pageerror',err);page.off('requestfailed',fail);
  }
  await page.setViewport({width:1440,height:1220,deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(root,'index.html')).href,{waitUntil:'networkidle0'});
  await page.screenshot({path:path.join(root,'comparison.png'),fullPage:true});
  results.push({gallery:{viewport:[1440,1220],overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)}});
  await page.setViewport({width:360,height:740});
  results.push({gallery_mobile:{overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)}});
  fs.writeFileSync(path.join(root,'qa/browser-checks.json'),JSON.stringify({browser:await browser.version(),capture:'Existing Puppeteer + headless Chrome; SVG/HTML; no video render',results},null,2));
  console.log(JSON.stringify(results.map(x=>x.id?{id:x.id,errors:x.errors,failed:x.failed,fonts:x.fonts,repeat:x.repeat_identical,fresh:x.fresh_identical,duplicate_ids:x.duplicate_ids}:x)));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
