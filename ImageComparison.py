__author__ = 'Michael'

from PIL import ImageChops, Image
import math, operator, time
from itertools import izip

def rmsdiff(im1, im2):
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms

def comparePercets(i1, i2):
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."

    pairs = izip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
    # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    return (dif / 255.0 * 100) / ncomponents



im1 = Image.open("KindaSimilar1.jpg")
im2 = Image.open("KindaSimilar2.jpg")

im5 = Image.open("Different.jpg")
im6 = Image.open("island.jpg")
im7 = Image.open("SimilarNoFlash.jpg")
im8 = Image.open("DifferentSubject.jpg")
im9 = Image.open("Rose1.jpg")
im10 = Image.open("Rose2.jpg")
print 'done opening images'
sameImage = 572.43340224
start = time.clock()
# print str(rmsdiff(im1, im2)) + 'kinda similar ones'  #about 70 +-?
# print str(rmsdiff(im1, im1)) + 'same'
# print str(rmsdiff(im2, im7)) + 'sorta similar no flash'
# print str(rmsdiff(im2, im8)) + 'sorta similar moved'
# print str(rmsdiff(im9, im10)) + 'same rose'
# print str(rmsdiff(im1, im10)) + 'very different'
print str(comparePercets(im1, im2)) + '% diff percents'
print str(comparePercets(im1, im9)) + '% diff percents'
elapsed = time.clock() - start
print elapsed