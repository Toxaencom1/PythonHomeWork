# Создайте программу для игры в 'Крестики-нолики'.
# НЕОБЯЗАТЕЛЬНО: Добавить игру против бота с интеллектом.

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


def insert_symbol_in_cell(symbol):
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


def main_game():
    while True:
        insert_symbol_in_cell('X')
        desk_print(cells)
        end_game = check_winner(cells)
        if not end_game:
            print(f'Игрок X победил!')
            break
        insert_symbol_in_cell('0')
        desk_print(cells)
        end_game = check_winner(cells)
        if not end_game:
            print(f'Игрок 0 победил!')
            break


cells = [7, 8, 9, 4, 5, 6, 1, 2, 3]
desk_print(cells)
main_game()
