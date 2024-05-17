class Cat:

    __shared_attribs = {
        # необязательно указывать
        "breed": '',
        "color": ''
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attribs
        



# паттерн моносостояние (monostate)
# паттерн Борг (Borg)


cat1 = Cat()
cat2 = Cat()
print(cat1.__dict__)
print(cat2.__dict__)
# >>>: {'breed': '', 'color': ''}
# >>>: {'breed': '', 'color': ''}
cat1.breed = 'red'
print(cat1.__dict__)
print(cat2.__dict__)
# >>>: {'breed': 'red', 'color': ''}
# >>>: {'breed': 'red', 'color': ''}
cat2.breed = 'sfinx'
print(cat1.__dict__)
print(cat2.__dict__)
# >>>: {'breed': 'sfinx', 'color': ''}
# >>>: {'breed': 'sfinx', 'color': ''}
cat3 = Cat()
print(cat1.__dict__)
print(cat2.__dict__)
print(cat3.__dict__)
# >>>: {'breed': 'sfinx', 'color': ''}
# >>>: {'breed': 'sfinx', 'color': ''}
# >>>: {'breed': 'sfinx', 'color': ''}
cat3.breed = 'scottish'
cat3.color = 'bald'
print(cat1.__dict__)
print(cat2.__dict__)
print(cat3.__dict__)
# >>>: {'breed': 'scottish', 'color': 'bald'}
# >>>: {'breed': 'scottish', 'color': 'bald'}
# >>>: {'breed': 'scottish', 'color': 'bald'}
cat3.weight = 10
print(cat1.__dict__)
print(cat2.__dict__)
print(cat3.__dict__)
# >>>: {'breed': 'scottish', 'color': 'bald', 'weight': 10}
# >>>: {'breed': 'scottish', 'color': 'bald', 'weight': 10}
# >>>: {'breed': 'scottish', 'color': 'bald', 'weight': 10}

print(id(cat1))
print(id(cat2))
print(id(cat3))
# >>>: 140494498643920
# >>>: 140494498643872
# >>>: 140494498643680