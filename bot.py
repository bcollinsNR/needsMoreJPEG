import praw
from PIL import Image
import os

picture = Image.open("test.jpg")
newPic = picture.save("/Users/bcollins/Desktop/test_compressed.jpg", quality=1)

# https://github.com/jacobgreenleaf/imgur-python/
# save url in text file

os.system("cd Imgur && python main.py upload ../../test_compressed.jpg > ../url.txt")
url = open('url.txt', 'r').readline()
print url

# todo: reddit API bot functionality
#  search for "Needs more JPEG!", or variant
#  get the image file
#  compress to 1 quality and save copy locally
#  upload to imgur, save url 
#  craft response 
#    get some template from somewhere 
#  post to reddit


# I know you need a user agent so reddit doesn't freak:
# user_agent = ("needsMoreJPEGBot/0.1 by bcollinsNR")



