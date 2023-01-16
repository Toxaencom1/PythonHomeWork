# Создайте программу для игры в 'Крестики-нолики'.
# НЕОБЯЗАТЕЛЬНО: Добавить игру против бота с интеллектом.
from functions import *

#Режим только против второго игрока ((

def main_game():
    while True:
        insert_symbol_in_cell('X', cells)
        desk_print(cells)
        end_game = check_winner(cells)
        if not end_game:
            print(f'Игрок X победил!')
            break
        insert_symbol_in_cell('0', cells)
        desk_print(cells)
        end_game = check_winner(cells)
        if not end_game:
            print(f'Игрок 0 победил!')
            break


cells = [7, 8, 9, 4, 5, 6, 1, 2, 3]
desk_print(cells)
print('Подкинем монетку, игроки определитесь с выбором!')
input('Нажмите Enter для продолжения...')
print('X ', end='')
coin = coin_catch()
main_game()
