# общий формат функции open()
# file = open(<имя файла>, <режим доступа>, <кодировка>)
# параметр кодировка опционален, но очень желателен

# режимы доступа

# r - только для чтения (по умолчанию), файл нельзя изменить

# w - только для записи, не можем читать, если файл существует, то его содержимое сотрётся.
#     Если файл не существует, создается новый

# a - дозапись, данные добавляются в конец файла.
#     Если файл не существует, создается новый

# r+ - открыть файл для чтения и записи.
#      Если файл не существует, возникнет ошибка

# x - создание нового файла.
#     Если файл существует, возникнет ошибка.


# 'w' - весь файл сначала стирается, а затем в него добавляются данные
# ОСТОРОЖНО DANGER
# with open("test.txt", "w", encoding='utf-8') as test_text:
#     test_text.write('Hi World!\n')
#     test_text.write('Hello World!\n')
#     test_text.write('Hello World!\n')

# # 'a' - данные добавляются в конец файла
# with open("test.txt", "a", encoding='utf-8') as test_text:
#     test_text.write('Hello World!\n')
#     test_text.write('Hello World!\n')
#     test_text.write('Hello World!\n')


# 'r+' - открыть файл для чтения и записи, запись работает как в режиме 'w'
with open("test.txt", "r+", encoding='utf-8') as test_text:
    test_text.write('Hello World!1\n')
    test_text.write('Hello World!2\n')
    test_text.write('Hello World!3\n')
    test_text.seek(0)
    print(test_text.read())