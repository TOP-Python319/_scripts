text = 'python is not a snake'

text
# 'python is not a snake'
text[0:6]
# 'python'
text[6:9]
# ' is'
text[7:9]
# 'is'
text[10:13]
# 'not'
text
# 'python is not a snake'
id(text)
# 140648514282528
id(text[0:6])
# 140648514381808
id(text[0:6])
# 140648514381808
text[2:-2]
# 'thon is not a sna'

quote = '"Умная цитата"'
print(quote)
# "Умная цитата"
quote[0:-1]
# '"Умная цитата'
print(quote[0:-1])
# "Умная цитата
print(quote[1:-1])
# Умная цитата