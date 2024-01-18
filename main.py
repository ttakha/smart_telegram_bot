import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message)
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, Message, ReplyKeyboardRemove
from aiogram import types
from dotenv import load_dotenv
from keyboard import start, yes_and_no, cancel, object

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)
storage = MemoryStorage()

user_dict: dict[int, dict[str, str | int | bool]] = {}

class FSMlogic(StatesGroup):
    object_all = State()
    title = State()
    request = State()
    finish = State()

text = '1234567'

@dp.message(Command(commands=['start']))
async def cmd_start(message: types.Message):
    await message.answer(f'Введите идентификатор')

@dp.message(F.text == '1234567')
async def cmd_start_answer(message: types.Message):
    if text == '1234567':
        await message.answer(f'Добрый день, {message.from_user.full_name}. Выберите действия:', reply_markup=start())

@dp.callback_query(F.data == 'create')
async def command_object(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите объект:', reply_markup=object())

@dp.callback_query(F.data.in_({'artcity','batareon','statum','uno'}))
async def start_title(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Пожалуйста, введите ваш заголовок:')

@dp.callback_query()
async def start_request(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Пожалуйста, введите ваш запрос:')

@dp.callback_query()
async def process_finish_test(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Вы ввели полный список или хотите его дополнить ?', reply_markup=yes_and_no())
    await state.clear()

@dp.callback_query(F.data == 'yes')
async def process_button_1_press(callback: CallbackQuery):
    await callback.answer(text='Заявка отправлена.', show_alert=True)


if __name__ == '__main__':
    dp.run_polling(bot)