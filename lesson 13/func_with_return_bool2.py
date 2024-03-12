# пользователь вводит артикул товара
# но только 100, 200, 300 валидные


art = int(input('Введите артикул: '))

# while art != 100 and art != 200 and art != 300:
#     print('Допустимые артикулы 100 200 и 300')
#     art = int(input('Введите артикул: '))


def is_valid_articule(articule):
    return True if art != 100 and art != 200 and art != 300 else False


while is_valid_articule(art):
    print('Допустимые артикулы 100 200 и 300')
    art = int(input('Введите артикул: '))