import model
import view
import menu
import validator



# model.read_db('7A.txt')  # для быстрого теста открыть ком


def input_handler(inp: int):
    match inp:
        case 1:
            pass


def start():
    while True:
        print()
        user_inp = view.menu(menu.main_menu(), '\nГлавное меню')
        input_handler(user_inp)
