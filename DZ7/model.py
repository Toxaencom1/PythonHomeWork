db_list = []
db_path = 'database.txt'


def read_db(path: str):
    global db_list
    db_list = []
    count = 0
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for i, line in enumerate(my_list):
            if count > 2:
                break
            if line == '\n':
                count += 1
                continue
            # id_dict = dict()
            line = line.strip().split(';')
            id_dict = {i + 1: {'lastname': line[0], 'firstname': line[1], 'phone': line[2], 'comment': line[3]}}
            db_list.append(id_dict)


def db_choice(which: int, input_=''):
    global db_path
    match which:
        case 1:
            db_path = 'database.txt'
        case 2:
            db_path = 'recent.txt'
        case 3:
            db_path = input_


def record_write(path: str, record: str):
    with open(path, 'a', encoding='UTF-8') as file:
        file.write(record + '\n')


def remove_record(looser: int):
    global db_list
    temp = {}
    if not looser > len(db_list):
        temp = db_list.pop(looser - 1)
        f = open('database.txt', encoding='UTF-8').readlines()
        a = f.pop(looser - 1)
        with open('recent.txt', 'a', encoding='UTF-8') as file:
            file.writelines(a)
        print(f'Запись - {a}отравлена в файл recent.txt c удаленными записями из базы\n')
        with open('database.txt', 'w', encoding='UTF-8') as file:
            file.writelines(f)
    else:
        print('Нет такой записи')
    return temp


def find_contact(search_menu_choice: int, search_input: str) -> list:
    global db_list
    match search_menu_choice:
        case 1:
            return case_choice(search_input, 'lastname')
        case 2:
            return case_choice(search_input, 'firstname')
        case 3:
            return case_choice(search_input, 'phone')
        case 4:
            return case_choice(search_input, 'comment')


def case_choice(search_input, key_type: str) -> list:
    search_dict = []
    for item in db_list:
        for key, value in item.items():
            if value.get(key_type) == search_input.title() or value.get(key_type) == search_input.lower() or \
                    value.get(key_type) == search_input.title() + 'а' or value.get(
                key_type) == search_input.lower() + 'а' or \
                    family_strip(value.get(key_type)) == family_strip(search_input.title()) or \
                    family_strip(value.get(key_type)) == family_strip(search_input.lower()):
                search_dict.append(item)
    else:
        print('Поиск закончен')
    return search_dict


def get_right_contact(dict_: list, ident):
    for item in dict_:
        for k, v in item.items():
            if k == ident:
                return item


def change_contact(dict_: list, ident: int, category: int, changes: str):
    global db_list
    remove_record(ident)
    match category:
        case 1:
            dict_[ident]['lastname'] = changes
        case 2:
            dict_[ident]['firstname'] = changes
        case 3:
            dict_[ident]['phone'] = changes
        case 4:
            dict_[ident]['comment'] = changes
    db_list.append(dict_)
    contact = f"{dict_[ident].get('lastname')};{dict_[ident].get('firstname')};\
{dict_[ident].get('phone')};{dict_[ident].get('comment')}"
    record_write('database.txt', contact)
    print('\nЗапись успешно заменена!\n')


def family_strip(firstname: str) -> str:
    firstname = firstname.rstrip('а')
    return firstname


def get_db():
    global db_list
    return db_list


def set_db(new_record: dict):
    global db_list
    db_list.append(new_record)


def get_db_path():
    global db_path
    return db_path


def set_db_path(path: str):
    global db_path
    db_path = path
