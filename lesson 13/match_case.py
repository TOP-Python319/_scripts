# перевод стобалльных оценок в пятибальные

def convert_grade(grade):
    # if grade > 80:
    #     return 5
    # elif grade > 60:
    #     return 4
    # elif grade > 40:
    #     return 3
    # elif grade > 20:
    #     return 2
    # elif grade > 0:
    #     return 1
    # else:
    #     return 'неверно введено значение'
    
    match grade:
        case _ if grade > 80:
            return 5
        case _ if grade > 60:
            return 4
        case _ if grade > 40:
            return 3
        case _ if grade > 20:
            return 2
        case _ if grade > 0:
            return 1

    
g = int(input('Введите 100-балльную оценку: '))
print(convert_grade(g))