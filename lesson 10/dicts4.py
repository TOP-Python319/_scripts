run = {
    'понедельник': 4.7,
    'среда': 5.0,
    'пятница': 4.9
}

run['понедельник'] = 3.7
run
# {'понедельник': 3.7, 'среда': 5.0, 'пятница': 4.9}
new_run = {'понедельник': 4.9, 'среда': 5.2, 'пятница': 5.1}
run
# {'понедельник': 3.7, 'среда': 5.0, 'пятница': 4.9}
run.update(new_run)
run
# {'понедельник': 4.9, 'среда': 5.2, 'пятница': 5.1}

del new_run['понедельник']
new_run
# {'среду': 5.2, 'пятницу': 5.1}
run.update(new_run)
run
# {'понедельник': 4.7, 'среда': 5.0, 'пятница': 4.9, 'среду': 5.2, 'пятницу': 5.1}
run.update({'понедельник': 7.2})
run
# {'понедельник': 7.2, 'среда': 5.0, 'пятница': 4.9, 'среду': 5.2, 'пятницу': 5.1}

id(run)
# 140030349385408
run.update({'понедельник': 17.2})
id(run)
# 140030349385408


# del удаляет элемент словаря по ключу
run = {'понедельник': 4.9, 'среда': 5.2, 'пятница': 5.1}
run
# {'понедельник': 4.9, 'среда': 5.2, 'пятница': 5.1}
del run['понедельник']
run
# {'среда': 5.2, 'пятница': 5.1}


# метод pop() удаляет элемент по ключу и возвращает соответсвтующее
# ему значение
run.pop('пятница')
# 5.1
run
# {'среда': 5.2}


# метод clear() очищает словарь
run = {'понедельник': 4.9, 'среда': 5.2, 'пятница': 5.1}
run
# {'понедельник': 4.9, 'среда': 5.2, 'пятница': 5.1}
run.clear()
run
# {}

run = {
    'понедельник': 4.9, 
    'вторник': 4.7, 
    'среда': 5.2, 
    'четверг': 5.0,
    'пятница': 5.1
}


# метод popitem() удаляет последний ключ
# и возвращает его в виде кортежа (ключ, значение)
run
# {'понедельник': 4.9, 'вторник': 4.7, 'среда': 5.2, 'четверг': 5.0, 'пятница': 5.1}
run.popitem()
# ('пятница', 5.1)
run
# {'понедельник': 4.9, 'вторник': 4.7, 'среда': 5.2, 'четверг': 5.0}
run.popitem()
# ('четверг', 5.0)
run.popitem()
# ('среда', 5.2)
run.popitem()
# ('вторник', 4.7)
run
# {'понедельник': 4.9}