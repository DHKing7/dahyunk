import numpy as np

###### sobel filter #########

fid = open('lena.raw', 'rb')
rows = 512
cols = 512
f = np.fromfile(fid, dtype=np.uint8, count=rows * cols)
img = f.reshape((rows, cols))
b = [0]
c = b * 512
a = np.array(c, dtype=np.uint8)
av_img = np.vstack([a, img, a])
a2 = np.array([[0]] * len(av_img), dtype=np.uint8)
av_img2 = np.append(a2, av_img, axis=1)
av_img3 = np.append(av_img2, a2, axis=1)
sobel_x_img = np.zeros(shape=(512, 512), dtype=np.uint8)
sobel_y_img = np.zeros(shape=(512, 512), dtype=np.uint8)
sobel_img = np.zeros(shape=(512, 512), dtype=np.uint8)
for k in range(512):
    for i in range(512):

        sobel_x = (-1) * int(av_img3[int(k)][int(i)]) + (-2) * int(av_img3[int(k)][int(i) + 1]) + \
                  (-1) * int(av_img3[int(k)][int(i) + 2]) + \
                  (1) * int(av_img3[int(k) + 2][int(i)]) + (1) * int(av_img3[int(k) + 2][int(i) + 1]) + \
                  (2) * int(av_img3[int(k) + 2][int(i) + 2])
        if sobel_x > 255:
            sobel_x = 255
        elif sobel_x < 0:
            sobel_x = 0
        sobel_x_img[k][i] = sobel_x

########## Y방향 edge 검출 ######################################
        sobel_y = (-1) * int(av_img3[int(k)][int(i)]) + (-2) * int(av_img3[int(k) + 1][int(i)]) + \
               (-1) * int(av_img3[int(k) + 2][int(i)]) + \
               (1) * int(av_img3[int(k)][int(i) + 2]) + (1) * int(av_img3[int(k) + 1][int(i) + 2]) + \
               (2) * int(av_img3[int(k) + 2][int(i) + 2])
        if sobel_y > 255:
            sobel_y = 255
        elif sobel_y < 0:
            sobel_y = 0
        sobel_y_img[k][i] = sobel_y

########## Gx+Gy ######################################

        sobel = abs(sobel_x) + abs(sobel_y)
        if sobel > 255:
            sobel = 255

        sobel_img[k][i] = sobel
fid.close()

fid = open('sobel_x_img.raw', "bw")
sobel_x_img.tofile(fid)
fid.close()


fid = open('sobel_y_img.raw', "bw")
sobel_y_img.tofile(fid)
fid.close()

fid = open('sobel_img.raw', "bw")
sobel_img.tofile(fid)
fid.close()