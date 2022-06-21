import cv2
import os,argparse
import pytesseract
from PIL import Image


file = "./549.jpg"
text_file = "./549.jpg.txt"

# convert to gray
image = cv2.imread(file)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# pre-processor(s)
cv2.threshold(image_gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
# cv2.medianBlur(gray, 3)

# new gray file
new_file = "./549.gray.jpg"
cv2.imwrite(new_file, image_gray)

# image -> text
text = pytesseract.image_to_string(Image.open(new_file))

os.remove(new_file)
open(text_file, "w").write(text).close()


print(text)