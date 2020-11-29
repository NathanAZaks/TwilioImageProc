import skimage
from skimage.color import rgb2gray
from skimage import io, img_as_ubyte, img_as_float, exposure
from skimage.filters import gaussian, gabor, laplace, unsharp_mask, try_all_threshold
# Gaussian: blur, gabor: edge detection, laplace: edge detection
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import data
from skimage.color.adapt_rgb import adapt_rgb, each_channel

image_path = '/Users/nathanzaks/Stevens/Schoolwork/CPE462A_ImageProc/Project/TwilioImageProc/images/img.jpg'

img = img_as_float(io.imread(image_path))
gray = img_as_float(rgb2gray(img))

io.imshow(gray)

@adapt_rgb(each_channel)
def adaptive_hist_equal(image_path):
    output = exposure.equalize_adapthist(image_path, clip_limit = 0.03)

    return output

new = adaptive_hist_equal(gray)
io.imshow(new)
io.imshow(gray)
