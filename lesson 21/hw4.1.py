# Написать программу, которая проверяет корректность введённого адреса электронной почты.

# Программа получает из стандартного потока ввода (stdin) строку, содержащую адрес электронной почты. 
# Программа выводит в stdout текстовый ответ.

# Для забегающих вперёд: да, такие задачи обычно решаются с помощью регулярных выражений. Но в этой задаче вам необходимо использовать строковые методы:
#     https://docs.python.org/3/library/stdtypes.html#string-methods

# Примечание: в корректном e-mail обязательно есть символ '@', а после него символ '.'

# Пример ввода 1:
#     sgd@ya.ru

# Пример вывода 1:
#     да

# Пример ввода 2:
#     abcde@fghij

# Пример вывода 2:
#     нет


email = input()

if email.count('@') != 1:
    result = 'Нет'
else:
    # Разбиваем строку на части по символу '@'
    name_email, domain = email.split('@') 
    if name_email == '':
        result = 'Нет'
    else:
        if domain.count('.') != 1:
            result = 'Нет'
        else:
            if domain[-1] == '.' or domain[0] == '.':
                result = 'Нет'
            else:
                result = 'Да'
print(result)
