from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from random import randint
import time
import calc

total = 0
coin = 0

RULES = """ Правила игры конфеты: Для начала устанавливается общее количество конфет (можно выбрать рекомендуемое 150)
после определяют кто будет ходить первым, игрок подкидывает монетку выбрав орел или решка (команды /Orel или /Reshka), 
и дальше участники игры берут с кона конфеты (просто вводите в чат число), 
можно брать от 1й до 28 конфет, кто последним заберет оставшиеся конфеты, побеждает!
"""


@dp.message_handler(commands=['calc'])
async def phrase_calc_start(message: types.Message):
    print(message.text)
    if ':' in message.text.split()[1]:
        temp = message.text.split()[1].replace(':', '/')
    else:
        temp = message.text.split()[1]
    calculate = round(calc.phrase_calc(temp), 2)
    await message.answer(f'Результат выражения = {calculate}')


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    print(message.text)
    end()  # Обнуляет Total и Coin
    await message.answer(f'Привет {message.from_user.first_name} Мы будем играть с тобой в конфетки\n')
    time.sleep(0.3)
    await message.answer(text=RULES)
    time.sleep(0.3)
    await message.answer('Введи "/set количество" конфет на кону в игре '
                         'или нажми сюда для 150 конфет по умолчанию "/set_150"')


@dp.message_handler(commands=['help'])
async def help_start(message: types.Message):
    print(message.text)
    await message.answer(f'Приветствую {message.from_user.first_name}!')
    time.sleep(0.5)
    await message.answer(f'Для просмотра инструкций к игре введите /start\n'
                         f'Так же можно закончить игру с помощью /end\n'
                         f'и если уже очень хочется подсмотреть сколько осталось на кону - /get_total\n'
                         f'А еще можно посчитать в калькуляторе выражений - /calc')


@dp.message_handler(commands=['set'])
async def set_total(message: types.Message):
    print(message.text)
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Установленно количество конфет = {total}')
    await message.answer(f'Теперь подбрось монетку, выбери "/Orel" - Орел или "/Reshka" - Решка')
    await message.delete()


@dp.message_handler(commands=['set_150'])
async def set_total_150(message: types.Message):
    print(message.text)
    global total
    total = 150
    await message.answer(f'Установленно количество конфет = {total}')
    await message.answer(f'Теперь подбросим монетку, выбери "/Orel" - Орел или "/Reshka" - Решка')
    await message.delete()


@dp.message_handler(commands=['end'])
async def end_game(message: types.Message):
    print(message.text)
    end()
    await message.answer(f'Игра завершена, или можно начать сначала, нажми /start')


@dp.message_handler(commands=['get_total'])
async def get_total_candys(message: types.Message):
    print(message.text)
    await message.answer(f'Вот хитрец!!!! ладно, на кону осталось {get_total()} конфет.')
    await message.delete()


@dp.message_handler(commands=['Orel'])
async def coin_O_choice(message: types.Message):
    print(message.text)
    global total
    global coin
    if total != 0:
        await message.answer(f'{message.from_user.first_name} выбрал "Орел!"')
        coin = randint(1, 2)
        match coin:
            case 1:
                await message.answer('Выпал "Орел"!')
            case 2:
                await message.answer('Выпала "Решка"!')
        match message.text:
            case '/Orel':
                if coin == 1:
                    mes = f'Первым ходит {message.from_user.first_name}\n' \
                          f'Бери конфеты'
                    await message.answer(mes)
                else:
                    bot_pick = bot_turn()
                    await message.answer('Первым ходит бот! ')
                    await message.answer(f'Бот берет {bot_pick} конфет')
                    await message.answer('Ваш ход, берите конфеты')
            case _:
                pass
    else:
        await message.answer('Сначала задайте количество конфет')


@dp.message_handler(commands=['Reshka'])
async def coin_P_choice(message: types.Message):
    print(message.text)
    global total
    global coin
    if total != 0:
        await message.answer(f'{message.from_user.first_name} выбрал "Решка!"')
        coin = randint(1, 2)
        match coin:
            case 1:
                await message.answer('Выпал "Орел"!')
            case 2:
                await message.answer('Выпала "Решка"!')
        match message.text:
            case '/Reshka':
                if coin == 2:
                    mes = f'Первым ходит {message.from_user.first_name}\n' \
                          f'Бери конфеты'
                    await message.answer(mes)
                else:
                    bot_pick = bot_turn()
                    await message.answer('Первым ходит бот! ')
                    await message.answer(f'Бот берет {bot_pick} конфет')
                    await message.answer('Ваш ход, берите конфеты')
            case _:
                pass
    else:
        await message.answer('Сначала задайте количество конфет')


@dp.message_handler(text=['Привет'])
async def mes_hi(message: types.Message):
    if message.text.lower() == 'привет':
        await message.answer(f'Привет! Хочешь поиграть в конфетки? Введи /start')


@dp.message_handler()
async def mes_all(message: types.Message):
    print(message.text)
    if message.text.isdigit() or message.text.replace('-', '').isdigit():
        global total
        global coin
        player_name = message['from']['first_name']
        if total == 0:
            mes = 'Вы не выбрали максимальное количество конфет'
            await message.answer(mes)
        if coin == 0:
            mes = 'Вы не подкинули монетку'
            await message.answer(mes)
        else:
            player_get = int(message.text)
            if player_get > 28 or player_get < 1:
                mes = 'По правилам игры можно брать только от 1й до 28 конфет '
                await message.answer(mes)
            else:
                total -= player_get
                mes = win(player_get, player_name, 'Бот')
                await message.answer(mes)
                if total > 29:
                    bot = bot_turn()
                    mes = win(bot, 'Бот', player_name)
                    await message.answer(mes)
        await message.answer(f'Осталось конфет {get_total()}')  # <-- Вот эту строку открыл для отображения конфет
    else:
        await message.answer(f'{message.from_user.full_name}, для того чтобы взять конфеты с кона '
                             f'введи количество без букв')


def get_total():
    global total
    return total


def win(get: int, player_name: str, opponent_name: str):
    global total
    global coin
    mes = ''
    temp = randint(1, 28)
    if total > 29:
        mes = f'{player_name} взял {get} конфет '
    elif total == 29:
        mes = f'{player_name} Выиграл!!!\nСколько бы не взял {opponent_name}, например {temp} конфет\n' \
              f'{player_name} забирает оставшиеся {total - temp} и побеждает'
        end()
    elif total <= 28:
        mes = f'{player_name} берет {get} конфет\n{opponent_name} Выиграл, забрав последние {total} конфет'
        end()
    return mes


def bot_turn():
    global total
    time.sleep(1)
    if total % 29 == 0:
        bot = randint(1, 28)
    else:
        bot = total % 29
    total -= bot
    return bot


def end():
    global total
    global coin
    total = 0
    coin = 0
