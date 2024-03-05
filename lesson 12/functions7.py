# def draw_star_box():
#     for _ in range(10):
#         print('*' * 100)
#     print()

# draw_star_box()


# названия произвольны, но должны быть осмысленными
def draw_star_box(height, width):  # функция принимает два параметра
    for _ in range(height):
        print('*' * width)
    print()

# draw_star_box()
# TypeError: draw_star_box() missing 2 required positional arguments: 'height' and 'width'

draw_star_box(10, 10)
draw_star_box(5, 5)
draw_star_box(3, 3)
draw_star_box(15, 7)

# с помощью одной и той же функции мы можем рисовать разные
# прямоугольники


h = 7
w = 2

draw_star_box(h, w)