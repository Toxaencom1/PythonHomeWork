from random import randint
import time


# Functions for first task
# ==============================================================================================================


def validate_max_candys_input():
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


def validate_pick_candy_input():
    while True:
        try:
            candy = int(input())
            if candy >= 1 and candy <= 28:
                break
            else:
                print('Можно взять только от одной до 28и конфет')
        except:
            print('Возьмите от 1й до 28 конфет а не то что вы написали')
    return candy


def validate_player_choice_input():
    while True:
        try:
            choice = int(input("Игрок 1 выберите вашу сторону монеты\n\
            Введите число где 1 - Орел, 2 - Решка: "))
            if choice >= 1 and choice <= 2:
                break
            else:
                print('Можно взять 1 - Орел или 2 - Решка:')
        except:
            print('Можно взять 1 - Орел или 2 - Решка, а не то что вы написали')
    return choice


def validate_vs_choice_input():
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


def first_player_turn(candy, player1_name):
    print(f'{player1_name}, возьмите конфеты: ')
    player1 = validate_pick_candy_input()
    candy -= player1
    print(f"Осталось конфет: {candy}")
    return candy


def second_player_turn(candy, player2_name):
    print(f'{player2_name}, возьмите конфеты: ')
    player1 = validate_pick_candy_input()
    candy -= player1
    print(f"Осталось конфет: {candy}")
    return candy


def bot_turn(candy, bot_name):
    time.sleep(1)
    if candy % 29 == 0:
        treatment = randint(1, 28)
    else:
        treatment = candy % 29
    bot_choice = treatment
    print(f'{bot_name} берет {bot_choice} конфет')
    candy -= bot_choice
    print(f"Осталось конфет: {candy}")
    return candy
# Functions for first task "end"
# ==============================================================================================================
