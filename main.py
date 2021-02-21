# Import
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

postchannelid = input("Введите id группы/канала/чата: ")

# /post message - Example - /post Hello world!
@dp.message_handler(commands=["post"])
async def post(message: types.Message):
    post = message.get_args()
    buttons = InlineKeyboardMarkup(row_wight=1)
    buttons.add(InlineKeyboardButton("♥ 0", callback_data="like"))
    await bot.send_message(postchannelid, f"{post}", reply_markup=buttons, parse_mode= "Markdown")

@dp.callback_query_handler(text="like")
async def like(callback: types.CallbackQuery):
    await callback.answer(text="Вы проголосовали!", show_alert=False)
    message = callback.message
    temp = message.reply_markup["inline_keyboard"][0][0]["text"].split("♥ ")[1]
    buttons = InlineKeyboardMarkup(row_wight=1)
    buttons.add(InlineKeyboardButton("♥ " + str(int(temp) +1), callback_data="like"))
    await bot.edit_message_text(
        chat_id= message.chat.id,
        message_id = message.message_id,
        text= message.text,
        reply_markup=buttons
    )

executor.start_polling(dp)