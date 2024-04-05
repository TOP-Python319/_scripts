venv_text = open("venv.txt", "r", encoding='utf-8')  # создаётся ссылка на файл, дескриптор

# .read() - считывает весь файл, включая переносы строк
# .readline() - считывает строку, до символа конца строки \n
# .readlines() - считывает все строки


while (file_line := venv_text.readline()) != '':
    print(file_line)

venv_text.close()


venv_text = open("venv.txt", "r", encoding='utf-8')  # заново создаётся ссылка на файл, дескриптор
for line in venv_text.readlines():
    print(line)
venv_text.close()