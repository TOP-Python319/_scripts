command = input('\nвведите команду >>: ')
print('Первый цикл')
while command != 'уйти':
    print(command.upper())
    command = input('\nвведите команду >>: ')
else:
    print('Оператор else сработал')


print('Второй цикл')
while True:
    if command == 'выход':
        break
    if command == 'exit':
        break
    print(command.upper())
    command = input('\nвведите команду >>: ')
else:
    print('оператор else не сработал')


print('Третий цикл')
# такой же как и первый цикл, но мы объединили первую и третью строку
while (command := input('\nвведите команду >>: ')) != 'exit':
    print(command.upper())
else:
    print('Оператор else сработал')