def main_func():
    def inner_func():
        print("Hello from inner function")

    return inner_func


b = main_func()  # inner_func()
print(b) 
# >>> <function main_func.<locals>.inner_func at 0x7f9486a66200>
# inner_func()  находится в локальной области видимости функции main_func()
# и теперь она нам доступна по ссылке b

# Замыкание - это функция, которая находится внутри другой функции и ссылается на 
# переменные объявленные в теле внешней функции

b()
# >>> Hello from inner function

