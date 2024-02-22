# (<выражение> for <переменная цикла> in <итерируемый объект> if <условие>)

# 2. Дополните приведенный код, используя списочное выражение, 
# так чтобы получить новый список, 
# содержащий длины строк исходного списка.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(word) for word in keywords]

print(lengths)

##################################################