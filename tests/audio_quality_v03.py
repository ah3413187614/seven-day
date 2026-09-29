"""Signal sanity for the shipped loops; not a listening test."""
from pathlib import Path
import math,struct,wave
root=Path(__file__).resolve().parents[1]/'assets/audio/bgm'
measure={}
for path in sorted(root.glob('*.wav')):
    with wave.open(str(path)) as wav:
        assert wav.getnchannels()==1 and wav.getsampwidth()==2 and wav.getframerate()==22050
        samples=struct.unpack('<'+str(wav.getnframes())+'h',wav.readframes(wav.getnframes()))
        duration=len(samples)/wav.getframerate()
    rms=math.sqrt(sum(x*x for x in samples)/len(samples))/32768
    db=20*math.log10(rms)
    peak=max(abs(x) for x in samples)/32768
    assert 71.9<duration<72.1 and -18<db<-14 and peak<.8,(path,db,peak)
    # Second half has a genuinely different contour rather than a duplicated 12s buffer.
    half=len(samples)//2
    assert samples[:half]!=samples[half:half*2]
    measure[path.stem]={'seconds':round(duration,2),'rmsDbFS':round(db,2),'peak':round(peak,3)}
assert len(measure)==8 and max(x['rmsDbFS'] for x in measure.values())-min(x['rmsDbFS'] for x in measure.values())<1.5
print(measure)
