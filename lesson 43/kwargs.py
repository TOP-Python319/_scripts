def print_info(**kwargs):
    # print(type(kwargs))
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30, city="New York")
print_info(name="Jane", age=25, city="London", country="UK")
print_info(name="Bob", age=40)
print_info()
print_info(name="Alice", age=35, city="Paris", country="France")
print_info(name="Charlie", age=50, city="Sydney", country="Australia", gender="male")

