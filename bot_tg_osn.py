import openai
from aiogram.utils import executor
from create_bot import disp

from handlers import client, admin, gpt_bot
print(openai.Model.list())



client.register_hendlers_client(disp)
gpt_bot.register_hendlers_gptbot(disp)

executor.start_polling(disp, skip_updates=True)
