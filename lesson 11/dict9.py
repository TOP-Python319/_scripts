# num = int(input())

# if num == 1:
#     description = 'one'
# elif num == 2:
#     description = 'two'
# elif num == 3:
#     description = 'three'
# else:
#     description = 'нет такого значения'


# print(description)


num = int(input())

description = {1: 'one', 2: 'two', 3: 'three'}
print(description.get(num, 'нет такого значения'))