from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, Message, ReplyKeyboardRemove


def start() -> InlineKeyboardMarkup:
    button = [
        [InlineKeyboardButton(text='1. Создать заявку', callback_data='create')],
        [InlineKeyboardButton(text='2. На согласовании', callback_data='accept')],
        [InlineKeyboardButton(text='3. Отклоненные', callback_data='reject')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


def yes_and_no() -> InlineKeyboardMarkup:
    button = [
        [InlineKeyboardButton(text='Да', callback_data='yes'),
         InlineKeyboardButton(text='Нет', callback_data='no')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


def cancel() -> InlineKeyboardMarkup:
    button = [
        InlineKeyboardButton(text='Назад', callback_data='cancel')
    ]


def object() -> InlineKeyboardMarkup:
    button = [
        [InlineKeyboardButton(text='1. АртСити', callback_data='artcity')],
        [InlineKeyboardButton(text='2. Батареон', callback_data='batareon')],
        [InlineKeyboardButton(text='3. Статум', callback_data='statum')],
        [InlineKeyboardButton(text='4. Уно', callback_data='uno')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard