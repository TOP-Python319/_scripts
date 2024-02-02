# допустимые аргументы для функции int()

print(
	f"{int(4) = }",
	f"{int(5.1) = }",
	f"{int(5.9) = }",
	f"{int(True) = }",
	f"{int(False) = }",
	f"{int('89') = }",
	f"{int('-13') = }",
	f"{int('0b1111', 2) = }",
	sep='\n'
)

print()
print(f"{1/3:.3f}")  # форматирование типов
print(f"{1/3}")

# недопустимые аргументы для функции int()

# print(int('8.9'))
# print(int('text'))
# print(int('1-3'))
# print(int(None))
# print(int('10p11'))
# print(int('10 11'))
