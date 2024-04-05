with open("test.txt", "w", encoding='utf-8') as test_text:
    print('Hello World!', file=test_text)
    print('Good bye!', file=test_text)

with open("test.txt", "w", encoding='utf-8') as test_text:
    print('Hi World!', 'GBye!', 'Hello Again', sep='\n', end='######', file=test_text)

l = ['Tbilisi', 'Ankara', 'Istanbul', 'Moscow', 'Minsk']
with open("test.txt", "w", encoding='utf-8') as test_text:
    print(*l, sep='\n', file=test_text)