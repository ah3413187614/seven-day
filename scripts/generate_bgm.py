"""Five original, reproducible 24-second dark-fantasy loops (stdlib only).

Eight bars at 80 BPM. Bowed tones, plucked melody, low pulse and sparse bell
replace the previous quiet static drones. Mastered with headroom for fades.
"""
from pathlib import Path
import math
import struct
import wave

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/audio/bgm'
OUT.mkdir(parents=True, exist_ok=True)
RATE, SECONDS = 22050, 24
N = RATE * SECONDS
BEAT = .75
# Root MIDI note, four chord offsets, 16-beat motif, bed/string/pulse levels.
SCORES = {
    'title': (45, [[0, 3, 7], [-2, 3, 7], [-4, 0, 5], [-2, 2, 7]],
              [12, None, 15, 12, 10, None, 7, None, 8, 10, 12, None, 7, 5, 3, None], (.73, .75, .32)),
    'normal': (48, [[0, 3, 7], [5, 9, 12], [3, 7, 10], [7, 10, 14]],
               [7, 10, 12, None, 15, 12, 10, 7, 5, 7, 10, None, 12, 10, 7, None], (.70, .85, .24)),
    'tension': (38, [[0, 3, 7], [1, 5, 8], [0, 3, 6], [-2, 2, 5]],
                [12, None, 13, None, 6, 7, None, 6, 12, None, 13, 15, 13, 7, 6, None], (.80, .53, .55)),
    'final_day': (40, [[0, 3, 7], [-2, 3, 7], [-4, 0, 5], [-2, 2, 7]],
                  [7, 10, 12, 15, 19, 15, 12, 10, 8, 10, 12, 15, 14, 12, 7, None], (.82, .86, .58)),
    'ending': (53, [[0, 4, 7], [-2, 3, 7], [-4, 0, 5], [-2, 2, 7]],
               [7, None, 12, 11, 9, None, 7, 4, 5, 7, 9, None, 12, 9, 7, None], (.65, .68, .17)),
}
def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)
def add_note(buf, start, duration, frequency, amount, kind):
    for i in range(max(0, int(start * RATE)), min(N, int((start + duration) * RATE))):
        u = i / RATE - start
        if kind == 'pluck':
            env = (1 - math.exp(-55 * u)) * math.exp(-4.3 * u)
            tone = (math.sin(2 * math.pi * frequency * u)
                    + .32 * math.sin(4 * math.pi * frequency * u)
                    + .12 * math.sin(6 * math.pi * frequency * u))
        elif kind == 'bell':
            env = (1 - math.exp(-45 * u)) * math.exp(-2.8 * u)
            tone = math.sin(2 * math.pi * frequency * u) + .22 * math.sin(2 * math.pi * frequency * 2.01 * u)
        else:
            env = (1 - math.exp(-60 * u)) * math.exp(-8 * u)
            tone = math.sin(2 * math.pi * frequency * u)
        buf[i] += amount * env * tone
def make(name, score):
    root, chords, melody, (bed, strings, pulse) = score
    sound = [0.0] * N
    for bar in range(8):
        chord = chords[bar % 4]
        start = bar * 3.0
        for i in range(int(start * RATE), int((start + 3.0) * RATE)):
            t = i / RATE
            env = math.sin(math.pi * (t - start) / 3) ** .65
            shimmer = .94 + .06 * math.sin(2 * math.pi * .5 * t)
            for offset in chord:
                f = hz(root + offset)
                sound[i] += bed * env * shimmer * (math.sin(2 * math.pi * f * t)
                    + .13 * math.sin(2 * math.pi * 2 * f * t)) / 3
    for beat in range(32):
        offset = melody[beat % 16]
        # The second phrase responds to the first with a different register
        # and fewer attacks, instead of repeating exactly every 12 seconds.
        if beat >= 16 and beat % 8 in (2, 6):
            offset = None
        elif beat >= 16 and offset is not None and beat % 4 == 0:
            offset -= 5
        if offset is not None:
            add_note(sound, beat * BEAT, .8, hz(root + 12 + offset), strings * .32, 'pluck')
        if beat % 4 == 0:
            add_note(sound, beat * BEAT, .45, hz(root - 12 + chords[(beat // 4) % 4][0]), pulse * .25, 'pulse')
    for beat in (2, 10, 18, 26):
        add_note(sound, beat * BEAT, 1.1, hz(root + 31), .105, 'bell')
    dry = sound[:]
    delay = int(.23 * RATE)
    for i in range(N):
        sound[i] += .12 * dry[(i - delay) % N]
    # Ramp the seam, avoiding clicks while retaining a natural breath between phrases.
    for i in range(int(.07 * RATE)):
        fade = i / (.07 * RATE)
        sound[i] *= fade
        sound[N - 1 - i] *= fade
    rms = math.sqrt(sum(x * x for x in sound) / N)
    peak = max(abs(x) for x in sound)
    gain = min(.155 / rms, .78 / peak)
    pcm = bytearray()
    for value in sound:
        pcm.extend(struct.pack('<h', round(max(-.99, min(.99, value * gain)) * 32767)))
    with wave.open(str(OUT / f'{name}.wav'), 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(RATE)
        wav.writeframes(pcm)
    print(name, f'RMS={20*math.log10(rms*gain):.1f} dBFS', f'peak={peak*gain:.2f}')
for key, value in SCORES.items():
    make(key, value)
