from instagrapi import Client 
from instagrapi.types import Usertag, Location 
import config 
import sys

cl=Client()
cl.login(config.username, config.password)
# path=sys.argv[2]

def reels(path):
    reels_upload=cl.clip_upload(
        path=path,
        caption="what's a beautiful place",
        location=Location(name='Spain', lat='39.697793', lng='2.735736'))
#       extra_data={
#           'custom_accessibility_caption': 'alt text example',
#           'like_and_view_counts_disabled': False,
#           'disable_comments':False
# }) 
    return reels_upload
# path=r'C:\Users\Dell\lesson_1\instagram_upload\majorca-spain.jpg'
def photo(path):
    upload_photo=cl.photo_upload(
        path=path,
        caption="Monaco",
        location=Location(name='Monaco', lat='39.697793', lng='2.735736'))
   
    return upload_photo



if __name__ == "__main__":
 globals()[sys.argv[1]](sys.argv[2])
 
  

