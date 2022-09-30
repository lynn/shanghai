import math
def sin(x):
    return math.sin(2*math.pi*x)
def wave(x):
    return (sin(x) + sin(2*x) + sin(3*x) + sin(4*x)) / 4

chords = [
    #("min", [16, 20, 27]),
    #("maj", [16, 20, 24]),
    ("sus2", [8, 9, 12]),
    #("dom", [14, 16, 20]),
    ("note", [1]),
]

for name, notes in chords:
    L = 256
    buf = []
    for i in range(L):
        f = sin if name == "note" else wave
        s = sum(f(k*i/L) for k in notes) / len(notes)
        buf.append(int(s * 126 + 128))
    buf = bytes(buf)
    #with open(f"{name}.pcm", "wb") as f:
    #    f.write(buf)
    with open(f"{name}.tal", "w") as f:
        f.write(f"@wave-{name}\n")
        for i in range(0, L, 16):
            f.write(f"    " + buf[i:i+16].hex(" ") + "\n")
