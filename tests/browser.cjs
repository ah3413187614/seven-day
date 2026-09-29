// Run only when a browser is provisioned. Never install a browser from this script.
const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const root=path.resolve(__dirname,'..'),matrix=[[1920,1080],[1440,900],[1366,768],[430,932],[390,844],[375,667],[320,568]];
(async()=>{
 let browser;
 try{browser=await require('playwright').chromium.launch({headless:true,args:['--no-sandbox']});}
 catch(e){fs.writeFileSync(path.join(__dirname,'browser-report-v04.json'),JSON.stringify({passed:false,status:'blocked',reason:String(e).split('\n').slice(0,5).join('\n'),viewports:matrix.map(([width,height])=>({width,height,status:'not_run'})),checksNotRun:['真实布局与横向溢出','七日屏幕与长尾声截图','键盘焦点与遮罩','读屏','系统导入导出']},null,2));console.log('BLOCKED: no usable browser; no installation attempted.');return;}
 const results=[];
 for(const [width,height]of matrix){
  const context=await browser.newContext({viewport:{width,height}}),page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('file://'+path.join(root,'dist/SeventhDay.html'));
  await page.screenshot({path:path.join(__dirname,`v04-${width}-title.png`),fullPage:true});
  await page.getByRole('button',{name:/翻开命运/}).click();await page.getByRole('button',{name:'推开门，进入第一日'}).click();
  for(let day=1;day<=7;day++){
   assert.equal(await page.locator('.choice').count(),4);assert.ok(await page.locator('.scene p').count()>=2);
   assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'horizontal overflow');assert.equal(await page.locator('.scene-art img').count(),1);assert.ok(await page.locator('.scene-art img').evaluate(el=>el.complete&&el.naturalWidth>0),'scene illustration loaded');
   await page.screenshot({path:path.join(__dirname,`v04-${width}-day${day}.png`),fullPage:true});
   await page.locator('.choice').nth(day%4).focus();await page.keyboard.press('Enter');
   assert.equal(await page.evaluate(()=>document.activeElement.id),'next-day');
   await page.keyboard.press('Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'next-day');await page.keyboard.press('Enter');
   assert.ok(await page.locator('main h1').evaluate(el=>document.activeElement===el));
  }
  await page.locator('.review summary').click();assert.equal(await page.locator('.history-row').count(),7);
  await page.screenshot({path:path.join(__dirname,`v04-${width}-ending.png`),fullPage:true});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.getByRole('button',{name:'查看命运图鉴'}).click();assert.equal(await page.locator('.ending-card').count(),1);
  await page.screenshot({path:path.join(__dirname,`v04-${width}-catalog.png`),fullPage:true});
  await page.reload();await page.getByRole('button',{name:'继续旅程'}).click();
  assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('seventh-day-v2')).completedRuns),1);
  assert.deepEqual(errors,[]);results.push({width,height,status:'automated_pass_screenshots_need_review'});await context.close();
 }
 await browser.close();fs.writeFileSync(path.join(__dirname,'browser-report-v04.json'),JSON.stringify({passed:true,status:'automated_only',viewports:results,manualStillRequired:['逐张视觉审查','读屏与系统文件选择器','Safari与移动端真实设备']},null,2));
})().catch(e=>{console.error(e);process.exitCode=1;});
