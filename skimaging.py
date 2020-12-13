import skimage
from skimage import io, img_as_ubyte, exposure, img_as_float
from skimage.color import rgb2gray
from skimage.filters import gaussian, unsharp_mask
from skimage.color.adapt_rgb import adapt_rgb, each_channel
import numpy as np
from scipy import ndimage

def img_to_gray(img):
    if not len(img.shape) < 3:
        img = rgb2gray(img)
    return img_as_ubyte(img)

@adapt_rgb(each_channel)
def segmentation(img):
    mean = np.mean(img)
    seg = (img > mean)
    return img_as_ubyte(seg)

@adapt_rgb(each_channel)
def hist_equalization(img):
    # gray = img_as_ubyte(rgb2gray(img)) #Change all Gray to img
    img = img_as_ubyte(img)
    x_max = img.shape[1]
    y_max = img.shape[0]
    total = img.size
    hist = [0] * 256
    equ_hist = hist

    y = 0
    while y < y_max:
        x = 0
        while x < x_max:
            hist[img[y, x]] += 1
            x += 1
        y += 1

    running_pct = 0
    equ_hist = hist
    value = 0

    output = img

    while value < 255:
        hist[value] /= total
        running_pct += hist[value]
        equ_hist[value] = round(255 * running_pct)
        value += 1

    y = 0
    while y < y_max:
        x = 0
        while x < x_max:
            output[y,x] = equ_hist[(img[y,x])]
            x += 1
        y += 1

    return img_as_ubyte(output)

@adapt_rgb(each_channel)
def hist_segment(img): # This looks bad and weird
    # just run ^^ above function and continue from there
    # img = img_as_ubyte(img)
    # x_max = img.shape[1]
    # y_max = img.shape[0]
    # total = img.size
    # hist = [0] * 256
    # equ_hist = hist
    #
    # y = 0
    # while y < y_max:
    #     x = 0
    #     while x < x_max:
    #         hist[img[y, x]] += 1
    #         x += 1
    #     y += 1
    #
    # running_pct = 0
    # equ_hist = hist
    # value = 0
    #
    # output = img
    #
    # while value < 255:
    #     hist[value] /= total
    #     running_pct += hist[value]
    #     equ_hist[value] = round(255 * running_pct)
    #     value += 1
    #
    # y = 0
    # while y < y_max:
    #     x = 0
    #     while x < x_max:
    #         output[y,x] = equ_hist[(img[y,x])]
    #         x += 1
    #     y += 1

    output = hist_equalization(img)

    mean = np.mean(output)
    seg = (output > mean)

    return img_as_ubyte(seg)

@adapt_rgb(each_channel)
def mask_convolution(img): #This looks bad and weird - Unsharp mask
    mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    output = img_as_ubyte(ndimage.convolve(img, mask, mode = 'constant', cval = 0.0))

    return output

@adapt_rgb(each_channel)
def gauss_blur(img):
    output = img_as_ubyte(gaussian(img, sigma = 5, multichannel = True))
    return output

@adapt_rgb(each_channel)
def unsharp(img): # Edit the values to make it look better
    output = img_as_ubyte(unsharp_mask(img, radius = 2, amount = 5))
    return output

@adapt_rgb(each_channel)
def adaptive_hist_equal(img):
    output = img_as_ubyte(exposure.equalize_adapthist(img, clip_limit = 0.03))
    return output

@adapt_rgb(each_channel)
def manual_unsharp(img): # Looks bad, lossy conversion warning
    img = img_as_float(img)
    blurred = gaussian(img, sigma = 10.0, multichannel = True)
    sharper = img - blurred
    output = img + (sharper * 0.8)
    return output
