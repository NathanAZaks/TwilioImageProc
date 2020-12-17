from skimaging import *
import config

from skimage import io, img_as_ubyte
from skimage.color import rgb2gray
from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from twilio.rest import Client
import urllib
import requests
import os

client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)

ngrok_public_url = requests.get("http://127.0.0.1:4040/api/tunnels").json()['tunnels'][0]['public_url'] # Get Public ngrok URL via internal ngrok api

UPLOAD_FOLDER = os.getcwd() + '/images' # CHANGE TO BACKSLASH FOR WINDOWS

image_proc_options = {"a": img_to_gray, "b": segmentation, "c": hist_equalization, "d": hist_segment, "e": mask_convolution, "f": gauss_blur, "g": unsharp, "h": adaptive_hist_equal, "i": manual_unsharp}

editing_string = "Send one picture with one of the following options:\na: Black and white\nb: Mean Threshold Segmentation\nc: Histogram Equalization\nd: Histogram Equalization Segmentation\ne: Mask Convolution\nf: Gaussian Blur\ng: Unsharpening Mask\nh: Adaptive Histogram Equalization\ni: Sharpen\nSend 'bw' to process in black and white"

app = Flask(__name__)

# A route to respond to SMS messages
@app.route('/sms', methods=['GET', 'POST'])
def inbound_sms():

	response = MessagingResponse() #initiate twilio response object

	if int(request.values['NumMedia']) == 1: # Check if incoming message has media
		image_url = request.values['MediaUrl0']

		if request.form['Body']: # Take first word of text and lowercase
			image_proc_choice = request.form['Body'].split()[0].lower()

			try: # Check if there are two words where second is the b/w flag
				bw_option = request.form['Body'].split()[1].lower()
			except IndexError: # If no second word
				bw_option = 'no'

			if image_proc_choice not in image_proc_options:
				image_proc_choice = 0

		else:
			image_proc_choice = 0

		if image_proc_choice == 0: # If no/incorrect editing option, send back instructions
			response.message(editing_string)
			return str(response)

		response.message("Thanks for the picture! I'll be right back with the edited photo.")

		filename = request.form['MessageSid'] + '.jpeg' # Call image file as message sid
		file_path = '{}/{}'.format(UPLOAD_FOLDER, filename)

		with open(file_path, 'wb') as f: # Open new file on this computer
			f.write(requests.get(image_url).content)

		if bw_option == 'bw':
			img = rgb2gray(io.imread(file_path))
		else:
			img = io.imread(file_path)

		output = image_proc_options[image_proc_choice](img) # Image Processing
		io.imsave(file_path, output) # Save edited image to original file path

		response.message().media(ngrok_public_url + '/uploads/{}'.format(filename)) # Send back edited image
		response.message("Here's your edited image.")

	else: # Incoming message has no media - send back editing instructions
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
