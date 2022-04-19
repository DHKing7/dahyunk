import numpy as np

fid = open('white_lena.raw', 'rb')
rows = 512
cols = 512
f = np.fromfile(fid, dtype=np.uint8, count=rows * cols)
img = f.reshape((rows, cols))
histogram_img = np.zeros(shape=(512, 512), dtype=np.uint8)
############ img의 히스토그램화 ##############
histogram = np.histogram(img, bins= 186)
a= list(histogram[0])
b= [0]*71 + a
c = []
############# 누적합 배열에 담기 ###############
for i in range(256):
    c += [round(255*sum(b[0:i])/(515*512))]
############### 평준화 #################3
for k in range(512):
    for i in range(512):
        histogram_img[k][i] = c[int(img[k][i])]

fid.close()

fid = open('histogram_img.raw', "bw")
histogram_img.tofile(fid)
fid.close()
