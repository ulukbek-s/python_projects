from instabot import Bot

bot = Bot()

bot.login(username='user_name', password='password')
image='code.jpg'
bot.upload_photo(image, caption='second check')