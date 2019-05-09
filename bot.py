from selenium import webdriver
from PIL import Image
import datetime
import time
import tweepy

# Twitter API Auth
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# file paths
DRIVER = ''
original_image_path = ''
cropped_image_path = ''

# varables
dt = datetime.datetime.now()
dt = str(dt)
driver = webdriver.Chrome(DRIVER)

# opens driver and takes screenshot saving it with the a datetime stamp prepended
def open_driver():
    driver.get('http://outagemap.cpsenergy.com/CPSStaticMapsEXT/CPSStaticMapV2_EXT.html')
    time.sleep(5)
    driver.save_screenshot(dt + '.png')
    driver.quit()


# Crops image then posts it to twitter
def post_cropped_img():
    filename = dt + '.png'
    # uses PIL to  crop image
    image = Image.open(filename)
    cropped_image = image.crop((0, 50, 690, 685))
    cropped_image.save(cropped_image_path + filename)

    # uses twitter api to post image
    api.update_with_media(cropped_image_path + filename)

open_driver()
post_cropped_img()