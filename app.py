from skimaging import *
from skimage import io, img_as_ubyte
from skimage.color import rgb2gray
from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from twilio.rest import Client
import urllib
import requests
import os

# Account SID and Auth Token from www.twilio.com/console
ACCOUNT_SID = 'ACcecd8dc1f34f143557d2fe713048f71f'
AUTH_TOKEN = '3024182f46dc1f3d0d37d953e9a39856'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

ngrok_public_url = requests.get("http://127.0.0.1:4040/api/tunnels").json()['tunnels'][0]['public_url']

UPLOAD_FOLDER = os.getcwd() + '/images' # CHANGE TO BACKSLASH FOR WINDOWS

image_proc_options = {"a": img_to_gray, "b": segmentation, "c": hist_equalization, "d": hist_segment, "e": mask_convolution, "f": gauss_blur, "g": unsharp, "h": adaptive_hist_equal, "i": manual_unsharp}

editing_string = "Send one picture with one of the following options:\na bw: Black and white\nb: Mean Threshold Segmentation\nc: Histogram Equalization\nd: Histogram Equalization Segmentation\ne: Mask Convolution\nf: Gaussian Blur\ng: Unsharpening Mask\nh: Adaptive Histogram Equalization\ni: Sharpen\nSend 'bw' to process in black and white"

app = Flask(__name__)

# A route to respond to SMS messages
@app.route('/sms', methods=['GET', 'POST'])
def inbound_sms():

	if int(request.values['NumMedia']) == 1: # if incoming message has media
		image_url = request.values['MediaUrl0']

		if request.form['Body']: # Take first word of text and lowercase
			image_proc_choice = request.form['Body'].split()[0].lower()

			if request.form['Body'].split()[1]:
				bw_option = request.form['Body'].split()[1].lower()
			else:
				bw_option = 'no'

			if image_proc_choice not in image_proc_options:
				image_proc_choice = 0

		else:
			image_proc_choice = 0

		if image_proc_choice == 0: # THIS TEXT WORKS
			response = MessagingResponse()
			response.message(editing_string)
			return str(response)

		response = MessagingResponse() # THIS TEXT DOES NOT WORK
		response.message("Thanks for the picture! I'll be right back with the edited photo.")

		filename = request.form['MessageSid'] + '.jpeg'
		file_path = '{}/{}'.format(UPLOAD_FOLDER, filename)

		with open(file_path, 'wb') as f: # Open file
			f.write(requests.get(image_url).content)

		if bw_option == 'bw':
			img = rgb2gray(io.imread(file_path))
		else:
			img = io.imread(file_path)

		output = img_as_float(image_proc_options[image_proc_choice](img)) # Image Processing
		io.imsave(file_path, output)


		response = MessagingResponse()
		with response.message() as message:
			message.body = "{0}".format("Here's your image.") # THIS TEXT IS NOT WORKING
			message.media(ngrok_public_url + '/uploads/{}'.format(filename))

	else:
		response = MessagingResponse() # THIS TEXT WORKS
		response.message(editing_string)
		return str(response)

    # Grab the relevant phone numbers.
	from_number = request.form['From']
	to_number = request.form['To']

	return str(response)


# A route to handle uploading images
@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def upload_file(filename):
	return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
