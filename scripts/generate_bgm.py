"""Original procedural ambience, strictly seamless 12-second 22050 Hz mono loops."""
from pathlib import Path
import math,random,struct,wave
R=Path(__file__).resolve().parents[1];p=R/'assets/audio/bgm';p.mkdir(parents=True,exist_ok=True)
rate=22050;seconds=12;n=rate*seconds
profiles={'title':([55,82.5,110],1),'normal':([65.4,98.1,130.8],2),'tension':([49,73.5,98],3),'final_day':([43.6,65.4,87.2],4),'ending':([55,110,164.8],5)}
for name,(notes,seed) in profiles.items():
 random.seed(seed);samples=bytearray()
 # Integer harmonic cycles over 12 seconds prevent clicks at the loop seam.
 hz=[round(x*seconds)/seconds for x in notes]
 for i in range(n):
  t=i/rate;slow=.84+.16*math.sin(2*math.pi*t/seconds)
  v=sum(math.sin(2*math.pi*f*t+0.12*k)*(.45/(k+1)) for k,f in enumerate(hz))*slow
  if name in ('tension','final_day'):v+=.08*math.sin(2*math.pi*round(1.5*seconds)/seconds*t)
  # Subtle distant bell twice per loop; envelope vanishes at each boundary.
  for at in (3,9):
   u=(t-at)%seconds
   if u<1.4:v+=.12*math.exp(-3*u)*math.sin(2*math.pi*round(330*seconds)/seconds*u)
  v=max(-1,min(1,v*.16));samples.extend(struct.pack('<h',int(v*32767)))
 with wave.open(str(p/f'{name}.wav'),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate);w.writeframes(samples)
print('5 original seamless quiet ambience loops')
