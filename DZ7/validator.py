def v_player_choice(choice, fr: int, to: int):
    if choice == 'exit':
        exit()
    while True:
        try:
            if fr <= int(choice) <= to:
                return int(choice)
            else:
                choice = emergency_exit(input(f'Неверно, выберите от {fr} до {to}: '))
        except ValueError:
            while True:
                try:
                    choice = emergency_exit(input(f'Выберите от {fr} до {to}: '))
                    if fr <= int(choice) <= to:
                        return int(choice)
                except ValueError:
                    print('Опять фигня получилась(((')


def emergency_exit(string_: str):
    if string_ == 'exit':
        exit()
    else:
        return string_
