import cv2;
import os;
import sys;

def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

# extract args
if (len(sys.argv) != 4):
  print("usage: split-image.py source hex column\n\tsource: image to split\n\thex: hex code of color to look for\n\tcolumn: how many pixels over from the left to search for the given color")
  exit()
src_file, col, hex = sys.argv[1:4]
col = int(col)

# make a folder to store split images
src_prefix, src_type = src_file.split('.')
folder_name = f'{src_prefix}_splits'
if not os.path.exists(folder_name):
  os.mkdir(folder_name)

# convert hex to reversed rgb
bgr = tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))[::-1]

# find pixels
src = cv2.imread(src_file)
prev = 0
count = 0
ht = src.shape[0]
wt = src.shape[1]
for row in range(1, ht):
  pxl = src[row, col]
  if (row == ht - 1 or totuple(pxl) == bgr):
    out = os.path.join(folder_name, f'{src_prefix}_{str(count).zfill(4)}.{src_type}')
    cv2.imwrite(out, src[prev:row + 1, 0:wt])
    count += 1
    prev = row

print("done");