#Напишите функцию is_palindrome(text),
#которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.

#Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

#Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

a = str(input("Введите строку:"))
def is_palindrome(string):
    if len(string) > 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False
if (is_palindrome(a) == True):
    print("True")
else:
    print("False")