# вывести сокращённые ФИО по полному имени

# Ввод:
# Иванов
# Иван
# Иванович

# Вывод
# ИИИ


input_surname = input('Введите фамилию: ')
input_name = input('Введите имя: ')
input_patronym = input('Введите отчество: ')


def print_fio(surname, name, patronym):
    print(surname[0].upper() + name[0].upper() + patronym[0].upper())


print_fio(input_surname, input_name, input_patronym)