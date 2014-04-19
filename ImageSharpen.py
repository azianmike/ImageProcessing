__author__ = 'Michael'

from scipy import misc

# The 1st Method:
from PIL import Image, ImageFilter, ImageChops

im2 = Image.open("KindaSimilar2.jpg")
image2 = im2

im2 = im2.filter(ImageFilter.SHARPEN)
im2 = im2.filter(ImageFilter.SHARPEN)
im2 = im2.filter(ImageFilter.SHARPEN)
im2 = im2.filter(ImageFilter.SHARPEN)
im2 = im2.filter(ImageFilter.SHARPEN)

im2.save('KindaSimilar2Sharpen.jpg',"JPEG")
