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
    print(f'ходит первым - {coin_side}')
    return choice


def player_turn(candy, player1_name):
    print(f'{player1_name}, возьмите конфеты: ')
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


def winning_logic_process(player1, player1_name, player2, player2_name, candy, coin):
    count = 1  # Декоративный
    while candy > 29:
        print(f'Ход №{count}')
        if coin == 1:
            candy = player1(candy, player1_name)
            if candy == 29:
                candy = player2(candy, player2_name)
                print(f'{player1_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
            elif candy < 29:
                print(f'{player2_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
            candy = player2(candy, player2_name)
            if candy == 29:
                candy = player1(candy, player1_name)
                print(f'{player2_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
            elif candy < 29:
                print(f'{player1_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
        if coin == 2:
            candy = player2(candy, player2_name)
            if candy == 29:
                candy = player1(candy, player1_name)
                print(f'{player2_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
            elif candy < 29:
                print(f'{player1_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
            candy = player1(candy, player1_name)
            if candy == 29:
                candy = player2(candy, player2_name)
                print(f'{player1_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
            elif candy < 29:
                print(f'{player2_name} забирает оставшиеся {candy} конфет и побеждает!')
                break
        count += 1

# Functions for first task "end"
# ==============================================================================================================
# Functions for second task

def validate_input(symbol):
    while True:
        try:
            cell = int(input(f'Игрок {symbol} - Введите номер клетки: '))
            if cell >= 1 and cell <= 9:
                return cell
            else:
                print('Можно взять только от 1 до 9и')
        except ValueError:
            print('Возьмите от 1 до 9, а не то что вы написали')


def desk_print(desk):
    print('=========================')
    for i in range(len(desk)):
        if i == 3 or i == 6 or i == 9:
            print('\n-------------------------')
        print(f'|\t{desk[i]}\t', end='|')
    print('\n=========================')


# def insert_symbol_in_cell(symbol,cells):  # Функция для игры глупых ботов
#     while True:  # Раскомментируйте этот метод и закомментируйте метод ниже с таким же названием
#         time.sleep(1)
#         input_value = randint(1,9)
#         if input_value not in cells:
#             continue
#         for i in range(len(cells)):
#             if cells[i] == input_value:
#                 cells[i] = symbol
#                 break
#         break

def insert_symbol_in_cell(symbol,cells):  # вот этот
    while True:
        input_value = validate_input(symbol)
        if input_value not in cells:
            print('Тут уже занято')
            continue
        for i in range(len(cells)):
            if cells[i] == input_value:
                cells[i] = symbol
                break
        break



def check_winner(cells):
    if cells[0] == cells[1] == cells[2] or \
            cells[3] == cells[4] == cells[5] or \
            cells[6] == cells[7] == cells[8] or \
            cells[0] == cells[3] == cells[6] or \
            cells[1] == cells[4] == cells[7] or \
            cells[2] == cells[5] == cells[8] or \
            cells[0] == cells[4] == cells[8] or \
            cells[6] == cells[4] == cells[2]:
        return False
    return True

# Functions for second task "end"
# ==============================================================================================================