# создадим класс Phone, который принимает три аргумента
# бренд, модель, цена
# нужно создать три атрибута по этим аргументам
# и 4-ый атрибут, который будет включать в себя Модель-Бренд


class Phone:

    def __init__(self, brand, model, price):

        self.brand = brand
        self.model = model
        self.price = price
        
        self.full_name = f'{self.brand} {self.model}'


iphone = Phone('Apple', 'iPhone 15', 1000)
samsung = Phone('Samsung', 'Galaxy s24', 1000)

print(iphone.__dict__)
print(samsung.__dict__)