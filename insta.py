from instabot import Bot
from dotenv import load_dotenv
import os
# import glob
import random

try:
    os.remove('config/taric.ov_uuid_and_cookie.json')
except:
    pass

load_dotenv()
bot = Bot()

bot.login(username=os.getenv('user'), password=os.getenv('pass'))

# using glob, you can post pics by files name pattern.

# os.chdir('img')
# for i in glob.glob('*.png'):
#     bot.upload_photo(i, caption='glad to share that with you. My work <3 <3 #love #instagood #like #follow #instagram #photooftheday #photography #beautiful #fashion #picoftheday #bhfyp #happy #smile #art #life #me #likeforlikes #instadaily #cute #followme #likes #style #nature #instalike #myself #followforfollowback #beauty #photo #l #bhfyp')
    
file = random.choice(os.listdir('E:\Instabot\img'))


for i in file:
       bot.upload_photo(i, caption='glad to share that with you. My work <3 <3 #love #instagood #like #follow #instagram #photooftheday #photography #beautiful #fashion #picoftheday #bhfyp #happy #smile #art #life #me #likeforlikes #instadaily #cute #followme #likes #style #nature #instalike #myself #followforfollowback #beauty #photo #l #bhfyp')
