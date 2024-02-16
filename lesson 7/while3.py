# i = 0
# while i < 10:
#     print(i)
#     # i = i + 1
#     i += 1

i = 0
j = 10
while i < 10 or j != 0:
    print(f'{i = }', end=' ')
    print(f'{j = }')
    i += 1
    j -= 1

print(f'После завершения цикла: {i = }')
print(f'После завершения цикла: {j = }')
