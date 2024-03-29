def main_func():
    name = 'Ivan'  # в локальной области видимости функции main_func()
    def inner_func():
        print("Hello from inner function", name) 

    return inner_func

b = main_func()
print(b)
b()