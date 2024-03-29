# создадим функцию mult(), которая принимает один аргумент,
# сохраняет это значение и возвращает результат умножения этого числа на новое


def mult(x: int) -> callable:

    # вложенная функция
    def inner(y: int) -> int:
        return x * y

    return inner


mult_to_2: callable = mult(x=2)
print('3 * 2 = ', mult_to_2(y=3))  # 6
print('5 * 2 = ', mult_to_2(y=5))  # 10

mult_to_7: callable = mult(x=7)
print('3 * 7 = ', mult_to_7(y=3))  # 21
print('5 * 7 = ', mult_to_7(y=5))  # 35