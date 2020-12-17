# TwilioImageProc
SciKit Image Processing with SMS Interface via Twilio

To Install Dependencies:
* go to 'https://ngrok.com/download', install, unzip
  * This project using version 2.3.35
* run `python3 -m pip install -r requirements.txt`

To run software:
* navigate to ngrok folder
  * run `./ngrok http 5000`
* create a file `config.py` with:
  * `ACCOUNT_SID` AND `AUTH_TOKEN` taken from twilio
  * ex:
    * `ACCOUNT_SID = "sid_goes_here"`
    * `AUTH_TOKEN = "auth_token_goes_here"`
* in another terminal window
  * run `python3 app.py`
* update target sms webhook from twilio console as public ngrok URL

Twiilio Instructions:
* Create a Twilio account
  * This will give you demo credits which are sufficient to run this project for a while
* Buy a phone number from Twilio (with the demo credits $) that is capable of SMS
* Configure the Primary SMS Webhook for the phone number inside of the Twilio console
  * The correct webhook address taken from 'Forwarding' line from ngrok window: 'https://yourngrokurl.ngrok.io/sms'

Usage:
* text twilio phone number:
  * send a picture with a letter as the image editing option
    * ex: "<img.jpeg> a"
  * send a picture with a letter and 'bw' to process in black and white
    * ex: "<img.png> b bw"
  * send a picture without a letter, text without a picture, or an incorrect editing option (any other format) to receive a list of editing options
* files set up for linux/mac. Check App.py to change / to \ for windows filesystem compatibility

Testing:
* `testing.py` can be used to test the various image processing functions without the Twilio aspect
* To use:
  * navigate to code folder in terminal
  * run `python3 testing.py`
  * follow on screen directions:
    * enter an editing option
    * enter a b/w option
    * code will loop until editing option not in list

Next steps:
* Add more editing functions
* Move to AWS/GCP instead of ngrok
* Delete all the Twilio media files and programmatically delete new ones
