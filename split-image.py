import cv2;
import numpy;
import sys;

if (len(sys.argv) != 4):
  print("usage: split-image.py source hex column\n\tsource: image to split\n\thex: hex code of color to look for\n\tcolumn: how many pixels over from the left to search for the given color")
  exit()
src_file, col, hex = sys.argv[1:4]
col = int(col)

bgr = tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))[::-1]
print(bgr)

def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

src = cv2.imread(src_file)
print(type(src[0, 0]))
for row in range(src.shape[0]):
  pxl = src[row, col]
  if (totuple(pxl) == bgr):
    print(row)
