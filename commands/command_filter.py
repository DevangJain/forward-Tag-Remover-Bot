from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ParseMode
import os

source="https://t.me/DevangJain"
START_TEXT="Hi [{}](tg://user?id={})\nI am A Forward Tag remover Bot which is created by @DevangJain.Send /help To Know What I Can Do"
HELP_TEXT="Forward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media"

#Inline Keyboard Button
keyboard = [
[
 InlineKeyboardButton("My Developer 🖥️", url=source)
],
reply_markup = InlineKeyboardMarkup(keyboard)

#Start Message
def start_text(u,c):
 u.message.reply_text(START_TEXT.format(u.message.from_user.full_name,u.message.chat.id),reply_markup=reply_markup,
parse_mode=ParseMode.MARKDOWN)

#Help Message
def help_text(u,c):
  u.message.reply_text(HELP_TEXT,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)
