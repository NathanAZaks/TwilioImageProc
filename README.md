# TwilioImageProc
Image Processing with SMS Interface via Twilio

To Install:
* go to 'https://ngrok.com/download', install, unzip
* run `python3 -m pip install -r requirements.txt`

To run server:
* navigate to ngrok folder
** run `ngrok http 5000`
* in another terminal window
** run `python3 app.py`

Usage:
* update target webhook from twilio console as proper ngrok URL
* text 703-546-9420:
** a picture and it will process the image
** a number between 1-893 and it will return the pokemon name that corresponds to that pokemon number

Notes:
* requirements.txt has opencv and pillow which aren't actively being used right now
