# 1. глобальные переменные затрудняют отладку
# 2. функции зависят от этих переменных
# 3. затрудняют понимание программы

def print_words():
    count = 1000  # переменная локальная
    print('Переменная равна', count)

def print_words2():
    print(count)  # переменная count находится в области видимости функции print_words()

print_words()
print_words2()