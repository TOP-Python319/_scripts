def sum_two_digits(digit1, digit2):
    return digit1 + digit2


print(sum_two_digits(10, 20))  # вызов функции с позиционными аргументами

print(sum_two_digits(digit1=10, digit2=20))  # вызов функции с именованными аргументами

print(sum_two_digits(digit2=10, digit1=20))  # вызов функции с именованными аргументами

# print(sum_two_digits(digit1=int(input()), digit2=int(input())))  # вызов функции с именованными аргументами


# негласное правило: если функция принимает больше трёх аргументов, то хотя бы часть из них нужно сделать именнованными

def draw_rectangle(width, height, border_color, fill_color, border_widtgh):
    pass


draw_rectangle(100, 200, 'red', 'blue', 5)
draw_rectangle(100, 200, border_color='red', fill_color='blue', border_widtgh=5)  # в соответствии с PEP8, знак равенства не окружается пробелами
draw_rectangle(100, 200, border_color = 'red', fill_color = 'blue', border_widtgh = 5)  # синтаксически верная, но нарушает стилистику PEP8

draw_rectangle(
    width=100,
    height=200,
    border_color='red',
    fill_color='blue',
    border_widtgh=5
)  # все аргументы именнованные


# draw_rectangle(
#     width=100,
#     height=200,
#     'red',
#     fill_color='blue',
#     border_widtgh=5
# )  # неверно, так как позиционные аргументы не могут идти после именнованных


# def rgb(red, green, blue):
#     pass


# rgb(255, 0, 0)
