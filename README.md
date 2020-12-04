# TwilioImageProc
Image Processing with SMS Interface via Twilio

To Install:
* go to 'https://ngrok.com/download', install, unzip
* run `python3 -m pip install -r requirements.txt`

To run software:
* navigate to ngrok folder
  * run `./ngrok http 5000`
* create a file `config.py` with:
  * `ACCOUNT_SID` AND `AUTH_TOKEN` taken from twilio
* in another terminal window
  * run `python3 app.py`

Usage:
* update target sms webhook from twilio console as public ngrok URL
* text 703-546-9420:
  * send a picture with a letter as the image editing option
    * ex: "<img.jpeg> a"
  * send a picture with a letter and 'wb' to process in black and white
    * ex: "<img.png> b wb"
  * send a picture without a letter, text without a picture, or a false editing option to receive a list of editing options

Next steps:
* Edit image processing functions to `skimaging.py`
  * Add Gabor Edge Detection Function
    * Example in `skimage_test.py`
  * Add Laplace Edge Detection Function
    * Example in `skimage_test.py`
* Move to AWS/GCP instead of ngrok
* Delete all the twilio media files and programatically delete new ones
* None of the text body for the responses is working
