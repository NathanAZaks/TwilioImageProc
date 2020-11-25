import skimage
from skimage.color import rgb2gray
from skimage import io, img_as_ubyte
import numpy as np


def segmentation(image_path):
    img = io.imread(image_path)
    gray = rgb2gray(img)
    mean = np.mean(gray)
    seg = (gray > mean)
    output = img_as_ubyte(seg)
    io.imsave(image_path, seg)

def img_to_gray(image_path):
    img = io.imread(image_path)
    gray = rgb2gray(img)
    io.imsave(image_path, gray)
