class City:
    pass

# два экземпляра
# в первом атрибуте population, age, hemisphere
# во втором атрибуте population, age, language

moscow = City()
moscow.population = 16_000_000
moscow.age = 870
moscow.hemisphere = 'north'

kyiv = City()
kyiv.population = 5_000_000
kyiv.age = 1200
kyiv.language = 'ukrainian'


print(moscow.__dict__)
print(kyiv.__dict__)
print(City.__dict__)
# >>>: {'population': 16000000, 'age': 870, 'hemisphere': 'north'}
# >>>: {'population': 5000000, 'age': 1200, 'language': 'ukrainian'}
# >>>: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'City' objects>, '__weakref__': <attribute '__weakref__' of 'City' objects>, '__doc__': None}

print(moscow.__module__)
# >>>: __main__

print(City.__dict__)
# >>>: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'City' objects>, '__weakref__': <attribute '__weakref__' of 'City' objects>, '__doc__': None}
# Все эти атрибуты так же попадают в каждый экземпляр класса