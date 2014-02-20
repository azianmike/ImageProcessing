test_pic = 'Similar1.jpg' #testing this pic against all pics in our db;
db = [
    [0, 0, 'KindaSimilar1.jpg'],
    [0, 0, 'KindaSimilar2.jpg'],
    [0, 0, 'island.jpg'],
    [0, 0, 'Rose1.jpg'],
    [0, 0, 'Rose2.jpg'],
    [0, 0, 'Different.jpg'],
    [0, 0, 'DifferentSubject.jpg'],
    [0, 0, 'Similar1.jpg'],
    [0, 0, 'Similar2.jpg'],
    [0, 0, 'SimilarNoFlash.jpg'],
    ]

from PIL import Image
from PIL import ImageStat
from PIL import ImageFilter
import time

def fe(file_name):
    im = Image.open(file_name)
    im = im.convert('L')
    w, h = 300, 300
    im = im.resize((w, h))
    imst = ImageStat.Stat(im)
    sr = imst.mean[0]
    def foo(t):
        if t < sr * 2 / 3: return 0
        if t <= sr: return 1
        if t < sr * 4 / 3: return 2
        return 3
    im = im.point(foo)
    res = [[0] * 4 for i in range(10)]
    for y in range(h):
        for x in range(w):
            k = im.getpixel((x, y))
            res[y / 60][k] += 1
            res[x / 60 + 5][k] += 1
    return res

def ff(file_name):
    im = Image.open(file_name)
    im = im.convert('L')
    w, h = 300, 300
    im = im.resize((w, h))
    im = im.filter(ImageFilter.FIND_EDGES)
    sr = ImageStat.Stat(im).mean[0]
    res = [0] * 10
    for y in range(h):
        for x in range(w):
            if im.getpixel((x, y)) > sr:
                res[y / 60] += 1
                res[x / 60 + 5] += 1
    #im.show()
    return res


start = time.clock()
z = [fe(db[i][2]) for i in range(len(db))]
test_z = fe(test_pic)
for k in range(len(db)):
    for i in range(10):
        for j in range(4):
            db[k][0] += abs(z[k][i][j] - test_z[i][j])

z = [ff(db[i][2]) for i in range(len(db))]
test_z = ff(test_pic)
for k in range(len(db)):
    for i in range(10):
        db[k][1] += abs(z[k][i] - test_z[i]) * 100.0 / (sum(z[k]) + sum(test_z))

db.sort()

print '------------------------------'
print '%12s       v1       v2' % (test_pic,)
print '------------------------------'
for k in range(len(db)):
    print '%12s %8.2f %8.2f' % (db[k][2], db[k][0] / 3600.0, db[k][1])
print '------------------------------'

print time.clock() - start


