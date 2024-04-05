venv_text = open("venv.txt", "r", encoding='utf-8')  # создаётся ссылка на файл, дескриптор

# .read() - считывает весь файл, включая переносы строк
# .readline() - считывает строку, до символа конца строки \n
# .readlines() - считывает все строки

file_line = venv_text.readline()  # читает первую строку
next_line = venv_text.readline()  # читает следующую строку


venv_text.close()