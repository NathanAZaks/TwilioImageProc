import cv2

def img_to_gray(image_filepath):

    #implement scikit-image/numpy to read image from url

    img = cv2.imread(image_filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return(gray)

    # cv2.imshow("img", img)
    # cv2.imshow("img - gray", gray)
    #
    # cv2.waitKey(0)
    #
    # cv2.destroyAllWindows()
