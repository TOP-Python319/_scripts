cats = 1000000  # глобальная переменная


def print_cats():
    print(f'В Стамбуле {cats} котиков.')


print_cats()


def print_cats_ankara():
    cats = 500  # создаём в области видимости print_cats_ankara переменную cats
    print(f'В Анкаре {cats} котиков.')

# def print_cats_moscow():
#     cats += 100  # глобальную переменную изменить нельзя
#     print(f'В Москве {cats} котиков')

print_cats_ankara()

print_cats_moscow()

print(cats)