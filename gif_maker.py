import os, glob
from pathlib import Path
from pickletools import optimize
from typing import List
from PIL import Image

images = []


fbs = int(input("Enter frames per second(FPS):"))
INPUT_DIR = r"C:\Users\CİHAN ŞAHİN\Desktop"
OUTPUT_GIF = "output.gif"
duration_ms = int(1000 / fbs)
frames = []
loop = 0

frames = sorted(glob.glob(os.path.join(INPUT_DIR, "*.png")) + glob.glob(os.path.join(INPUT_DIR, "*.jpg")))
if len(frames) == 0:
    print("❌ No frames found in folder:", INPUT_DIR)
    exit()
else:
    print(f"✅ {len(frames)} frames found.")

for frame_path in frames:
    img = Image.open(frame_path).convert("RGB")
    images.append(img)

    base_size = images[0].size
    images = [img.resize(base_size) for img in images]
    images[0].save(OUTPUT_GIF,
    save_all = True,
    append_images = images[1:],
    duration = duration_ms,
    loop = loop,
    optimize = True,
    )
    print("✅ GIF created:", OUTPUT_GIF)
