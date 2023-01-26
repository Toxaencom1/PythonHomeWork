class_list = []
subjects_names_list = ['математика', 'русский', 'физкультура', 'Возвращение в главное меню']
students_names = []


def read_class_list(path: str):
    global class_list
    class_list = []
    count = 0
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        student_list = []
        for i, line in enumerate(my_list):
            if count > 2:
                break
            if line == '\n':
                count += 1
                continue
            subject = line.split(':')[0]
            student = line.split(':')[1].split(';')
            for i, student_el in enumerate(student):
                f_i = student_el.split('%')[0]
                marks = list(student_el.split('%')[1].rstrip())
                dict_ = {str(i + 1): {f_i: marks}}
                student_list.append(dict_)
            else:
                dict_subject = {subject: student_list}
                class_list.append(dict_subject)
                student_list = []
        return class_list


def get_subjects_names_list():
    global subjects_names_list
    return subjects_names_list


def create_subject_names_list(path: str):
    global subjects_names_list
    for i in read_class_list(path):
        for subj, stud in i.items():
            subjects_names_list.append(subj)
    subjects_names_list.append('Возвращение в главное меню')
    return subjects_names_list


def class_choice(which: int, input_=''):
    match which:
        case 1:
            return '7A.txt'
        case 2:
            return '7B.txt'
        case 3:
            class_path_choice = input_
            return class_path_choice


def subj_choice(which: int) -> str:
    global subjects_names_list
    return subjects_names_list[which-1]


def record_write(path: str):
    global class_list
    record = ''
    for i in class_list:
        for subj, stud in i.items():
            record += subj + ':'
            for j in stud:
                for ident, stu in j.items():
                    for f_i, marks in stu.items():
                        record += f'{f_i}%{"".join(marks)};'
        else:
            record = record.rstrip(';')
            record += '\n'
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(record)


def get_db_path():
    global class_path
    return class_path


def class_list_print():
    global class_list
    print(class_list)


def set_student_mark(subj_menu_choice: int, who_working: int, evaluation):
    global class_list
    class_list[subj_menu_choice - 1][subj_choice(subj_menu_choice)][who_working - 1][str(who_working)][
        names_list()[who_working - 1]].append(str(evaluation))


def names_list() -> list:
    global class_list
    global students_names
    students_names = []
    for i in class_list:
        for subj, stud in i.items():
            for j in stud:
                for ident, stu in j.items():
                    for f_i, marks in stu.items():
                        students_names.append(f_i)
        break
    return students_names
