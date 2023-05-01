from aiogram import Bot, Dispatcher, executor, types
import logging

TOKEN = '6163554865:AAETTqqma8B-xmYbS-m7DYquNVXZP6vdl9o'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

buttons = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='one'),
            types.KeyboardButton(text='two'),
        ]
    ],resize_keyboard=True,
)

inlineMenu = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='one',callback_data='1'),
            types.InlineKeyboardButton(text='two', callback_data='2'),
        ]
    ]
)
@dp.message_handler(commands = ["start",'salom'])
async def send_welcome(massage: types.Message):
    await massage.reply('WElcome')

@dp.message_handler(commands = ['test'])
async def send_test(massage: types.Message):
    await massage.answer('Tanlang: ', reply_markup=inlineMenu)
    

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)