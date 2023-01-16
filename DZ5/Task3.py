# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# Не стал выносить функции в файл, тут кода немного

def archive(rle: str):
    count = 0
    archive = ''
    symbol = ''
    rle = ''.join(' ') + rle + ''.join(' ')
    for i in range(len(rle)):
        if rle[i].isalpha() or rle[i] == ' ':
            if rle[i] == ' ' and i < 2:
                continue
            if rle[i] != rle[i - 1] and count != 0:
                archive += f'{count}{symbol}'
                count = 0
            symbol = rle[i]
            count += 1
    else:
        rle = rle.strip()
    return archive


def unpack_file(rle: str):
    unpack = ''
    symbol = ''
    digit = 0
    residue = ''
    for i in range(len(rle)):
        if rle[i].isdigit():
            if rle[i + 1].isdigit():
                residue += rle[i]
                continue
            digit = int(residue + rle[i])
            residue = ''
            symbol = rle[i + 1]
            unpack += f'{digit * symbol}'
    return unpack


def read_file():
    path = 'Files/File1.txt'  # Читаем файлы
    data = open(path, 'r', encoding='UTF-8')
    source = data.readline()
    data.close()
    return source


def write_file(source: str):
    with open('Files/File2.txt', 'w', encoding='UTF-8') as data:
        data.write(source)


# ====================================================================================================================
rle = read_file()
print(f'{rle} - Изначальные данные')
rle = rle.strip()
if rle[0].isalpha():
    file_archive = archive(rle)
    write_file(file_archive)
    print(file_archive)
elif rle[0].isdigit():
    file_unpack = unpack_file(rle)
    write_file(file_unpack)
    print(file_unpack)
