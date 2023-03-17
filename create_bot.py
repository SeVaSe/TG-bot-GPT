import openai
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

token = 'Ваш токен бота'
openai.api_key = 'Ваш токен OpenAI бота'

bot = Bot(token)
disp = Dispatcher(bot)



