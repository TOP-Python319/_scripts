d = [
    (10, 10, -19),
    (12, 9, 0),
    (0, 2, 1),
    (-2, -10, -3),
    (0, 0, 100, 10)
]

# просто сортировка по первому значению
print(sorted(d))

# сортировка по среднему арифмитеческому в каждом кортеже

def avg(x):
    return sum(x) / len(x)

print(sorted(d, key=avg))


print(sorted(d, key=avg)[0])
print(sorted(d, key=avg)[-1])

# кортеж с максимальным первым значением
print(max(d))


# кортеж с максимальным третьим значением
def f(x):
    return x[2]

print(max(d, key=f))

# сумма минимального и макимального значения в каждом кортеже
def min_max(x):
    return min(x) + max(x)

print(sorted(d, key=min_max))
