import praw
from PIL import Image
import os

# user_agent = ("needsMoreJPEGBot/0.1 by bc")

picture = Image.open("test.jpg")
newPic = picture.save("/Users/bcollins/Desktop/reddit/Imgur/test_compressed.jpg", quality=1)

# https://github.com/jacobgreenleaf/imgur-python/
# save url in text file

# works, but very clunky
os.system("cd Imgur && python main.py upload test_compressed.jpg > ../url.txt")
url = open('url.txt', 'r').readline()
print url

# todo:" how to do this without using a file to save url? i am such a noob... :(

# todo: reddit API bot functionality
#  search for "Needs more JPEG!", or variant
#  get the image file
#  compress to 1 quality and save copy locally
#  upload to imgur, save url 
#  craft response and post to reddit
#  profit