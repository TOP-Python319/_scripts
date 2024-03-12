# функция принимает в качестве аргумента номер месяца (от 1 до 12)
# возвращает количество дней в этом месяце
# в феврале всегда 28 дней 
# 1 3 5 7 8 10 12 - 31
# 4 6 9 11 - 30
# 2 - 28

month = int(input('Введите порядковый номер месяца: '))

def get_days_in_month(month):
    if month < 1 or month > 12:
        return 'нет такого месяца'
    if month == 2:
        return 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

print(get_days_in_month(month))