import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, PhotoSize)
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, Message, ReplyKeyboardRemove
from aiogram import types
from dotenv import load_dotenv


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


object1 = 'АртСити'
object2 = 'Батареон'
object3 = 'Статум'
object4 = 'Уно'


text = '1234567'
button1 = KeyboardButton(text='1.Создать заявку')
button2 = KeyboardButton(text='2.На согласовании')
button3 = KeyboardButton(text='3.Отклоненные')

button4 = InlineKeyboardButton(text='Да', callback_data='yes')
button5 = InlineKeyboardButton(text='Нет', callback_data='no')

button6 = InlineKeyboardButton(text='Назад', callback_data='cancel')

button7 = InlineKeyboardButton(text=object1, callback_data='1.artcity')
button8 = InlineKeyboardButton(text=object2, callback_data='2.batareon')
button9 = InlineKeyboardButton(text=object3, callback_data='3.statum')
button10 = InlineKeyboardButton(text=object4, callback_data='4.uno')

keyboard_1 = ReplyKeyboardMarkup(keyboard=[[button1],
                                         [button2],
                                         [button3]])

keyboard_2 = InlineKeyboardMarkup(inline_keyboard=[[button4, button5]])

keyboard_3 = InlineKeyboardMarkup(inline_keyboard=[[button7],
                                                   [button8],
                                                   [button9],
                                                   [button10]])


@dp.message(Command(commands=['start']))
async def cmd_start(message: types.Message):
    await message.answer(f'Введите идентификатор')

@dp.message(F.text == '1234567')
async def cmd_start_answer(message: types.Message):
    if text == '1234567':
        await message.answer(f'Добрый день, {message.from_user.full_name}. Выберите действия:',reply_markup=keyboard_1)

@dp.message(Command(commands='logic'), StateFilter(default_state)) #handler keyboard add object
async def start_logic(message: Message, state: FSMContext):
    await message.answer(text='Выберите объект:',reply_markup=keyboard_3)
    #button7 = InlineKeyboardButton(text=object1, callback_data='1.artcity')
    #button8 = InlineKeyboardButton(text=object2, callback_data='2.batareon')
    #button9 = InlineKeyboardButton(text=object3, callback_data='3.statum')
    #button10 = InlineKeyboardButton(text=object4, callback_data='4.uno')
    #keyboard: list[list[InlineKeyboardButton]] = [[button7],
                                                   #[button8],
                                                   #[button9],
                                                   #[button10]]
    await state.set_state(FSMlogic.object_all)
@dp.message(StateFilter(FSMlogic.title),F.data.in_(['artcity','batareon','statum','uno']))#hanlder add data next object (request, accepted, denied)
async def start_title(callback: CallbackQuery, state: FSMContext):
    await state.update_data(object=callback.data)
    await callback.message.answer(text='Пожалуйста, введите ваш заголовок:')
    await state.set_state(FSMlogic.title)

@dp.message(StateFilter(FSMlogic.request))
async def start_request(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer(text='Пожалуйста, введите ваш запрос:')
    await state.set_state(FSMlogic.request)

#@dp.message(F.text == )
#async def process_create(message: types.Message):
#    await message.answer(text='Напишите заголовок')

#@dp.message(F.text == 'Заголовок')
#async def process_create_1(message: types.Message):
#    await message.answer(text='Введите ваш запрос',)

#@dp.message(F.text == 'Запрос')

@dp.callback_query(StateFilter(FSMlogic.finish))
async def process_finish_test(callback: CallbackQuery, state: FSMContext):
    await state.update_data(request=callback.data == text)
    await callback.message.edit_text(text='Вы ввели полный список или хотите его дополнить ?', reply_markup=keyboard_2)
    user_dict[callback.from_user.id] = await state.get_data()
    await state.clear()
    await callback.message.answer(text='Для просмотра введеного вами запроса введите /show')

@dp.callback_query(F.data == 'yes')
async def process_button_1_press(callback: CallbackQuery):
    await callback.answer(text='Заявка отправлена.',show_alert=True)

dp.message(Command(commands='show'), StateFilter(default_state))
async def process_show_data(message: Message):
    if message.from_user.id in user_dict:
        await message.answer(
            caption = f'Ваш объект: {user_dict[message.from_user.id]["object"]}\n'
                      f'Ваш заголовок: {user_dict[message.from_user.id]["title"]}\n'
                      f'Ваш запрос: {user_dict[message.from_user.id]["request"]}\n'
        )
    else:
        await message.answer(text='Ваш запрос ещё не создан')







#@dp.message(StateFilter(FSMlogic.finish))
#async def process_finish(message: types.Message, state: FSMContext):
#    await state.update_data(request=message.text)
#    await message.answer(text='Вы ввели полный список или хотите его дополнить ?', reply_markup=keyboard_2)








if __name__ == '__main__':
    dp.run_polling(bot)