from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

inline_button_der = InlineKeyboardButton('Der', callback_data='der')
inline_button_die = InlineKeyboardButton('Die', callback_data='die')
inline_button_das = InlineKeyboardButton('Das', callback_data='das')
inline_kb = InlineKeyboardMarkup()
inline_kb.add(inline_button_der,inline_button_das,inline_button_die)
