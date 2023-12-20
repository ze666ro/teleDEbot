from aiogram import types
from .app import dp
from .keybords import inline_kb

@dp.message_handler(commands='train_ten')
async def train_ten(message: types.Message):
    await message.reply('pipiska',reply_markup=inline_kb)