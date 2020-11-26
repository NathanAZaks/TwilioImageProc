# from pokemon import get_pokemon_name
# from pillow import img_to_gray
# from opencv import img_to_gray
from skimaging import segmentation, img_to_gray, hist_equalization, hist_segment, mask_convolution

from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from twilio.rest import Client
import urllib
import requests
import os

# Account SID and Auth Token from www.twilio.com/console
client = Client('ACcecd8dc1f34f143557d2fe713048f71f', '3024182f46dc1f3d0d37d953e9a39856')

ngrok_public_url = requests.get("http://127.0.0.1:4040/api/tunnels").json()['tunnels'][0]['public_url']

UPLOAD_FOLDER = os.getcwd() + '/images' # CHANGE TO BACKSLASH FOR WINDOWS

image_proc_options = {"a": img_to_gray, "b": segmentation, "c": hist_equalization, "d": hist_segment, "e": mask_convolution}

app = Flask(__name__)

# A route to respond to SMS messages
@app.route('/sms', methods=['GET', 'POST'])
def inbound_sms():

	if int(request.values['NumMedia']) == 1: # if incoming message has media
		image_url = request.values['MediaUrl0']

		if request.form['Body']: # Take first word of text and lowercase
			image_proc_choice = request.form['Body'].split()[0].lower()
			if image_proc_choice not in image_proc_options:
				image_proc_choice = "a"
		else:
			image_proc_choice = "a"

		response = MessagingResponse()
		response.message("Thanks for the picture! I'll be right back with the edited photo. I default make the image black and white.")

		filename = request.form['MessageSid'] + '.jpeg'
		with open('{}/{}'.format(UPLOAD_FOLDER, filename), 'wb') as f: # Open file
			f.write(requests.get(image_url).content)

		image_proc_options[image_proc_choice]('{}/{}'.format(UPLOAD_FOLDER, filename)) # Image Processing

		with response.message() as message:
			# message.body = "{0}".format("Here's your image in black and white.")
			message.body = "{0}".format("Here's your segmented image.")
			message.media(ngrok_public_url + '/uploads/{}'.format(filename))

	else:
		# pokemon_number = urllib.parse.quote(request.form['Body'])
		#
		# response = MessagingResponse()
		# response.message('Thanks for texting! Pokemon %s is %s' % (pokemon_number, get_pokemon_name(pokemon_number).capitalize()))

		response = MessagingResponse()
		response.message("Try sending one photo with either 'a' for black/white or 'b' for segmentation or 'c' for histogram equaliztion or 'd' for histogram segmentation or 'e' for mask convolve")

    # Grab the relevant phone numbers.
	from_number = request.form['From']
	to_number = request.form['To']

	return str(response)


# A route to handle uploading images
@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
	return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
