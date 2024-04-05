venv_text = open("venv.txt", "r", encoding='utf-8')  # создаётся ссылка на файл, дескриптор

# .read() - считывает весь файл, включая переносы строк
# .readline() - считывает строку, до символа конца строки \n
# .readlines() - считывает все строки, и возвращает в виде списка


file_lines = venv_text.readlines()  # читает все строки

venv_text.close()
