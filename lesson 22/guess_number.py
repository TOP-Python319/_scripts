# угадайка чисел
# программа генерирует число от 1 до 100, просит пользователя угадать это число.
# Если догадка больше случайного числа,
# то программа выводит сообщение "Слишком много, попробуйте снова"
# Если догадка меньше случайного числа,
# то программа выводит сообщение "Слишком мало, попробуйте снова"
# Если пользователь угадал, то программа выводит "Вы угдадали, поздравляю!"
#____
# Пользователь сам выбирает границы рандомизатора.
#____
# Пользователю даётся 5 попыток, иначе проигрыш.


# random
# while True
# input(), print()
# if/elif/else
# break, continue


# Приветствие пользователя +
# Сгенерировать число +
# Попросить ввести число +
# Проверить число на валидность +
# Циклом проверяем соответствие введённых чисел загаднному числу
# Поздравить и вывести угаданное число


import random


total_tries = 5

print('Я хочу сыграть с тобой в игру!')

while True:
    while True:
        bottomline = input('Введите нижнюю границу рандомизатора: ')
        if not bottomline.isdigit():
            print('Введите целое число для нижней границы!')
            continue
        bottomline = int(bottomline)
        break
    while True:
        topline = input('Введите верхнюю границу рандомизатора: ')
        if not topline.isdigit():
            print('Введите целое число для верхней границы!')
            continue
        topline = int(topline)
        break
    if bottomline >= topline:
        print('Недопустимые границы, нижняя граница не должна быть больше или равна верхней границе.')
        continue
    break

print(f'Я загадал число от {bottomline} до {topline}, попробуй угадать! 😈😈😈')
print(f'У тебя всего {total_tries} попыток!')

number = random.randint(bottomline, topline)

def is_valid(n: str, bottom: int, top: int) -> bool:
    if not n.isdigit() and not (n[0] == '-' and n[1:].isdigit()):
        return False
    if bottom <= int(n) <= top:
        return True
    return False


while True:
    user_try = input(f'Введите число от {bottomline} до {topline}: ')
    if not is_valid(user_try, bottomline, topline):
        print(f'Некорректный ввод!\nПрограмма принимает только числа от {bottomline} до {topline}')
        continue
    response = int(user_try)

    if response > number:
        print('Слишком много, попробуйте снова')
    elif response < number:
        print('Слишком мало, попробуйте снова')
    else:
        print('Вы угдадали, поздравляю!')
        print('Игра закончена!')
        print('Сегодня вы уйдёте живым.')
        break

    total_tries -= 1
    print(f'Осталось {total_tries} попыток.')
    
    if total_tries == 0:
        print('Вы проиграли, вы самое слабое звено!')
        break


print('Спасибо за игру, приходите к нам снова!')
