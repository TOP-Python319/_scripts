# HockeyPlayer
# конструктор принимает два аргумента: name, number

# так же во время инициализации создаётся 2 атрибута: goals, assists,
# по умолчанию по нулям

# метод, который увеличивает goals

# метод, который увеличивает assists

# метод, который выводит статистику


class HockeyPlayer:
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.goals = 0
        self.assists = 0

    # __str__ и __repr__ похожи, но первый используется, для чтения людьми
    # второй для чтения машиной
    # иными словами __str__ вызывается функциий print()
    # __repr__ вызывается функция repr()
    def __str__(self) -> str:
        return f'Игрок {self.name} под номером {self.number} забил {self.goals} голов и сделал {self.assists} голевых передач'

    def __repr__(self):
        return f'{self.__class__} {id(self)}'

    def score(self, increase=1):
        self.goals += increase

    def assist(self, increase=1):
        self.assists += increase


panarin = HockeyPlayer('Артемий Панарин', 10)
panarin.score(49)
panarin.assist(71)
print(panarin)
print(panarin.__repr__)
print(panarin.__dict__)

print()

ovechkin = HockeyPlayer('Александр Овечкин', 8)
ovechkin.score(31)
ovechkin.assist(34)
print(ovechkin)
print(ovechkin.__repr__)
print(ovechkin.__dict__)
pass