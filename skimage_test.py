import skimage
from skimage.color import rgb2gray
from skimage import io, img_as_ubyte, img_as_float, exposure
from skimage.filters import gaussian, gabor, laplace, unsharp_mask, try_all_threshold
# gabor: edge detection, laplace: edge detection
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import data
from skimage.color.adapt_rgb import adapt_rgb, each_channel

image_path = '/Users/nathanzaks/Stevens/Schoolwork/CPE462A_ImageProc/Project/TwilioImageProc/images/img.jpg'

@adapt_rgb(each_channel)
def manual_unsharp(img): # idk if this is doing anything
    img = img_as_float(img)
    blurred = gaussian(img, sigma = 10.0, multichannel = True)
    sharper = img - blurred
    output = img + (sharper * 0.8)
    return output

astro = data.astronaut()
man = manual_unsharp(astro)
io.imshow(man)
