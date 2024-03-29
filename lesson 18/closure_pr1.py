# def counter():
#     count = 0

#     def increment():
#         nonlocal count 
#         count += 1
#         return count

#     return increment

# создать функцию-замыкание create_summator, она должна суммировать в себе все значения, 
# которые ей
# будут переданы, по умолчанию сумму равна нулю.

def create_summator():
    count = 0
    def summator(value):
        nonlocal count
        count += value
        return count
    return summator

summator_1 = create_summator()
print(summator_1(1))  # 1
print(summator_1(3))  # 4
print(summator_1(5))  # 9

print('######################')
summator_2 = create_summator()
print(summator_2(10))  # 10
print(summator_2(-2))  # 8
print(summator_2(7))  # 15

print('######################')
summator_3 = create_summator()
print(summator_3(1))  # 1
print(summator_3(-2))  # -1
print(summator_3(-10))  # -11
