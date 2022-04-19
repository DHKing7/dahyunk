import numpy as np

#######  Laplacian Filtering ############
# {0, 1, 0
#  1, -4, 0
#  0, 1, 0}   사용


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
f_x_y = np.append(av_img2, a2, axis=1)
laplacian_img4 = np.zeros(shape=(512, 512), dtype=np.uint8)
for k in range(512):
    for i in range(512):
        g_x_y = (-1) * int(f_x_y[int(k)+2][int(i)+1]) + (-1) * int(f_x_y[int(k)][int(i)+1]) + \
               5 * int(f_x_y[int(k)+1][int(i)+1]) + \
               (-1) * int(f_x_y[int(k)+1][int(i) +2]) + (-1) * int(f_x_y[int(k) + 1][int(i)])

        if g_x_y > 255:
            g_x_y = 255
        elif g_x_y < 0:
            g_x_y = 0
        laplacian_img4[k][i] = g_x_y
fid.close()


fid = open('laplacian_img4.raw', "bw")
laplacian_img4.tofile(fid)
fid.close()




######  Laplacian Filtering ############
# {1, 1, 1
#  1, -8, 1
#  1, 1, 1}   사용

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
f_x_y = np.append(av_img2, a2, axis=1)
laplacian_img8 = np.zeros(shape=(512, 512), dtype=np.uint8)
for k in range(512):
    for i in range(512):
        g_x_y = (-1)*int(f_x_y[int(k)][int(i)]) + (-1)*int(f_x_y[int(k)][int(i) + 1]) + (-1)*int(f_x_y[int(k)][int(i) + 2]) + \
               (-1)*int(f_x_y[int(k) + 1][int(i)]) + 9*int(f_x_y[int(k) + 1][int(i) + 1]) + (-1)*int(f_x_y[int(k) + 1][int(i) + 2]) + \
               (-1)*int(f_x_y[int(k) + 2][int(i)]) + (-1)*int(f_x_y[int(k) + 2][int(i) + 1]) + (-1)*int(f_x_y[int(k) + 2][int(i) + 2])
        if g_x_y > 255:
            g_x_y = 255
        elif g_x_y < 0:
            g_x_y = 0
        laplacian_img8[k][i] = g_x_y

fid.close()

fid = open('laplacian_img8.raw', "bw")
laplacian_img8.tofile(fid)
fid.close()
