import skimage
from skimage.color import rgb2gray
from skimage import io, img_as_ubyte
import numpy as np
from scipy import ndimage

def segmentation(image_path):
    img = io.imread(image_path)
    gray = rgb2gray(img)
    mean = np.mean(gray)
    seg = (gray > mean)
    output = img_as_ubyte(seg)
    io.imsave(image_path, output)

def img_to_gray(image_path):
    img = io.imread(image_path)
    gray = rgb2gray(img)
    io.imsave(image_path, gray)

def hist_equalization(image_path):
    img = io.imread(image_path)
    gray = img_as_ubyte(rgb2gray(img))
    x_max = gray.shape[1]
    y_max = gray.shape[0]
    total = gray.size
    hist = [0] * 256
    equ_hist = hist

    y = 0
    while y < y_max:
        x = 0
        while x < x_max:
            hist[gray[y, x]] += 1
            x += 1
        y += 1

    running_pct = 0
    equ_hist = hist
    value = 0

    output = gray

    while value < 255:
        hist[value] /= total
        running_pct += hist[value]
        equ_hist[value] = round(255 * running_pct)
        value += 1

    y = 0
    while y < y_max:
        x = 0
        while x < x_max:
            output[y,x] = equ_hist[(gray[y,x])]
            x += 1
        y += 1

    io.imsave(image_path, output)

def hist_segment(image_path): # This looks bad and weird
    img = io.imread(image_path)
    gray = img_as_ubyte(rgb2gray(img))
    x_max = gray.shape[1]
    y_max = gray.shape[0]
    total = gray.size
    hist = [0] * 256
    equ_hist = hist

    y = 0
    while y < y_max:
        x = 0
        while x < x_max:
            hist[gray[y, x]] += 1
            x += 1
        y += 1

    running_pct = 0
    equ_hist = hist
    value = 0

    output = gray

    while value < 255:
        hist[value] /= total
        running_pct += hist[value]
        equ_hist[value] = round(255 * running_pct)
        value += 1

    y = 0
    while y < y_max:
        x = 0
        while x < x_max:
            output[y,x] = equ_hist[(gray[y,x])]
            x += 1
        y += 1

    mean = np.mean(output)
    seg = (output > mean)

    io.imsave(image_path, seg)

def mask_convolution(image_path): #This looks bad and weird
    img = io.imread(image_path)
    gray = img_as_ubyte(rgb2gray(img))

    mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    output = ndimage.convolve(gray, mask, mode = 'constant', cval = 0.0)

    io.imsave(image_path, output)
