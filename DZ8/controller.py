import model as m
import view as v
import menu
import validator as val


def input_handler(inp: int):
    global subj_names
    class_path = ''
    match inp:
        case 1:
            class_choice = v.menu(menu.class_menu(), '\nВыберите Класс учащихся')
            if class_choice == 3:
                class_path = val.v_bd_path(v.string_input('\nВведите название файла\n'
                                            'Файл должен быть Цифра_класса+Буква_класса.txt '
                                            'и в папке classes, \n'                                            
                                            'Формат базы - "предмет:Фамилия Имя%оценки;Фамилия Имя%оценки; итд" \n:>'))
                m.read_class_list(class_path)
            else:
                class_path = m.class_choice(class_choice)
                m.read_class_list(class_path)
            # m.class_list_print()
            action_menu_choice = v.menu(menu.action_menu(), '\nВыбирите действие')
            match action_menu_choice:
                case 1:
                    subj_menu_choice = v.menu(m.create_subject_names_list(class_path), '\nВыберите предмет')
                    if not subj_menu_choice == len(m.get_subjects_names_list()):
                        flag1 = True
                        while flag1:
                            flag2 = True
                            v.show_all(m.get_class_list(), m.subj_choice(subj_menu_choice))
                            who_working = v.which_one('\nКому дать задание?', m.get_max_students())
                            evaluation = v.estimate('\nКакую оценку дать??')
                            m.set_student_mark(subj_menu_choice, who_working, evaluation)
                            m.record_write(class_path)
                            while flag2:
                                v.show_all(m.get_class_list(), m.subj_choice(subj_menu_choice))
                                lesson_menu_choice = v.menu(menu.lesson_menu(), '\nПродолжить?')
                                match lesson_menu_choice:
                                    case 1:
                                        flag2 = False
                                    case 2:
                                        m.delete_student_mark(subj_menu_choice, who_working, evaluation)
                                    case 3:
                                        flag1 = False
                                        flag2 = False
                                m.record_write(class_path)
                case 2:
                    m.add_student(v.f_i_input('\nВведите Фамилию и Имя через пробел: '))
                    m.record_write(class_path)
                case 3:
                    m.create_subject_names_list(class_path)
                    v.show_all(m.get_class_list(), m.get_subjects_names_list()[0])
                    who_looser = v.which_one('\nКого удалить?', m.get_max_students())
                    m.delete_student(who_looser)
                    m.record_write(class_path)
                    v.show_all(m.get_class_list(), m.get_subjects_names_list()[0])
        case 2:
            exit()


def start():
    while True:
        print()
        user_inp = v.menu(menu.main_menu(), '\nГлавное меню')
        input_handler(user_inp)
