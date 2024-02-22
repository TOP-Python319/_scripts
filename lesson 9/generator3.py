words = ['cat', 'rat', 'python', 'Kamchatka', 'water', 'affective']


words_lengths1 = []
for word in words:
    length_of_word = len(word)
    words_lengths1.append(length_of_word)
print(words_lengths1)


generator_object = (len(word) for word in words)
words_lengths2 = list(generator_object)
# words_lengths2 = list(len(word) for word in words)  # можно написать в одну строку
print(words_lengths2)


words_lengths3 = [len(word) for word in words]  # вместо того чтобы писать list(), мы можем написать генератор сразу в квадратных скобках
print(words_lengths3)