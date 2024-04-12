# from string import ascii_lowercase
# ascii_lowercase
# # 'abcdefghijklmnopqrstuvwxyz'
# from string import ascii_uppercase
# ascii_uppercase
# # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# from string import digits
# digits
# # '0123456789'

# программа генерирует заданное количество паролей, включает в себя умную настройку на
# длину пароля, наличие цифр, заглавных и строчных букв, спецсимволов


# определить количество паролей
# определить длину пароля

# определить наличие цифр
# определить наличие заглавных букв
# определить наличие строчных букв
# определить наличие спецсимволов
# исключать ли символы lI10Oo
import random

###### ЗАГОЛОВОК ПРОГРАММЫ
DIGITS = '0123456789'
UPPER_CASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_CASE = 'abcdefghijklmnopqrstuvwxyz'
SIGNS = '!?#%&*+-=$_.,|()[]~'
alphabet = '' # определить алфавит для пароля

###### ВВОД ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ
quantity = int(input('Сколько паролей генерировать?\n'))
pass_len = int(input('Введите длину паролей.\n'))

while flag_digit := input('Включать ли цифры? Y-да, N-нет\n').upper().strip() not in ('N', 'Y'):
    continue

flag_upper = input('Включать ли строчные буквы? Y-да, N-нет\n').upper().strip()
flag_lower = input('Включать ли прописные буквы? Y-да, N-нет\n').upper().strip()
flag_signs = input('Включать ли спецсимволы? Y-да, N-нет\n').upper().strip()

if flag_digit == flag_upper == flag_lower == flag_signs == 'N':
    print('Нет данных для генерации пароля.')

###### НАСТРОЙКА ГЕНЕРИРУЕМЫХ ПАРОЛЕЙ
if flag_digit == 'Y':
    alphabet += DIGITS
if flag_upper == 'Y':
    alphabet += UPPER_CASE
if flag_lower == 'Y':
    alphabet += LOWER_CASE
if flag_signs == 'Y':
    alphabet += SIGNS

###### ФУНКЦИЯ ГЕНЕРАЦИИ ПАРОЛЯ
def generate_password(password_length: int, chars: str) -> str:
    return ''.join(random.choices(chars, k=password_length))

for _ in range(quantity):
    print(generate_password(pass_len, alphabet))


# составить цикл по количеству паролей
# с помощью цикла и random.choice() составить пароль
# или с помощью random.choices()

# 5
# 10
# Y
# N
# N
# Y

