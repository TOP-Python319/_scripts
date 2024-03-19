# список точек на координатной плоскости

dots = [
    (1, -1), 
    (2, 5), 
    (-13, 2), 
    (10, 3), 
    (17, -2), 
    (0, 0)
]

# задача отсортировать
print(sorted(dots))


# задача отсортировать по второму значению
def sort_by_second(item):
    return item[1]

print(sorted(dots, key=sort_by_second))


# задача отсортирова по сумме кортежа
def sort_by_sum(item):
    return item[0] + item[1]

print(sorted(dots, key=sort_by_sum))

