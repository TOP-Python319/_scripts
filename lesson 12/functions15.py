cats = 1000000  # глобальная переменная


def print_cats_moscow():
    global cats
    cats += 100
    print(f'В Москве {cats} котиков')


print_cats_moscow()

print(cats)