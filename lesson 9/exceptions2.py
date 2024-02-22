text = '\nвведите целое число: '
warning = 'используйте только десятичные цифры'


# while True:
#     n = int(input(text))


# while True:
#     n = input(text)
#     if n.isdecimal():
#         n = int(n)
#         break
#     else:
#         print(warning)


while True:
    try:
        n = int(input(text))
    except ValueError:
        print(warning)
    else:
        break
