import skimage
from skimage import io, img_as_ubyte, exposure, img_as_float
from skimage.color import rgb2gray
from skimage.filters import gaussian, unsharp_mask, try_all_threshold
from skimage.color.adapt_rgb import adapt_rgb, each_channel
import numpy as np
from scipy import ndimage

def img_to_gray(image_path, bw_option):
    img = io.imread(image_path)
    gray = rgb2gray(img)
    io.imsave(image_path, gray)

def segmentation(image_path, bw_option):
    img = io.imread(image_path)
    gray = rgb2gray(img)
    mean = np.mean(gray)
    seg = (gray > mean)
    output = img_as_ubyte(seg)
    io.imsave(image_path, output)

def hist_equalization(image_path, bw_option):
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

def hist_segment(image_path, bw_option): # This looks bad and weird
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

def mask_convolution(image_path, bw_option): #This looks bad and weird - Unsharp mask
    img = io.imread(image_path)
    gray = img_as_ubyte(rgb2gray(img))

    mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    output = ndimage.convolve(gray, mask, mode = 'constant', cval = 0.0)

    io.imsave(image_path, output)

def gauss_blur(image_path, bw_option):
    img = io.imread(image_path)

    output = gaussian(img, sigma = 5, multichannel = True)

    io.imsave(image_path, output)

def unsharp(image_path, bw_option):
    img = io.imread(image_path)

    output = unsharp_mask(img, radius = 0.5, amount = 2)

    io.imsave(image_path, output)

@adapt_rgb(each_channel)
def adaptive_hist_equal(img):
    return exposure.equalize_adapthist(img, clip_limit = 0.03)

def manual_unsharp(image_path, bw_option): # idk if this is doing anything
    img = img_as_float(io.imread(image_path))

    blurred = gaussian(img, sigma = 10.0, multichannel = True)
    sharper = img - blurred

    output = img + (sharper * 0.8)
    io.imsave(image_path, output)
