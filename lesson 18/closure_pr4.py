# функция вносит число в список и подсчитывает среднее арифмитическое этого списка


# решение со списком (sum()/len())
# def avg_numbers() -> callable:
#     numbers = []
#     def inner(number: int) -> float:
#         numbers.append(number)
#         print(numbers)
#         return sum(numbers) / len(numbers)

#     return inner

# решение с двумя переменными (summator/counter)
def avg_numbers() -> callable:
    summator = 0
    counter = 0
    def inner(number) -> float:
        nonlocal summator, counter
        summator += number
        counter += 1
        return summator / counter

    return inner


list1 = avg_numbers()
list2 = avg_numbers()

print(list1(1))  # [1] 1.0
print(list1(3))  # [1, 3] 2.0

print(list2(5))  # [5] 5.0
print(list2(7))  # [5, 7] 6.0

print(list1(10))  # [1, 3, 10] 4.(6)7
print(list1(15))  # [1, 3, 10, 15] 7.25