"""
Дан текст. Выведите все слова, встречающиеся
в тексте, по одному на каждую строку.
Слова должны быть отсортированы
по убыванию их количества появления в тексте,
а при одинаковой частоте
появления — в лексикографическом порядке.
"""

file = open('input.txt', 'r')
text = file.read().split()
file.close()

dict_of_words = {}

for word in text:
    if word in dict_of_words:
        dict_of_words[word] += 1
    else:
        dict_of_words[word] = 0

list_of_frequencies = []

for freq in dict_of_words:
    temp_tuple = (dict_of_words[freq], freq)
    list_of_frequencies.append(temp_tuple)

sorted_list = sorted(list_of_frequencies, reverse=True)

final_dict = {}

for item in sorted_list:
    if item[0] in final_dict:
        final_dict[item[0]].append(item[1])
    else:
        final_dict[item[0]] = [item[1]]

for item in final_dict:
    temp = sorted(final_dict[item])
    for word in temp:
        print(word)
