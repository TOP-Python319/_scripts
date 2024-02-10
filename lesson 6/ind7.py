digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1-ый элемент = 1
# прибавали шаг +2, 3-ий элемент = 3

digits[1:7]
# [1, 2, 3, 4, 5, 6]
digits[1:7:2]
# [1, 3, 5]
digits[1:7:1]
# [1, 2, 3, 4, 5, 6]
digits[1:7:2]
# [1, 3, 5]
digits[1:7:3]
# [1, 4]

digits_2 = digits[1:7]
digits[0]
# 0
digits_2[0]
# 1
digits[::2]
# [0, 2, 4, 6, 8]
digits[::-1]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
digits[::-2]
# [9, 7, 5, 3, 1]
digits[-2::-2]
# [8, 6, 4, 2, 0]

text = 'python is not a snake'
text[0:6] + text[-1:-5]
# 'python'
text[0:6] + text[-5:-1]
# 'pythonsnak'
text[0:6] + text[-7:-1]
# 'pythona snak'
text[0:6] + text[-6:-1]
# 'python snak'
text[0:6] + text[-6:]
# 'python snake'