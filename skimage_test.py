import skimage
from skimage.color import rgb2gray
from skimage import io, img_as_ubyte
import numpy as np


image_path = '/Users/nathanzaks/Stevens/Schoolwork/CPE462A_ImageProc/Project/TwilioImageProc/images/img.jpg'

img = io.imread(image_path)
img
img.imshow()

gray = rgb2gray(img)
gray

new_gray = gray

mean = np.mean(gray)
mean

img

type(img)

gray.shape
io.imshow(gray)

x = 0
y = 0

gray

seg = (gray > mean)

seg
io.imshow(seg)

new_gray
io.imshow(new_gray)

io.imshow(gray)

x, y = (gray > mean).nonzero()

vals = gray[x, y]

type(vals)

type(y)

io.imshow(vals)
io.show()

new_seg = img_as_ubyte(seg)

io.imsave('/Users/nathanzaks/Stevens/Schoolwork/CPE462A_ImageProc/Project/TwilioImageProc/images/seg.jpeg', new_seg)
