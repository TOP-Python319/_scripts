class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class Discount:
    def apply_discount(self, discount):
        self.price -= self.price * discount
        # self.price = self.price - self.price * discount


class DiscountedProduct(Product, Discount):
    pass


product1 = DiscountedProduct('Телефон', 10000)
product1.apply_discount(0.1)
print(product1.get_price())
