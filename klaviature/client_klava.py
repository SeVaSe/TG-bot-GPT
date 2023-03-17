from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import types, Dispatcher
from create_bot import disp, bot
import telebot

from telebot import types


b1 = KeyboardButton('/О_боте')
b2 = KeyboardButton('/Эксплуатация')
b3 = KeyboardButton('/Обратная_связь')

kl_client = ReplyKeyboardMarkup(resize_keyboard=True)
kl_client.row(b1, b2)
kl_client.add(b3)















