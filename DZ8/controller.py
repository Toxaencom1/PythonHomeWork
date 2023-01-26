import model as m
import view as v
import menu
import validator


subj_names = m.get_subjects_names_list()


def input_handler(inp: int):
    global subj_names
    class_path = ''
    match inp:
        case 1:
            subj_menu_choice = v.menu(subj_names, '\nВыберите предмет')
            print(len(m.get_subjects_names_list()))
            if not subj_menu_choice == len(m.get_subjects_names_list()):
                class_choice = v.menu(menu.class_menu(), '\nВыберите Класс учащихся')
                if class_choice == 3:
                    class_path = v.string_input('\nВведите название файла\n'
                                                'Файл должен быть Цифра_класса+Большая_Буква_класса.txt '
                                                'и в корне папки, \n'
                                                'писать без расширения\n'
                                                'Формат - "предмет:Фамилия Имя%оценки;Фамилия Имя%оценки; итд" \n:>')
                    print(class_path)
                    bd_class = m.read_class_list(m.class_choice(class_choice,class_path))
                else:
                    bd_class = m.read_class_list(m.class_choice(class_choice))
                flag = True
                while flag:
                    v.show_all(bd_class, m.subj_choice(subj_menu_choice))
                    who_working = v.which_one('\nКому дать задание?')
                    evaluation = v.estimate('\nКакую оценку дать??')
                    m.set_student_mark(subj_menu_choice, who_working, evaluation)
                    v.show_all(bd_class, m.subj_choice(subj_menu_choice))
                    if class_choice == 3:
                        m.record_write(class_path)
                    else:
                        m.record_write(m.class_choice(class_choice))
                    lesson_menu_choice = v.menu(menu.lesson_menu(), '\nПродолжить?')
                    if lesson_menu_choice == 2:
                        flag = False
        case 2:
            exit()


def start():
    while True:
        print()
        user_inp = v.menu(menu.main_menu(), '\nГлавное меню')
        input_handler(user_inp)
