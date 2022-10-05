from PIL import Image

img = Image.open("font.png")

lines = []
lines.append("@font")

for x in range(128):
    bs = []
    for ty in range(2):
        for tx in range(1):
            for by in range(8):
                byte = 0
                for bx in range(8):
                    xx = 8*x + bx
                    yy = 8*ty + by
                    if img.getpixel((xx, yy)) == 2:
                        byte |= 1 << 7-bx
                bs.append(byte)
    lines.append("    " + " ".join("%02x" % b for b in bs))

with open("font.tal", "w") as f:
    f.write("\n".join(lines) + "\n")
