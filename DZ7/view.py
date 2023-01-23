import validator
from validator import emergency_exit


def menu(menu_list: list, string_: str):
    print(string_)
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    user_input = validator.v_player_choice(input('Введи команду : '), 1, len(menu_list))
    return user_input


def show_all(db: list):
    print('\nВот, что нашел:\nid ======================Contact=============================')
    print('    ====*Фамилия*====*Имя*====*Телефон*====*Комментарий*====')
    if db_success(db):
        for i in db:
            for key, value in i.items():
                print(f"{key}\t-", end='\t')
                for k, v in value.items():
                    print(f" {v} ", end='')
                else:
                    print()
        else:
            print('=============================================================')


def db_success(db: list):
    if db:
        return True
    else:
        print('\nТут пусто, возможно вам нужно открыть другую базу данных')
        return False


def which_one(string_: str) -> int:
    print(string_)
    looser = int(validator.v_player_choice(input('Введите номер контакта из базы: '), 1, 200))
    return looser


def exit_programm():
    print('\nЗавершение программы.\n')
    exit()


def create_contact() -> str:
    print('\nСоздание нового контакта')
    lastname = emergency_exit(input('    Введите Фамилию >: '))
    firstname = emergency_exit(input('    Введите Имя >: '))
    phone = emergency_exit(input('    Введите телефон >: '))
    comment = emergency_exit(input('    Введите комментарий >: '))
    new_contact = f'{lastname};{firstname};{phone};{comment}'
    return new_contact


def string_input(string_: str) -> str:
    record = emergency_exit(input(string_))
    return record
