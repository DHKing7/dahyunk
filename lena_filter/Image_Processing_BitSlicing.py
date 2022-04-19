import numpy as np

fid = open('lena_water_mark.raw', 'rb')
rows = 512
cols = 512
f = np.fromfile(fid, dtype=np.uint8, count=rows * cols)
img = f.reshape((rows, cols))
imgList = img.tolist()

############## 2^7 슬라이싱 ###################
img7 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[0:1]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img7.append(line)
img_2_7 = np.array(img7, dtype=np.uint8)

fid = open('img_2_7.raw', "bw")
img_2_7.tofile(fid)
fid.close()

############## 2^6 슬라이싱 ###################
img6 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[1:2]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img6.append(line)
img_2_6 = np.array(img6, dtype=np.uint8)
fid.close()

fid = open('img_2_6.raw', "bw")
img_2_6.tofile(fid)
fid.close()

############## 2^5 슬라이싱 ###################
img5 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[2:3]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img5.append(line)
img_2_5= np.array(img5, dtype=np.uint8)
fid.close()

fid = open('img_2_5.raw', "bw")
img_2_5.tofile(fid)
fid.close()

############## 2^4 슬라이싱 ###################
img4 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[3:4]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img4.append(line)
img_2_4 = np.array(img4, dtype=np.uint8)
fid.close()

fid = open('img_2_4.raw', "bw")
img_2_4.tofile(fid)
fid.close()

############## 2^3 슬라이싱 ###################
img3 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[4:5]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img3.append(line)
img_2_3 = np.array(img3, dtype=np.uint8)
fid.close()

fid = open('img_2_3.raw', "bw")
img_2_3.tofile(fid)
fid.close()

############## 2^2 슬라이싱 ###################
img2 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[5:6]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img2.append(line)
img_2_2 = np.array(img2, dtype=np.uint8)
fid.close()

fid = open('img_2_2.raw', "bw")
img_2_2.tofile(fid)
fid.close()

############## 2^1 슬라이싱 ###################
img1 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[6:7]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img1.append(line)
img_2_1 = np.array(img1, dtype=np.uint8)
fid.close()

fid = open('img_2_1.raw', "bw")
img_2_1.tofile(fid)
fid.close()

############## 2^0 슬라이싱 ###################
img0 = []
for k in imgList:
    line = []
    for i in k:
        a = "{0:b}".format(i).zfill(8)
        if int(a[7:8]) == 1:
            a = int(255)
        else:
            a = int(0)
        line.append(a)
    img0.append(line)
img_2_0 = np.array(img0, dtype=np.uint8)
fid.close()

fid = open('img_2_0.raw', "bw")
img_2_0.tofile(fid)
fid.close()