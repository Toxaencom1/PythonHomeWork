# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота 'интеллектом'

from random import randint
import time


def coin_catch():
    coin_side = randint(1, 2)
    choice = coin_side
    match coin_side:
        case 1:
            coin_side = 'Орел'
        case 2:
            coin_side = 'Решка'
    print(f'Первым ходит - {coin_side}')
    return choice


def validate_max_candys():
    while True:
        try:
            max_candys = int(input("Сколько конфет в игре?: "))
            if max_candys >= 100:
                break
            else:
                print('Введите больше 100, а то игра будет не корректной')
        except:
            print('Введите число больше 100, а не то, что вы написали')
    return max_candys


def validate_pick_candy(player_number: int):
    while True:
        try:
            candy = int(input(f"Игрок №{player_number}, бери конфеты: "))
            if candy >= 1 and candy <= 28:
                break
            else:
                print('Можно взять только от одной до 28и конфет')
        except:
            print('Возьмите от 1й до 28 конфет а не то что вы написали')
    return candy


def validate_player_choice():
    while True:
        try:
            choice = int(input("Введите число где 1 - Орел, 2 - Решка: "))
            if choice >= 1 and choice <= 2:
                break
            else:
                print('Можно взять 1 - Орел или 2 - Решка:')
        except:
            print('Можно взять 1 - Орел или 2 - Решка, а не то что вы написали')
    return choice

def validate_vs_choice():
    while True:
        try:
            choice = int(input("Введите число где 1 - против игрока 2 - против Бота: "))
            if choice >= 1 and choice <= 2:
                break
            else:
                print('Можно взять 1 - против игрока 2 - против Бота:')
        except:
            print('1 - против игрока 2 - против Бота, а не то что вы написали')
    return choice


def next_turn_PvP(candy):
    print('\nСледующий ход')
    player1 = validate_pick_candy(1)
    candy -= player1
    if candy < 28:
        print(f"Осталось конфет: {candy}")
        print(f'Игрок №2 - Выиграл')
        return candy
    print(f"Осталось конфет: {candy}")
    player2 = validate_pick_candy(2)
    candy -= player2
    if candy < 28:
        print(f"Осталось конфет: {candy}")
        print(f'Игрок №1 - Выиграл')
        return candy
    print(f"Осталось конфет: {candy}")
    return candy


def first_player_turn(candy):
    player1 = validate_pick_candy(1)
    candy -= player1
    print(f"Осталось конфет: {candy}")
    return candy

def second_player_turn(candy):
    player1 = validate_pick_candy(2)
    candy -= player1
    print(f"Осталось конфет: {candy}")
    return candy


def bot_turn(candy):
    time.sleep(1)
    if max_candys % 29 == 0:
        treatment = randint(1,28)
    else:
        treatment = max_candys % 29
    bot_choice = treatment
    print(f'ИИ берет {bot_choice} конфет')
    candy -= bot_choice
    print(f"Осталось конфет: {candy}")
    return candy


# =====================================================================================================================
# vs = validate_vs_choice()


print("Условия: Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n\
За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n")


print('Подкинем монетку, игроки определитесь с выбором!')

# input('Нажмите Enter для продолжения')

player_choice = validate_player_choice()
coin = coin_catch()
coin = 1 if player_choice == coin else 2

max_candys = validate_max_candys()
count = 1

while max_candys > 30:
    print(f'Ход №{count}')
    if coin == 1:
        max_candys = first_player_turn(max_candys)
        if max_candys == 29:
            max_candys = bot_turn(max_candys)
            print(f'Игрок забирает оставшиеся {max_candys} конфет и побеждает!')
            break
        elif max_candys < 29:
            print(f'Бот забирает оставшиеся {max_candys} конфет и побеждает!')
            break
        max_candys = bot_turn(max_candys)
        if max_candys == 29:
            max_candys = first_player_turn(max_candys)
            print(f'Бои забирает оставшиеся {max_candys} конфет и побеждает!')
            break
        elif max_candys < 29:
            print(f'Игрок забирает оставшиеся {max_candys} конфет и побеждает!')
            break
    elif coin == 2:
        max_candys = bot_turn(max_candys)
        if max_candys == 29:
            max_candys = first_player_turn(max_candys)
            print(f'Бои забирает оставшиеся {max_candys} конфет и побеждает!')
            break
        elif max_candys < 29:
            print(f'Игрок забирает оставшиеся {max_candys} конфет и побеждает!')
            break
        max_candys = first_player_turn(max_candys)
        if max_candys == 29:
            max_candys = bot_turn(max_candys)
            print(f'Игрок забирает оставшиеся {max_candys} конфет и побеждает!')
            break
        elif max_candys < 29:
            print(f'Бот забирает оставшиеся {max_candys} конфет и побеждает!')
            break
    count += 1
