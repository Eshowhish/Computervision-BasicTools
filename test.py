import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import Image

Chihiro_Image_path='Dataset_opencvdl/Q3_Image/Chihiro.jpg'
# test
def Sobel(arr,rstart, cstart,masksize, divisor):
    s = 0
    x = 0
    y = 0

    for i in range(rstart, rstart+masksize, 1):
        x = 0
        for j in range(cstart, cstart+masksize, 1):
            if x == 0 and y == 0:
                p1 = arr[i][j]
            if x == 0 and y == 1:
                p2 = arr[i][j]
            if x == 0 and y == 2:
                p3 = arr[i][j]
            if x == 1 and y == 0:
                p4 = arr[i][j]
            if x == 1 and y == 1:
                p5 = arr[i][j]           
            if x == 1 and y == 2:
                p6 = arr[i][j]
            if x == 2 and y == 0:
                p7 = arr[i][j]
            if x == 2 and y == 1:
                p8 = arr[i][j]
            if x == 2 and y == 2:
                p9 = arr[i][j]
            x +=1
        y +=1
    return np.abs((p1 + 2*p2 + p3) - (p7 + 2*p8+p9)) + np.abs((p3 + 2*p6 + p9) - (p1 + 2*p4 +p7)) 


def padwithzeros(vector, pad_width, iaxis, kwargs):
    vector[:pad_width[0]] = 0
    vector[-pad_width[1]:] = 0
    return vector


im = Image.open(Chihiro_Image_path)
im.show()
img = np.asarray(im)
img.flags.writeable = True
p = 1
k = 2
m = img.shape[0]
n = img.shape[1]
masksize = 3
img = np.lib.pad(img, p, padwithzeros) #this function padds image with zeros to cater for pixels on the border.
x = 0
y = 0


for row in img:
    y = 0
    for col in row:
        if not (x < p or y < p or y > (n-k) or x > (m-k)):
        img[x][y] = Sobel(img, x-p,y-p,masksize,masksize*masksize)
        y = y + 1
  x = x + 1

img2 = Image.fromarray(img)
img2.show()