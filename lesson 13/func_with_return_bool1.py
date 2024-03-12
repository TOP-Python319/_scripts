n = int(input('Введите число: '))


# def is_even(number):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    

def is_even(number):
    if n % 2 == 0:
        return True
    return False
    

if is_even(n):  # часто, ф-ции, которые начинаются с is_ возвращают bool
    print('Число чётное')
else:
    print('Число нечётное')