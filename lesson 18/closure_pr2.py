# создать функцию-замыкание create_summator, она должна суммировать в себе все значения, 
# которые ей
# будут переданы, можно менять значение по умолчанию с нуля, на другое число.

def create_summator(count=0):
    
    def summator(value):
        nonlocal count
        count += value
        return count
    return summator


summator_1 = create_summator(count=10)
print(summator_1(value=1))  # 11
print(summator_1(value=3))  # 14
print(summator_1(value=5))  # 19

print('######################')
summator_2 = create_summator(count=-10)
print(summator_2(value=10))  # 0
print(summator_2(value=-2))  # -2
print(summator_2(value=7))  # 5

print('######################')
summator_3 = create_summator(count=0)
print(summator_3(value=1))  # 1
print(summator_3(value=-2))  # -1
print(summator_3(value=-10))  # -11