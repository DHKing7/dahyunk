import numpy as np
fid = open('lena.raw', 'rb')
rows = 512
cols = 512
f = np.fromfile(fid, dtype=np.uint8,count=rows*cols)
img = f.reshape((rows, cols))
fid.close()
print(img)
print(len(img))
print(len(img[0]))
fid = open('lena.raw', 'rb')
rows = 512
cols = 512
f = np.fromfile(fid, dtype=np.uint8,count=rows*cols)
img = f.reshape((rows, cols))
img_reverse = 255-img
fid.close()
print(img_reverse)

fid = open('lena_reverse.raw', "bw")
img_reverse.tofile(fid)
fid.close()