import pokemon
# import opencv
import pillow

from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib
import requests
import os

# Account SID and Auth Token from www.twilio.com/console
client = Client('ACcecd8dc1f34f143557d2fe713048f71f', '3024182f46dc1f3d0d37d953e9a39856')

UPLOAD_FOLDER = os.getcwd() + '\images'
# UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)

# A route to respond to SMS messages
@app.route('/sms', methods=['GET', 'POST'])
def inbound_sms():

	if int(request.values['NumMedia']) > 0: #if incoming message has media
		image_url = request.values['MediaUrl0']

		response = MessagingResponse()
		response.message('Thanks for the picture')

		filename = request.form['MessageSid'] + '.jpeg'
		with open('{}\{}'.format(UPLOAD_FOLDER, filename), 'wb') as f:
			f.write(requests.get(image_url).content)

		pillow.img_to_gray('{}\{}'.format(UPLOAD_FOLDER, filename))

		with response.message() as message:
			message.body = "{0}".format("Here's you image in black and white.")
			message.media('https://6dbd7537c4ea.ngrok.io/uploads/{}'.format(filename))

	else:
		pokemon_number = urllib.parse.quote(request.form['Body'])

		response = MessagingResponse()
		response.message('Thanks for texting! Pokemon %s is %s' % (pokemon_number, pokemon.get_pokemon_name(pokemon_number).capitalize()))

    # Grab the relevant phone numbers.
	from_number = request.form['From']
	to_number = request.form['To']

	return str(response)


# A route to handle uploading images
@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
	return(send_from_directory(UPLOAD_FOLDER, filename))

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
