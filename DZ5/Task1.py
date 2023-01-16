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
from functions import *


def main():
    print("Условия: Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n\
        За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n")
    player1_name = input("Введите имя первого игрока: ")
    bot_name = '\"Умный бот\"'
    vs = validate_vs_choice_input()

    player2_name = input('Введите имя второго игрока: ') if vs == 1 else 'second player'
    print('Подкинем монетку, игроки определитесь с выбором!')
    player_choice = validate_player_choice_input()

    coin = coin_catch()
    coin = 1 if player_choice == coin else 2

    max_candys = validate_max_candys_input()

    match vs:
        case 1:
            winning_logic_process(player_turn, player1_name, player_turn, player2_name, max_candys, coin)
        case 2:
            winning_logic_process(player_turn, player1_name, bot_turn, bot_name, max_candys, coin)


if __name__ == '__main__':
    main()
