#pip install pytesseract
#pip install pillow

import pytesseract as tes
tes.pytesseract.tesseract_cmd = r''  #Enter the path for tesseract.exe that is installed into your system
from PIL import Image

path = input("Enter the Image you want to know the data of:  ")
img = Image.open(path)

text = tes.image_to_string(img)

print(text)
