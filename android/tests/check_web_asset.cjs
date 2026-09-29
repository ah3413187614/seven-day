const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
const source = fs.readFileSync('app/src/main/assets/SeventhDay.html', 'utf8');
const scripts = [...source.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(x => x[1]);
assert.equal(scripts.length, 5);
scripts.forEach((s, i) => new vm.Script(s, {filename: `android-asset-${i}.js`}));
assert.equal((source.match(/AndroidBridge\.saveJson/g) || []).length, 1);
console.log('Android asset JavaScript syntax passed');
