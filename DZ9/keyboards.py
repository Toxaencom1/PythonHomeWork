from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help_menu_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

help_menu_kb.add(KeyboardButton('/start'), KeyboardButton('/end'), KeyboardButton('/get_total'),
                 KeyboardButton('/calc'))

start_menu_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

start_menu_kb.add(KeyboardButton('/help'), KeyboardButton('/150'))

set_menu_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

set_menu_kb.add(KeyboardButton('/Орел'), KeyboardButton('/Решка'))

pick_candys_kb = ReplyKeyboardMarkup(resize_keyboard=True)

pick_candys_kb.row(KeyboardButton('1'), KeyboardButton('2'), KeyboardButton('3'),
                   KeyboardButton('4'), KeyboardButton('5'), KeyboardButton('6'),
                   KeyboardButton('7'), )
pick_candys_kb.row(KeyboardButton('8'), KeyboardButton('9'), KeyboardButton('10'),
                   KeyboardButton('11'), KeyboardButton('12'), KeyboardButton('13'),
                   KeyboardButton('14'), )
pick_candys_kb.row(KeyboardButton('15'), KeyboardButton('16'), KeyboardButton('17'),
                   KeyboardButton('18'), KeyboardButton('19'), KeyboardButton('20'),
                   KeyboardButton('21'), )
pick_candys_kb.row(KeyboardButton('22'), KeyboardButton('23'), KeyboardButton('24'),
                   KeyboardButton('25'), KeyboardButton('26'), KeyboardButton('27'),
                   KeyboardButton('28'), )
pick_candys_kb.insert(KeyboardButton('/end'))
