class_list = []
subjects_names_list = []
students_names = []


def read_class_list(path: str):
    global class_list
    class_list = []
    count = 0
    with open('classes/'+path, 'r', encoding='UTF-8') as file:
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


def get_class_list():
    global class_list
    return class_list


def get_subjects_names_list():
    global subjects_names_list
    return subjects_names_list


def create_subject_names_list(path: str):
    global subjects_names_list
    subjects_names_list = []
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
    with open('classes/'+path, 'w', encoding='UTF-8') as file:
        file.write(record)


def class_list_print():   # для отладки
    global class_list
    print(class_list)


def set_student_mark(subj_menu_choice: int, who_working: int, evaluation):
    global class_list
    class_list[subj_menu_choice - 1][subj_choice(subj_menu_choice)][who_working - 1][str(who_working)][
        names_list()[who_working - 1]].append(str(evaluation))

def delete_student_mark(subj_menu_choice: int, who_working: int, evaluation):
    global class_list
    class_list[subj_menu_choice - 1][subj_choice(subj_menu_choice)][who_working - 1][str(who_working)][
        names_list()[who_working - 1]].pop()


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

def get_max_students():
    max_students = 0
    for i in class_list:
        for subj, stud in i.items():
            for j in stud:
                for ident, stu in j.items():
                    if int(ident) > max_students:
                        max_students = int(ident)
    return max_students


def add_student(student_f_i: str):
    global class_list
    student_f_i += '% '
    max_id = get_max_students()
    student_f_i = student_f_i.split('%')
    student_f_i[1] = []
    temp_dict_1 = {student_f_i[0]: student_f_i[1]}
    temp_dict_2 = {f'{max_id + 1}': temp_dict_1}
    for i in class_list:
        for subj, stud in i.items():
            stud.append(temp_dict_2)


def delete_student(which: int):
    global class_list
    record_write('recent.txt')
    for i in class_list:
        for subj, stud in i.items():
            for j in stud:
                for ident, stu in j.items():
                    if int(ident) == which:
                        j.pop(ident)
                        break

