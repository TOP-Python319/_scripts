# прямо или косвенно пользовательские исключения наследуются от базового класса Exception

# class MyOwnException(Exception):
#     ...


# class YetAnotherException(MyOwnException):
#     ...


# class MyOwnArithmeticException(ArithmeticError):
#     ...


# в назавании пользовательского исключения как правило есть слово Error
# как правило все пользовательские исключения хранятся в файле exceptions.py или errors.py
class CustomError(Exception):
    ...


# raise CustomError
# Traceback (most recent call last):
#   File "/home/maks/Work/top-academy/python 319/.scripts/lesson 32/exceptions/exception2.py", line 19, in <module>
#     raise CustomError
# __main__.CustomError


# raise CustomError('custom message')
# Traceback (most recent call last):
#   File "/home/maks/Work/top-academy/python 319/.scripts/lesson 32/exceptions/exception2.py", line 26, in <module>
#     raise CustomError('custom message')
# __main__.CustomError: custom message
