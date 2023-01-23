import model
import view
import menu


model.read_db('database.txt')  # для быстрого теста открыть ком


def input_handler(inp: int):
    match inp:
        case 1:
            if view.db_success(model.get_db()):
                view.show_all(model.get_db())
        case 2:
            db_choice = view.menu(menu.db_menu(), '\nВыберите файл базы данных')
            if not db_choice == 4:
                if db_choice == 3:
                    model.db_choice(db_choice, view.string_input('"Внимание!" - файл базы данных должен быть корневой '
                                                                 'папке и в формате *.txt\n'
                                                                 'Введите название файла базы данных: '))
                    model.read_db(model.get_db_path())
                    view.db_success(model.get_db())
                else:
                    model.db_choice(db_choice)
                    model.read_db(model.get_db_path())
                    view.db_success(model.get_db())
        case 3:
            if view.db_success(model.get_db()):
                find = view.menu(menu.search_menu(), '\nПоисковое меню\n==============')
                if not find == 5:
                    view.show_all(model.find_contact(find, view.string_input('Кого ищем? :')))
        case 4:
            if view.db_success(model.get_db()):
                model.record_write(model.get_db_path(), view.create_contact())
                model.read_db(model.get_db_path())
        case 5:
            if view.db_success(model.get_db()):
                find = view.menu(menu.search_menu(),
                                 '\nКакой контакт хотите изменить?\nДавайте найдем Id контакта\n==============')
                if not find == 5:
                    temp = model.find_contact(find, view.string_input('Кого ищем? :'))
                    view.show_all(temp)
                    was_chosen = view.which_one('Укажите идентификатор контакта для изменения')
                    contact_to_change = model.get_right_contact(temp, was_chosen)
                    category = view.menu(menu.search_menu(), '\nПо какой категории хотите внести изменения?\n')
                    if not category == 5:
                        model.change_contact(contact_to_change, was_chosen, category,
                                             view.string_input('Внесите изменения: '))
                        model.read_db(model.get_db_path())
        case 6:
            if view.db_success(model.get_db()):
                model.remove_record(view.which_one('Кого удалить?'))
        case 7:
            view.exit_programm()


def start():
    while True:
        print()
        user_inp = view.menu(menu.main_menu(), '\nГлавное меню')
        input_handler(user_inp)
