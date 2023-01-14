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


def validate_pick_candys(player_number: int):
    while True:
        try:
            candys = int(input(f"Игрок №{player_number}, бери конфеты: "))
            if candys >= 1 and candys <= 28:
                break
            else:
                print('Можно взять только от одной до 28и конфет')
        except:
            print('Возьмите от 1й до 28 конфет а не то что вы написали')
    return candys


def next_turn(candys):
    print('\nСледующий ход')
    player1 = validate_pick_candys(1)
    candys -= player1
    if candys < 28:
        print(f"Осталось конфет: {candys}")
        print(f'Игрок №2 - Выиграл')
        return candys
    print(f"Осталось конфет: {candys}")
    player2 = validate_pick_candys(2)
    candys -= player2
    if candys < 28:
        print(f"Осталось конфет: {candys}")
        print(f'Игрок №1 - Выиграл')
        return candys
    print(f"Осталось конфет: {candys}")
    return candys


# =====================================================================================================================

print("Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n\
За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n")

print('Подкинем монетку, игроки определитесь с выбором!')

input('Нажмите Enter для продолжения')
coin = randint(1, 2)
match coin:
    case 1:
        coin = 'Орел'
        print(coin)
    case 2:
        coin = 'Решка'
        print(coin)
print(f'Игрок №1 - {coin}')

max_candys = validate_max_candys()

while True:
    if max_candys > 28:
        max_candys = next_turn(max_candys)
    else:
        print(f"Он забирает конфет: {max_candys}")
        print('И все остальные!')
        break
