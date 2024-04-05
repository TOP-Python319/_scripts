venv_text = open("venv.txt", "r", encoding='utf-8')  # создаётся ссылка на файл, дескриптор

# .read() - считывает весь файл, включая переносы строк
# .readline() - считывает строку
# .readlines() - считывает все строки


# file_contains = venv_text.read()  # читает весь файл
# print(file_contains)

file_contains_10 = venv_text.read(10)  # читает первые 10 символов
file_contains_next_10 = venv_text.read(10)  # читает следущие 10 символов
file_contains = venv_text.read() 

venv_text.seek(0)  # перемещает курсор в начало файла
another_file_contains_10 = venv_text.read(10)  # читает первые 10 символов

venv_text.close()