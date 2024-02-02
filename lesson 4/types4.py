def func():
    pass

print(
	f"{bool(None) = }",
	f"{bool(1) = }",
	f"{bool(2) = }",
	f"{bool(0) = }",
	f"{bool(0.0) = }",
	f"{bool(0.000001) = }",
	f"{bool('text') = }",
	f"{bool('') = }",
	f"{bool(' ') = }",
	f"{bool([]) = }",
	f"{bool(['']) = }",
	f"{bool(func) = }",
	sep='\n'
)
