# TwilioImageProc
Image Processing with SMS Interface via Twilio

To Install:
* go to 'https://ngrok.com/download', install, unzip
* run `python3 -m pip install -r requirements.txt`

To run server:
* navigate to ngrok folder
  * run `ngrok http 5000`
* in another terminal window
  * run `python3 app.py`

Usage:
* update target webhook from twilio console as proper ngrok URL
* text 703-546-9420:
  * a picture and it will process the image
  * a picture and either 'a' or 'b'
    * 'a' will return black and white
    * 'b' will return threshold segmentation image

Notes:
* requirements.txt has opencv and pillow which aren't actively being used right now

Next steps:
* Add more image processing functions to `skimaging.py`
* Move to AWS/GCP instead of ngrok
  * Find way to programatically update twilio webhook address
* Remove test files and opencv/pillow files
* Delete all the twilio media files and automatically delete new ones when done
* When checking for BW flag, check for if no flag
* None of the text body for the responses is working I don't think
* Make all the functions similar to adaptive_hist_equal
* Figure out the lossy conversion error
