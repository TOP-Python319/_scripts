numbers = [1, 1, 1, 1, 10, 10, 3, 10, 10, 'hi', 7, 9, 10, 10, 'hi', 7]
# список чисел, некоторые повторяется
# посчитать сколько какое число повторяется

# записать в словарь пары число: количество повторений

result = {}
# for n in numbers:
#     result[n] += 1  # result[n] = result[n] + 1

for n in numbers:  # последовательно перебираем 1 1 1 1 10 10 3
    if n not in result:
        result[n] = 1  #1.{1: 1} #5.{1: 4, 10: 1}
    else:
        result[n] += 1  #2.{1: 2} #3.{1: 3} #4.{1: 4} #6.{1: 4, 10: 2}

print(result)

