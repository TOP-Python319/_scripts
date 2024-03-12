# перевод стобалльных оценок в пятибальные


# за одно выполнение функции может выполниться только один return
def convert_grade(grade):
    if grade > 80:
        return 5
    elif grade > 60:
        return 4
    elif grade > 40:
        return 3
    elif grade > 20:
        return 2
    elif grade > 0:
        return 1
    else:
        return 'неверно введено значение'
    

# def convert_grade(grade):
#     if grade > 80:
#         result = 5
#     elif grade > 60:
#         result = 4
#     elif grade > 40:
#         result = 3
#     elif grade > 20:
#         result = 2
#     elif grade > 0:
#         result = 1
#     else:
#         result = 'неверно введено значение'
    
#     return result

    
g = int(input('Введите 100-балльную оценку: '))
grade_in_5 = convert_grade(g)
print(convert_grade(g))