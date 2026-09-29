"""Original 72-second instrumental loops for the offline edition.

No external samples. Deterministic NumPy synthesis; project-owned composition.
The same four-note theme appears in different registers and modes across scenes.
"""
from pathlib import Path
import math
import wave
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/audio/bgm'
OUT.mkdir(parents=True,exist_ok=True)
RATE=22050
BPM=80
BEAT=60/BPM
BARS=24
SECONDS=BARS*4*BEAT
N=int(SECONDS*RATE)
THEME=[0,3,5,7,5,3,2,0]
# MIDI root, eight successive triads, melody/bed/arp/bass balance, density.
SCORES={
 'title':(50,[(0,3,7),(-2,3,7),(-4,0,5),(-2,2,7),(0,3,7),(3,7,10),(-4,0,5),(-2,2,7)],(.95,.75,.39,.25),.72),
 'home':(53,[(0,4,7),(5,9,12),(3,7,10),(-2,2,7),(0,4,7),(-4,0,5),(5,9,12),(-2,2,7)],(.83,.66,.48,.17),.64),
 'normal':(48,[(0,3,7),(5,9,12),(3,7,10),(7,10,14),(0,3,7),(-2,2,7),(3,7,10),(5,9,12)],(.82,.70,.45,.22),.75),
 'explore':(52,[(0,3,7),(-2,2,7),(-4,0,5),(1,5,8),(0,3,7),(3,7,10),(-4,0,5),(-2,2,7)],(.70,.54,.54,.19),.66),
 'tension':(45,[(0,3,7),(1,5,8),(0,3,6),(-2,2,5),(0,3,7),(-4,0,5),(1,5,8),(-2,2,5)],(.57,.72,.42,.33),.84),
 'final_day':(47,[(0,3,7),(-2,3,7),(-4,0,5),(-2,2,7),(0,3,7),(3,7,10),(-4,0,5),(-2,2,7)],(.79,.84,.57,.37),.94),
 'ending':(53,[(0,4,7),(-2,3,7),(-4,0,5),(-2,2,7),(0,4,7),(5,9,12),(-4,0,5),(-2,2,7)],(.72,.71,.28,.14),.60),
 'ending_dark':(48,[(0,3,7),(-2,2,5),(-4,0,5),(-2,2,7),(0,3,7),(1,5,8),(-4,0,5),(-2,2,5)],(.55,.67,.20,.18),.53),
}
def hz(midi):return 440*2**((midi-69)/12)
def note(out,start,duration,midi,amp,kind):
    a=int(start*RATE);b=min(N,int((start+duration)*RATE))
    if b<=a:return
    t=np.arange(b-a,dtype=np.float64)/RATE
    f=hz(midi)
    if kind=='bow':
        attack=np.minimum(1,t/.42);release=np.minimum(1,(duration-t)/.54)
        env=np.maximum(0,attack*release)
        tone=np.sin(2*np.pi*f*t)+.22*np.sin(2*np.pi*f*2*t)+.045*np.sin(2*np.pi*f*3*t)
        tone*=.95+.05*np.sin(2*np.pi*4.3*t)
    elif kind=='wood':
        env=(1-np.exp(-30*t))*np.exp(-2.5*t)
        tone=np.sin(2*np.pi*f*t)+.25*np.sin(2*np.pi*f*2*t)+.08*np.sin(2*np.pi*f*3*t)
    elif kind=='bell':
        env=(1-np.exp(-18*t))*np.exp(-1.85*t)
        tone=np.sin(2*np.pi*f*t)+.13*np.sin(2*np.pi*f*2.003*t)
    else:
        env=(1-np.exp(-12*t))*np.exp(-2.2*t)
        tone=np.sin(2*np.pi*f*t)+.18*np.sin(2*np.pi*f*2*t)
    out[a:b]+=amp*env*tone

def render(name,score):
    root,chords,(lead,bed,arp,bass),density=score
    sound=np.zeros(N,dtype=np.float64)
    for bar in range(BARS):
        chord=chords[bar%8]
        section=bar//8
        start=bar*4*BEAT
        # Each eight-bar movement changes voicing, phrase density and bass register.
        bed_gain=bed*(.76 if section==0 else .66 if section==1 else .82)
        for offset in chord:
            note(sound,start,4*BEAT+.16,root+offset-12 if offset==chord[0] else root+offset,bed_gain/3,'bow')
        for step in range(4):
            if step==3 and (bar+section)%3==0:continue
            index=(step+(bar%2))%3
            note(sound,start+(step+.5)*BEAT,.65,root+12+chord[index],arp*.28*(.75 if section==0 else 1),'wood')
        if bar%2==0:
            note(sound,start,1.0,root-12+chord[0],bass*.25,'wood')
        for step in range(4):
            beat=bar*4+step
            if (beat+section)%7==0 and density<.9:continue
            motif=THEME[(beat//2+bar//4)%len(THEME)]
            # Phrase response and cadence vary while retaining the common theme.
            interval=motif+(-2 if section==1 and beat%8 in (2,3) else 0)
            interval+=3 if section==2 and beat%12==0 else 0
            if step in (0,2) or (section==2 and step==3 and bar%2):
                note(sound,start+step*BEAT,.9,root+12+interval,lead*.30*(.8 if section==0 else 1),'wood')
        if bar%4==3:note(sound,start+2.5*BEAT,1.1,root+24+chord[1],.075,'bell')
    # Low unobtrusive room reflections; leave a small intentional breath at the seam.
    dry=sound.copy()
    for delay,gain in ((.19,.085),(.37,.047)):
        n=int(delay*RATE);sound[n:]+=gain*dry[:-n]
    n=int(.16*RATE)
    ramp=np.linspace(0,1,n)
    sound[:n]*=ramp
    sound[-n:]*=ramp[::-1]
    rms=np.sqrt(np.mean(sound*sound));peak=np.max(np.abs(sound))
    gain=min(.15/rms,.72/peak)
    samples=np.rint(np.clip(sound*gain,-.99,.99)*32767).astype('<i2')
    with wave.open(str(OUT/f'{name}.wav'),'wb') as wav:
        wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(RATE);wav.writeframes(samples.tobytes())
    print(name, f'{SECONDS:.0f}s',f'RMS={20*math.log10(rms*gain):.1f}dBFS',f'peak={peak*gain:.2f}')
for key,score in SCORES.items():render(key,score)
