# класс Zebra

# с методом which_stipe(),
# метод поочерёдно печатает фразы "полоса белая", "полоса чёрная"
# начиная с "полоса белая"


class Zebra:
    
    def __init__(self):
        self.counter = 0

    def which_stripe(self):
        self.counter += 1

        # if self.counter % 2 == 0:
        #     print('Полоса чёрная')
        # else:
        #     print('Полоса белая')

        print(
            ['Полоса чёрная', 'Полоса белая'][self.counter % 2] # один аргумент
        )


marty = Zebra()
marty.which_stripe()  # полоса белая
marty.which_stripe()  # полоса чёрная
marty.which_stripe()  # полоса белая
marty.which_stripe()  # полоса чёрная
marty.which_stripe()  # полоса белая
marty.which_stripe()  # полоса чёрная


# ['Полоса чёрная', 'Полоса белая'][self.counter % 2]
# ['Полоса чёрная', 'Полоса белая'] - список
# [self.counter % 2] - индекс
# в списке всего два элемента, следовательно есть индексы только 0 и 1
# 1 % 2 = 1
# 2 % 2 = 0
# 3 % 2 = 1
# 4 % 2 = 0
# 5 % 2 = 1