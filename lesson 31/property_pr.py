# класс UserMail
# методы:
#   __init__ с двумя аргументами login, __email
#   get_email возвращает __email
#   set_email принимает в виде строки новую почту,
#       должен проверять, что есть только один символ @ и после него точка
#   в противном случае выведем сообщение "неправильный формат почты"

import re


class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if not isinstance(value, str) or not re.fullmatch(r'\w+[@]\w+[.]\w+', value):
            print('неправильный формат почты')
        else:
            self.__email = value

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait

# ErrorMail:[1, 2, 3]
# ErrorMail:hello@@re.ee
# ErrorMail:{1, 2, 3}
# ErrorMail:prince@still@.wait
# ErrorMail:prince@stillwait
# ErrorMail:pri.nce@stillwait
