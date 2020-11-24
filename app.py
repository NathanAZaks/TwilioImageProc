# use 'ngrok http 5000', 'python3 app.py', then you can send a text and get response

import pokemon
import opencv

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib

# Account SID and Auth Token from www.twilio.com/console
client = Client('ACcecd8dc1f34f143557d2fe713048f71f', '3024182f46dc1f3d0d37d953e9a39856')
app = Flask(__name__)


# A route to respond to SMS messages and kick off a phone call.
@app.route('/sms', methods=['POST'])
def inbound_sms():

    if int(request.values['NumMedia']) > 0: #if incoming message has media
        image_url = request.values['MediaUrl0']
        # print(image_url)
        response = MessagingResponse()
        response.message('Thanks for the picture')

        #call opencv manipulation stuff here


    else:
        pokemon_number = urllib.parse.quote(request.form['Body'])

        response = MessagingResponse()
        response.message('Thanks for texting! Pokemon %s is %s' % (pokemon_number, pokemon.get_pokemon_name(pokemon_number).capitalize()))

    # Grab the relevant phone numbers.
    from_number = request.form['From']
    to_number = request.form['To']

    # # Create a phone call that uses our other route to play a song from Spotify.
    # client.api.account.calls.create(to=from_number, from_=to_number,
    #                     url='http://sagnew.ngrok.io/call?track={}'
    #                     .format(song_title))

    return str(response)


# A route to handle the logic for phone calls.
# @app.route('/call', methods=['POST'])

# def outbound_call():
#     song_title = request.args.get('track')
#     track_url = spotify.get_track_url(song_title)
#
#     response = MessagingResponse()
#     response.play(track_url)
#     return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
