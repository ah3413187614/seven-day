"""Original code-native pixel avatars, 16×24 logical pixels, no raster source."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parents[1];out=R/'assets/characters/pixel';out.mkdir(parents=True,exist_ok=True)
# Silhouette, complexion, coat, headwear, held object. All 14 have distinct palettes/props.
specs=[
('npc_01','#c5ad76','#273d40','crown','seal'),('npc_02','#aaa9a2','#3b454e','helm','shield'),
('npc_03','#d8ccad','#474b52','hood','staff'),('npc_04','#d9cbb1','#586b67','veil','case'),
('npc_05','#a78d78','#465256','horn','scroll'),('npc_06','#947a68','#65604d','horn','hammer'),
('npc_07','#ac8a70','#504342','horn','spear'),('npc_08','#607b79','#29494c','crest','wing'),
('npc_09','#d5be9b','#53635a','ear','map'),('npc_10','#b89d7e','#50483d','cap','hammer'),
('npc_11','#c4ac84','#4a564e','cap','book'),('npc_12','#cbb19a','#55534c','cap','page'),
('npc_13','#bdb1a8','#343c43','white','tube'),('npc_14','#d2c7a7','#343c40','halo','lamp')]
for cid,skin,cloth,head,prop in specs:
 pixels=[]
 def rect(x,y,w,h,color):pixels.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')
 iron='#18292e';gold='#aa9463';light='#b4c9bc'
 if cid=='npc_08':
  rect(2,9,12,9,cloth);rect(1,13,5,7,skin);rect(10,13,5,7,skin);rect(5,4,6,7,skin);rect(3,3,3,4,skin);rect(10,3,3,4,skin);rect(7,10,2,8,gold)
 else:
  rect(3,21,4,3,iron);rect(9,21,4,3,iron);rect(2,11,12,11,cloth);rect(1,12,2,8,skin);rect(13,12,2,8,skin);rect(4,5,8,7,skin);rect(5,7,2,1,iron);rect(9,7,2,1,iron)
  rect(6,11,4,2,gold)
 if head=='crown':rect(4,3,8,2,gold);rect(4,1,2,2,gold);rect(7,1,2,2,gold);rect(10,1,2,2,gold)
 elif head=='helm':rect(3,2,10,4,iron);rect(7,1,2,3,gold)
 elif head in ('hood','veil'):rect(3,2,10,4,light if head=='veil' else cloth);rect(2,5,2,7,light if head=='veil' else cloth)
 elif head=='horn':rect(3,2,2,5,iron);rect(11,2,2,5,iron);rect(4,2,2,2,skin);rect(10,2,2,2,skin)
 elif head=='ear':rect(2,5,2,4,skin);rect(12,5,2,4,skin);rect(4,2,8,3,iron)
 elif head=='cap':rect(3,3,10,3,iron);rect(2,5,5,1,iron)
 elif head=='white':rect(3,2,10,4,'#d6d5ce');rect(3,6,2,6,'#d6d5ce')
 elif head=='halo':rect(3,0,10,2,gold);rect(2,2,2,5,gold);rect(12,2,2,5,gold)
 if prop in ('staff','spear'):rect(14,5,1,17,gold)
 if prop=='shield':rect(0,12,4,7,iron);rect(1,13,2,4,gold)
 if prop in ('seal','book','case','scroll','map','page'):rect(11,14,4,5,'#b8a477');rect(12,15,2,1,iron)
 if prop=='hammer':rect(13,13,1,9,gold);rect(11,13,5,2,iron)
 if prop=='tube':rect(2,13,2,9,light)
 if prop=='lamp':rect(13,11,2,5,gold);rect(13,9,2,2,'#ecd9a5')
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 24" shape-rendering="crispEdges" role="img" aria-label="像素角色"><title>{escape(cid)}</title>'+''.join(pixels)+'</svg>'
 (out/f'{cid}.svg').write_text(svg)
print('14 original pixel avatars')
