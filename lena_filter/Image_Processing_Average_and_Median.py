import numpy as np

#######  Average filtering ############

fid = open('output_lena_GN_std_8.raw', 'rb')
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
print(av_img3)
list_avg = np.zeros(shape=(512, 512), dtype=np.uint8)
for k in range(512):
    for i in range(512):
        avg = (int(av_img3[int(k)][int(i)]) + int(av_img3[int(k)][int(i) + 1]) + int(av_img3[int(k)][int(i) + 2])
               + int(av_img3[int(k) + 1][int(i)]) + int(av_img3[int(k) + 1][int(i) + 1]) + int(
                    av_img3[int(k) + 1][int(i) + 2])
               + int(av_img3[int(k) + 2][int(i)]) + int(av_img3[int(k) + 2][int(i) + 1]) + int(
                    av_img3[int(k) + 2][int(i) + 2])) / 9
        list_avg[k][i] = avg

print(list_avg)
fid.close()

fid = open('lena_average.raw', "bw")
list_avg.tofile(fid)
fid.close()

###### Median Filtering ######


fid = open('lena_salt_noise.raw', 'rb')
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
print(av_img3)
list_med = np.zeros(shape=(512, 512), dtype=np.uint8)
for k in range(512):
    for i in range(512):
        med = [int(av_img3[int(k)][int(i)]), int(av_img3[int(k)][int(i) + 1]), int(av_img3[int(k)][int(i) + 2]),
               int(av_img3[int(k) + 1][int(i)]), int(av_img3[int(k) + 1][int(i) + 1]),
               int(av_img3[int(k) + 1][int(i) + 2]),
               int(av_img3[int(k) + 2][int(i)]), int(av_img3[int(k) + 2][int(i) + 1]),
               int(av_img3[int(k) + 2][int(i) + 2])]
        list_med[k][i] = int(np.median(med))

print(list_med)
fid.close()

fid = open('lena_median.raw', "bw")
list_avg.tofile(fid)
fid.close()
