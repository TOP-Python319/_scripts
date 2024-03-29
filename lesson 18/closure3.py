def add(value):
    def inner(a):
        return value + a

    return inner

increase_to_2 = add(value=2)  # функция, которая будет увеличивать входящее значение на 2
increase_to_3 = add(value=3)  # функция, которая будет увеличивать входящее значение на 3
# главная идея замыкания - мы вызываем функцию, помещая туда значение, и
# теперь эта функция связана только с этим значением

print(increase_to_2)
print(increase_to_3)


print(increase_to_2(a=5))  # value = 2, a = 5, 2 + 5 = 7
print(increase_to_3(a=5))  # value = 3, a = 5, 3 + 5 = 8

