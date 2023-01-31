import io 

from aiogram import types 
from aiogram.dispatcher.filters import Command 

from filters import isGroup 
from filters.admins import AdminFilter

from loader import dp, bot


@dp.message_handler(isGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    sourse_message = message.reply_to_message
    photo = sourse_message.photo[-1]
    photo = await photo.download(destination = io.BytesIO())
    input_file = types.InputFile(photo)
    
    await message.chat.set_photo(photo = input_file )
    
    
@dp.message_handler(isGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    sourse_message = message.reply_to_message
    title = sourse_message.text 
    await bot.set_chat_title(message.chat.id, title=title)
    