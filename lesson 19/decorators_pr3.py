# декоратор, который возвращает удвоенный результат вывода функции

def double(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs) * 2
        return result
    return inner

@double
def get_sum(*args):
    return sum(args)


@double
def double_str(text):
    return text


r = get_sum(1, 2, 3, 4, 5)
print(r)  # 30

t = double_str('Hi!')
print(t)