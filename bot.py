import time
import praw
from PIL import Image
import os

#picture compression stuff works so working on the reddit interaction now

#picture = Image.open("test.jpg")
#newPic = picture.save("/Users/bcollins/Desktop/test_compressed.jpg", quality=1)

# https://github.com/jacobgreenleaf/imgur-python/
# save url in text file

#os.system("cd Imgur && python main.py upload ../../test_compressed.jpg > ../url.txt")
#url = open('url.txt', 'r').readline()
#print url

r = praw.Reddit('needsMoreJPEGBot/0.1 by bcollinsNR'
                'Url: https://github.com/bcollinsNR/needsMoreJPEG')
r.login('needMoarJPEG','0111000001100001011100110111001101110111011011110111001001100100')
already_done = []


prawWords = ['testestestestestes', 'test']
while True:
    subreddit = r.get_subreddit('test')
    for submission in subreddit.get_hot(limit=10):
        op_text = submission.selftext.lower()
        has_praw = any(string in op_text for string in prawWords)
        # Test if it contains a PRAW-related question
        if submission.id not in already_done and has_praw:
            msg = '[PRAW related thread](%s)' % submission.short_link
            print('found match')
            print(submission.permalink)
            
            #already_done.append(submission.id)
    time.sleep(1800)
