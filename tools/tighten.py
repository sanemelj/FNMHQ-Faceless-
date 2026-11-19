#!/usr/bin/env python3
"""Tighten an avatar clip: drop head/tail silence and internal pauses > MAXGAP.
usage: tighten.py clip.mp4 words.json KEY out.mp4 [--from A] [--to B] [--maxgap 0.35] [--pad 0.1]
words.json[KEY] = [(word, start, end), ...] in clip time. Writes out.mp4 and out.words.json (remapped times)."""
import sys, json, subprocess
a = sys.argv[1:]; clip, wj, key, out = a[:4]
opt = lambda k, d: float(a[a.index(k) + 1]) if k in a else d
A, B, MG, PAD = opt('--from', 0), opt('--to', 1e9), opt('--maxgap', 0.35), opt('--pad', 0.1)
W = [w for w in json.load(open(wj))[key] if w[1] >= A - 0.05 and w[2] <= B + 0.05]
segs = []
for w, s, e in W:
    if segs and s - segs[-1][1] <= MG: segs[-1][1] = e
    else: segs.append([s, e])
segs = [[max(A, s - PAD), min(B, e + PAD + 0.08)] for s, e in segs]
for i in range(1, len(segs)):  # avoid overlap
    if segs[i][0] < segs[i-1][1]: segs[i][0] = segs[i-1][1]
fc, cat = '', ''
for i, (s, e) in enumerate(segs):
    fc += f"[0:v]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS,fps=30[v{i}];[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={e-s-0.03:.3f}:d=0.03[a{i}];"
    cat += f"[v{i}][a{i}]"
fc += cat + f"concat=n={len(segs)}:v=1:a=1[v][a]"
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', clip, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', out], check=True)
# remap word times
nw, off = [], 0.0
for s, e in segs:
    for w, ws, we in W:
        if ws >= s - 0.01 and we <= e + 0.01: nw.append((w, round(ws - s + off, 3), round(we - s + off, 3)))
    off += e - s
json.dump({key: nw}, open(out.rsplit('.', 1)[0] + '.words.json', 'w'))
print(out, 'segments', len(segs), 'dur', round(off, 2), 'cut', round((min(B, 10) - A) - off, 2))
