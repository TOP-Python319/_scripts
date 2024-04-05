# with <объект> as <переменная>:
#     <код> в котором нам доступен ресурс <переменная>
# ресурс <переменной> уже освобождён даже если в блоке with произошла ошибка


# без менеджера контекста:
# venv_text = open("venv.txt", "r", encoding='utf-8')

# for line in venv_text.readlines():
#     print(line)

# venv_text.close()


# с менеджером контекста:
with open("venv.txt", "r", encoding='utf-8') as venv_text:
    for line in venv_text.readlines():
        print(line)
    print(venv_text)


# venv_text.seek(0)
# for line in venv_text.readlines():
#     print(line)
# print(venv_text)
# Код не сработает, потому что файл закрыт
# Traceback (most recent call last):
#   File "/home/maks/Work/top-academy/python 319/.scripts/lesson 20/with.py", line 21, in <module>
#     venv_text.seek(0)
# ValueError: I/O operation on closed file.