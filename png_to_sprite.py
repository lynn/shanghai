from PIL import Image

img = Image.open("tiles.png")

rows = [
    ("dot", 9),
    ("bamboo", 9),
    ("char", 9),
    ("honor", 7),
    ("bonus", 8),
]

for y, (row_name, tile_count) in enumerate(rows):
    for x in range(tile_count):
        print(f"@s-{row_name}-{x+1}")
        for ty in range(3):
            for tx in range(2):
                bs = []
                for bit in [1, 2]:
                    for by in range(8):
                        byte = 0
                        for bx in range(8):
                            xx = 16*x + 8*tx + bx
                            yy = 24*y + 8*ty + by
                            if img.getpixel((xx, yy)) & bit:
                                byte |= 1 << 7-bx
                        bs.append(byte)
                print("    " + " ".join("%02x" % b for b in bs))
