import cv2
import requests
import numpy as np

def img_to_gray(image_url):

	# image_url = r'api.twilio.com' + image_uri[:-5] # strip .json from uri and create url

	r = requests.get(image_url, stream = True).raw # retrieve raw image info from url

	img = np.asarray(bytearray(r.read()), dtype = 'uint8') # create cv-readable numpy array
	img = cv2.imdecode(img, cv2.IMREAD_COLOR) # create openable image

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to gray

	# cv2.imshow("Grey Image", gray)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	return(gray)
