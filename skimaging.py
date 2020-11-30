import skimage
from skimage import io, img_as_ubyte, exposure, img_as_float
from skimage.color import rgb2gray
from skimage.filters import gaussian, unsharp_mask, try_all_threshold
from skimage.color.adapt_rgb import adapt_rgb, each_channel
import numpy as np
from scipy import ndimage

def img_to_gray(img):
    return img

@adapt_rgb(each_channel)
def segmentation(img):
    mean = np.mean(gray)
    seg = (gray > mean)
    return img_as_ubyte(seg)

@adapt_rgb(each_channel)
def hist_equalization(img):
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

    return img_as_ubyte(output)

@adapt_rgb(each_channel)
def hist_segment(img): # This looks bad and weird
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

    return img_as_ubyte(seg)

@adapt_rgb(each_channel)
def mask_convolution(img): #This looks bad and weird - Unsharp mask
    gray = img_as_ubyte(rgb2gray(img))

    mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    output = ndimage.convolve(gray, mask, mode = 'constant', cval = 0.0)

    return img_as_ubyte(output)

@adapt_rgb(each_channel)
def gauss_blur(img):
    return img_as_ubyte(gaussian(img, sigma = 5, multichannel = True))

@adapt_rgb(each_channel)
def unsharp(img):
    return img_as_ubyte(unsharp_mask(img, radius = 0.5, amount = 2))

@adapt_rgb(each_channel)
def adaptive_hist_equal(img):
    return img_as_ubyte(exposure.equalize_adapthist(img, clip_limit = 0.03))

@adapt_rgb(each_channel)
def manual_unsharp(img): # idk if this is doing anything
    blurred = gaussian(img, sigma = 10.0, multichannel = True)
    sharper = img - blurred

    return img_as_ubyte(img + (sharper * 0.8))
