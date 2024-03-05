# функция, которая будет повторять
# текст, который ввёл пользователь
# заданное (пользователем) количество раз

phrase = input('Введите текст: ')
repeats = int(input('Количество повторений: '))

# когда мы определяем фукнцию,
# text, r — параметры
def repeat_text(text, r):
    print(*[text for _ in range(r)])
    print()


# вызвали функцию и что-то в неё передаём
# phrase, repeats — аргументы
repeat_text(phrase, repeats)