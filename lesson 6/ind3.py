simple_list = [1, 3, 5, 7, 11, 13, 17, 19, 23]
nested_list = [['Россия', 'Москва'], ['Грузия', 'Тбилиси'], ['Турция', 'Анкара']]

len(simple_list)
# 9
simple_list[0]
# 1
simple_list[8]
# 23
nested_list[0]
# ['Россия', 'Москва']
type(nested_list[0])
# <class 'list'>
nested_list[0][1]
# 'Москва'
nested_list[0][1][0]
# 'М
city_1 = nested_list[0]
city_1
# ['Россия', 'Москва']
city_1[1]
# 'Москва'