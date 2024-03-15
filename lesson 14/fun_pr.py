def f(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(f(2, ':', '|'))  # :|:|:
# char1 по умолчанию имеет значение "-",
# но мы его заменяем на :
# char2 по умолчанию имеет значение "*",
# но мы его заменяем на |


print(f(3))  # -*-*-*-


print(f(char1='+', char2='#'))
