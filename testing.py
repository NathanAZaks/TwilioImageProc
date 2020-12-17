from skimaging import *
from skimage import io
from skimage.color import rgb2gray

image_proc_options = {"a": img_to_gray, "b": segmentation, "c": hist_equalization, "d": hist_segment, "e": mask_convolution, "f": gauss_blur, "g": unsharp, "h": adaptive_hist_equal, "i": manual_unsharp}

image_proc_choice = 'a'
bw_option = 'a'

image_path = './images/img.jpg' # change to backslash for windows

print("Editing options:\na: Black and white\nb: Mean Threshold Segmentation\nc: Histogram Equalization\nd: Histogram Equalization Segmentation\ne: Mask Convolution\nf: Gaussian Blur\ng: Unsharpening Mask\nh: Adaptive Histogram Equalization\ni: Sharpen\nAnything else to quit.")

while(True):
    image_proc_choice = input("Enter one of the editing options letters:\n").lower()
    if image_proc_choice not in image_proc_options:
        print("Not valid option")
        break

    if image_proc_choice != 'a':
        bw_option = input("Enter 'y' if you want to process the image in black and white, anything else for color:\n")

    if bw_option == 'y':
        img = rgb2gray(io.imread(image_path))
    else:
        img = io.imread(image_path)

    output = image_proc_options[image_proc_choice](img) # Image Processing
    io.imshow(output)
    io.show()

print("Bye.")
