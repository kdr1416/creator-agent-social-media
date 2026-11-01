const fs=require('fs'),path=require('path'),crypto=require('crypto'),{pathToFileURL}=require('url');
const {launch}=require('C:/Users/LENOVO/AppData/Local/npm-cache/_npx/110f701c48e68d66/node_modules/puppeteer-core');
const root=__dirname;
(async()=>{
const browser=await launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true,userDataDir:path.resolve(root,'../../../../scratch/video34-character-r3-browser')});
const items=[...['A','B','C'].map(x=>({name:'option-'+x,w:1800,h:1600})),...['A','B','C'].map(x=>({name:'scene-scale-'+x,w:1080,h:1920})),{name:'R2-vs-options',w:1800,h:940},{name:'S08-interaction-A',w:1080,h:1920}];
const results=[];
try{const page=await browser.newPage();
for(const item of items){
 const errors=[],failed=[];const fn=e=>errors.push(e.message),req=e=>failed.push(e.url());page.on('pageerror',fn);page.on('requestfailed',req);
 await page.setViewport({width:item.w,height:item.h,deviceScaleFactor:1});
 await page.goto(pathToFileURL(path.join(root,item.name+'.html')).href,{waitUntil:'networkidle0'});await page.waitForFunction(()=>window.artReady);
 const png=await page.screenshot({path:path.join(root,item.name+'.png')});
 const fresh=await page.screenshot();
 const text=await page.$$eval('text',es=>es.map(e=>({text:e.textContent,x:e.getBoundingClientRect().x,y:e.getBoundingClientRect().y,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})));
 const duplicateIds=await page.$$eval('[id]',es=>{const a=es.map(e=>e.id);return a.filter((x,i)=>a.indexOf(x)!==i)});
 const fontReady=await page.evaluate(()=>document.fonts.check('24px Display'));
 if(item.name==='S08-interaction-A')await page.screenshot({path:path.join(root,'qa/contact-detail-A.png'),clip:{x:580,y:1120,width:280,height:300}});
 if(item.w===1080){
   await page.setViewport({width:360,height:640});await page.reload({waitUntil:'networkidle0'});await page.waitForFunction(()=>window.artReady);await page.screenshot({path:path.join(root,item.name+'-mobile.png')});
 }
 results.push({name:item.name,width:item.w,height:item.h,errors,failed_requests:failed,font_ready:fontReady,text,duplicate_ids:duplicateIds,repeat_identical:crypto.createHash('sha256').update(png).digest('hex')===crypto.createHash('sha256').update(fresh).digest('hex')});page.off('pageerror',fn);page.off('requestfailed',req);
}
await page.setViewport({width:1800,height:1200});await page.goto(pathToFileURL(path.join(root,'index.html')).href,{waitUntil:'networkidle0'});
await (await page.$('.three')).screenshot({path:path.join(root,'three-directions.png')});
await page.setViewport({width:360,height:740});
results.push({gallery_mobile:{overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)}});
fs.writeFileSync(path.join(root,'qa/browser-checks.json'),JSON.stringify({browser:await browser.version(),results},null,2));console.log(JSON.stringify(results.map(x=>({name:x.name,errors:x.errors,repeat:x.repeat_identical}))));
}finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
