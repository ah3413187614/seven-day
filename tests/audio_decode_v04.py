"""Decode each delivery asset and measure signal. This is not speaker QA."""
from pathlib import Path
import json,math,shutil,struct,subprocess
root=Path(__file__).resolve().parents[1]
assert shutil.which('ffprobe') and shutil.which('ffmpeg'),'ffmpeg tools required for delivery audio validation'
keys=['title','home','normal','explore','tension','final_day','ending','ending_dark']
report={}
for key in keys:
    f=root/'assets/audio/bgm/ogg'/f'{key}.ogg'
    assert f.is_file()
    info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name','-of','json',str(f)]))
    assert info['streams'][0]['codec_name']=='vorbis'
    duration=float(info['format']['duration']);assert abs(duration-72)<.1
    pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-f','s16le','-ac','1','-ar','22050','pipe:1'])
    samples=memoryview(pcm).cast('h');assert len(samples)>70*22050
    rms=math.sqrt(sum(int(s)*int(s) for s in samples)/len(samples))/32768
    db=20*math.log10(rms);peak=max(abs(s) for s in samples)/32768
    assert -18<db<-14 and peak<.8,(key,db,peak)
    report[key]={'duration':round(duration,2),'rmsDbFS':round(db,2),'peak':round(peak,3),'bytes':f.stat().st_size}
assert max(x['rmsDbFS'] for x in report.values())-min(x['rmsDbFS'] for x in report.values())<1.5
(root/'tests/audio-decode-report-v04.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('Eight delivered Ogg tracks decode; RMS span',round(max(x['rmsDbFS'] for x in report.values())-min(x['rmsDbFS'] for x in report.values()),2),'dB')
