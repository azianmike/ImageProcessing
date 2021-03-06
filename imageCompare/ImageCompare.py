

from PIL import Image
from PIL import ImageStat
from PIL import ImageFilter


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
    return res


def PrintOutStats(db, test_pic):
    print '------------------------------'
    print '%12s       v1       v2         Match?' % (test_pic,)
    print '------------------------------'
    for k in range(len(db)):
        match = 'false'
        if (((db[k][0] / 3600.0) <= 5) or (db[k][1] <= 5)):
            subtract = abs((db[k][0] / 3600.0) - db[k][1])
            if (subtract <= 5):
                match = 'true'
        output = '%12s %8.2f %8.2f ' % (db[k][2], db[k][0] / 3600.0, db[k][1])
        print output + match
    print '------------------------------'


def compareImages(test_pic, db):
    a = [fe(db[i][2]) for i in range(len(db))]
    b = [ff(db[i][2]) for i in range(len(db))]
    returnMe = []
    test_a = fe(test_pic)
    test_b = ff(test_pic)
    db2 = []
    for k in range(len(db)):
        for i in range(10):
            db[k][1] += abs(b[k][i] - test_b[i]) * 100.0 / (sum(b[k]) + sum(test_b))
            for j in range(4):
                db[k][0] += abs(a[k][i][j] - test_a[i][j])

        if (((db[k][0] / 3600.0) < 5) or (db[k][1] < 5)):
            print 'similar'
            subtract = abs((db[k][0] / 3600.0) - db[k][1])
            if subtract < 5:
                returnMe.append(db[k][2])
            else:
                db2.append([0, 0, db[k][2]])
        else:
            db2.append([0, 0, db[k][2]])

    db.sort()

    #PrintOutStats(db, test_pic)
    returnMe.append(test_pic)
    return returnMe, db2

def compareImages2(test_pic, db, folderName):
    a = [fe(folderName+db[i][2]) for i in range(len(db))]
    b = [ff(folderName+db[i][2]) for i in range(len(db))]
    returnMe = []
    test_a = fe(folderName+test_pic)
    test_b = ff(folderName+test_pic)
    db2 = []
    for k in range(len(db)):
        for i in range(10):
            db[k][1] += abs(b[k][i] - test_b[i]) * 100.0 / (sum(b[k]) + sum(test_b))
            for j in range(4):
                db[k][0] += abs(a[k][i][j] - test_a[i][j])

        if (((db[k][0] / 3600.0) < 5) or (db[k][1] < 5)):
            print 'similar'
            subtract = abs((db[k][0] / 3600.0) - db[k][1])
            if subtract <= 5 or ((db[k][0] / 3600.0) + db[k][1])/2 <= 5:
                returnMe.append(db[k][2])
            else:
                db2.append([0, 0, db[k][2]])

        else:
            db2.append([0, 0, db[k][2]])


    db.sort()

    # PrintOutStats(db, test_pic)
    returnMe.append(test_pic)
    return returnMe, db2


