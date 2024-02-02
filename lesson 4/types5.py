# str() - человекочитаемое строковое представление
# repr() - машиночитаемое строковое представление

def func():
    pass
    

print(
	f"{str(None) = }",
	f"{str(1) = }",
	f"{str(0.0) = }",
	f"{str(0.000001) = }",
	f"{str('text') = }",
	f"{str(True) = }",
	f"{str(False) = }",
	f"{str([13, 14]) = }",
	f"{str(['']) = }",
	f"{str(func) = }",
	sep='\n'
)

print()
print()

print(
	f"{repr(None) = }",
	f"{repr(1) = }",
	f"{repr(0.0) = }",
	f"{repr(0.000001) = }",
	f"{repr('text') = }",
	f"{repr(True) = }",
	f"{repr(False) = }",
	f"{repr([13, 14]) = }",
	f"{repr(['']) = }",
	f"{repr(func) = }",
	sep='\n'
)

print("Let's go!")
