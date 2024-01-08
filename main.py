import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, Message, ReplyKeyboardRemove
from aiogram import types
from dotenv import load_dotenv


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

text = '1234567'
button1 = KeyboardButton(text='Создать заявку')
button2 = KeyboardButton(text='На согласовании')
button3 = KeyboardButton(text='Отклоненные')

button4 = InlineKeyboardButton(text='Да', callback_data='yes')
button5 = InlineKeyboardButton(text='Нет', callback_data='no')

button6 = InlineKeyboardButton(text='Назад', callback_data='cancel')

keyboard_1 = ReplyKeyboardMarkup(keyboard=[[button1],
                                         [button2],
                                         [button3]])

keyboard_2 = InlineKeyboardMarkup(inline_keyboard=[[button4], [button5]])

@dp.message(Command(commands=['start']))
async def cmd_start(message: types.Message):
    await message.answer(f'Введите идентификатор')

@dp.message(F.text == '1234567')
async def cmd_start_answer(message: types.Message):
    if text == '1234567':
        await message.answer(f'Добрый день, {message.from_user.full_name}. Выберите действия:',reply_markup=keyboard_1)

@dp.message(F.text == 'Создать заявку')
async def process_create(message: types.Message):
    await message.answer(text='Напишите заголовок')

@dp.message(F.text == 'Заголовок')
async def process_create_1(message: types.Message):
    await message.answer(text='Введите ваш запрос',)

@dp.message(F.text == 'Запрос')
async def process_create_2(message: types.Message):
    await message.answer(text='Вы ввели полный список или хотите его дополнить ?', reply_markup=keyboard_2)

@dp.callback_query(F.data == 'yes')
async def process_yes_kb(callback: CallbackQuery):





if __name__ == '__main__':
    dp.run_polling(bot)