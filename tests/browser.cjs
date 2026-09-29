const {chromium}=require('playwright');const path=require('path');const fs=require('fs');const assert=require('assert/strict');
(async()=>{
 const root=path.resolve(__dirname,'..'),browser=await chromium.launch({headless:true,args:['--no-sandbox']});const page=await browser.newPage({viewport:{width:1440,height:1060}});const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto('file://'+path.join(root,'dist/SeventhDay.html'));
 await page.screenshot({path:path.join(root,'tests/title.png'),fullPage:true});
 await page.getByRole('button',{name:/翻开命运之书/}).click();await page.locator('.choice').first().waitFor();assert.equal(await page.locator('.choice').count(),4);
 await page.screenshot({path:path.join(root,'tests/day1.png'),fullPage:true});
 await page.locator('.choice').first().click();await page.getByRole('button',{name:/迎接第 2 日/}).click();
 const expectedTitle=await page.locator('.chapter-title').innerText();await page.reload();await page.getByRole('button',{name:'继续旅程'}).click();assert.equal(await page.locator('.chapter-title').innerText(),expectedTitle);
 for(let d=2;d<=7;d++){assert.equal(await page.locator('.choice').count(),4);await page.locator('.choice').nth(d%4).click();await page.locator('#next-day').click();}
 await page.locator('.ending-head').waitFor();assert.equal(await page.locator('.history-row').count(),7);await page.screenshot({path:path.join(root,'tests/ending.png'),fullPage:true});
 const p=await page.evaluate(()=>JSON.parse(localStorage.getItem('seventh-day-v1')));assert.equal(p.completedRuns,1);assert.equal(Object.keys(p.collection).length,1);
 await page.reload();await page.getByRole('button',{name:'继续旅程'}).click();const p2=await page.evaluate(()=>JSON.parse(localStorage.getItem('seventh-day-v1')));assert.equal(p2.completedRuns,1);
 await page.getByRole('button',{name:'查看命运图鉴'}).click();assert.equal(await page.locator('.ending-card').count(),1);
 await page.getByRole('button',{name:'开始另一段旅程'}).click();assert.equal(await page.locator('.choice').count(),4);
 await page.setViewportSize({width:390,height:844});await page.screenshot({path:path.join(root,'tests/mobile.png'),fullPage:true});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth),'mobile overflow');
 assert.deepEqual(errors,[]);await browser.close();fs.writeFileSync(path.join(root,'tests/browser-report.json'),JSON.stringify({passed:true,checks:['file://离线加载','无脚本异常','七日四选一通关','刷新后恢复同一节点','结束后不重复计次','图鉴记录','再开一局','390px屏幕无横向溢出']},null,2));console.log('Browser checks passed');
})().catch(e=>{console.error(e);process.exit(1)});
