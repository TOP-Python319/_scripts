# сравнение чисел

bool(1)
# True
bool(10)
# True
bool(0)
# False
bool(0.0)
# False
1 == 1
# True
2 == 2
# True
2 == -2
# False
1 != 2
# True
0 != 2
# True
5 <= 7
# True
9 >= 7
# True
1 == '1'
# False
0 == 0.0
True


# сравнение строк

'a' == 'A'
# False
'a' == 'а'
# False
12 > 2
# True
'12' > '2'
# False
'!' < '?'
# True
':' < '.'
# False


# ord() и chr()
# ord() - order, принимает один символ str, выдаёт порядковый номер символа в таблице Unicode
# chr() - char, принимает число int, выдаёт символ по его порядковому номеру

ord('A')
# 65
ord('a')
# 97
'A' < 'a'
# True
ord('!')
# 33
ord('1')
# 49
chr(97)
# 'a'
chr(123)
# '{'
chr(124)
# '|'
chr(125)
# '}'
ord('a')
# 97
ord('а')
# 1072
'a' < 'а'
# True


# сравнение остальных последовательностей

[1, 2] < [1, 9]
# True
[1, 2] < [1, 9, 1]
# True
[1, 2] < [1, 9, 1, 5]
# True
[1, 2] < [1, 9, 1, 5, 1]
# True
[1, 2] < [1, 9, 'text']
# True