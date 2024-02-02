# допустимые аргументы для функции float()

print(
	f"{float(4) = }",
	f"{float(5.1) = }",
	f"{float(5.9) = }",
	f"{float(True) = }",
	f"{float(False) = }",
	f"{float('89') = }",
	f"{float('-13') = }",
	f"{float('10.1') = }",
	f"{float('-10.1') = }",
	sep='\n'
)


# недопустимые аргументы для функции float()
# print(float(None))
# print(float('8,8'))
# print(float('8 8'))
# print(float('3/10'))
