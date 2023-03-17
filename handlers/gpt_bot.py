import openai
from aiogram import types, Dispatcher
from create_bot import bot, disp
# import telegram
# from telegram.ext import Updater, CommandHandler


#@disp.message_handler()
async def send(Mes : types.Message):
    chat_id = Mes.chat.id
    await bot.send_chat_action(chat_id, "typing")
    wait_message = await Mes.answer("🕐Подождите я загружаю ответ...")

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=Mes.text,
    temperature=0.5,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    #stop=["You:"]
    )
    await bot.delete_message(chat_id, wait_message.message_id)

    answer_text = response['choices'][0]['text']
    max_message_length = 1000
    # del answer
    answer_parts = [answer_text[i:i + max_message_length] for i in range(0, len(answer_text), max_message_length)]
    # send answer
    for answer_part in answer_parts:
        await Mes.answer(answer_part)


def register_hendlers_gptbot(disp: Dispatcher):
    disp.register_message_handler(send)
