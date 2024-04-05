l = ['Tbilisi\n', 'Ankara\n', 'Istanbul\n', 'Moscow\n']

with open("test.txt", "w", encoding='utf-8') as test_text:
    test_text.writelines(l)
    test_text.seek(0)
    # print(test_text.read())  не работает в режиме 'w'

print()