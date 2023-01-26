import validator
from validator import emergency_exit


def menu(menu_list: list, string_: str):
    print(string_)
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    user_input = validator.v_player_choice(input('Введи команду : '), 1, len(menu_list))
    return user_input


def show_all(class_list: list, subject: str):
    print('\nid =================Journal=======================')
    print('    ====*Фамилия*====*Имя*====*Оценки*============')
    for i in class_list:
        for subj, stud in i.items():
            if subj == subject:
                print(subj)
                for j in stud:
                    for ident, stu in j.items():
                        for f_i, marks in stu.items():
                            print(f'{ident}   {f_i:24}: {", ".join(marks)}')
    print('==================================================\n')


def which_one(string_: str, max_students: int) -> int:
    print(string_)
    looser = int(validator.v_player_choice(input('(Выбирайте по ID ученика): '), 1, max_students))
    return looser


def estimate(string_: str) -> int:
    print(string_)
    mark = int(validator.v_player_choice(input('От 1го до 5: '), 1, 5))
    return mark


def exit_programm():
    print('\nЗавершение программы.\n')
    exit()


def string_input(string_: str) -> str:
    record = emergency_exit(input(string_))
    if '.txt' in record:
        return record
    else:
        record = record + '.txt'
        return record

def f_i_input(string_: str) -> str:
    record = emergency_exit(input(string_))
    return record