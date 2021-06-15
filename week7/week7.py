"""
======Встречалось ли число раньше==========
list_of_ints = list(map(int, input().split()))
set_of_ints = set()

for i in list_of_ints:
    if i in set_of_ints:
        print("YES")
    else:
        print("NO")
        set_of_ints.add(i)
"""
"""
==========Страны и города===========

number_of_countries = int(input())
dict_of_cities = dict()

for i in range(number_of_countries):
    input_string_list = list(input().split())
    for j in input_string_list[0:]:
        dict_of_cities[j] = input_string_list[-1]

number_of_cities = int(input())
input_list = []
for i in range(number_of_cities):
    input_list.append(input())

for i in input_list:
    print(dict_of_cities[i])
"""
"""
==========Номер появления слова============
file = open("input.txt", "r")
list_of_words = file.read().split()
counts = dict()
output = ''
for word in list_of_words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 0
    output = output + str(counts[word]) + ' '

print(output)
file.close()
"""
"""
========= Словарь синонимов ========

n = int(input())
dict_of_sins = dict()
for i in range(n):
    pair = input().split()
    dict_of_sins[pair[0]] = pair[1]
    dict_of_sins[pair[1]] = pair[0]

print(dict_of_sins[input()])
"""
"""
=========Выборы в США==========

file = open("input.txt", "r")
candidates = dict()
for line in file.readlines():
    temp = line.split()
    if temp[0] in candidates:
        candidates[temp[0]] += int(temp[1])
    else:
        candidates[temp[0]] = int(temp[1])

names = list(candidates.keys())
names.sort()
for i in names:
    print(i, candidates[i])
"""
"""
======== Самое частое слово ===========

file = open("input.txt", "r")
text = file.read().split()
words_counter = dict()
for word in text:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

list_of_values = list(words_counter.values())
list_of_values.sort()
max_value = list_of_values[-1]
list_of_max = []
for i in words_counter:
    if words_counter[i] == max_value:
        list_of_max.append(i)
list_of_max.sort()
print(list_of_max[0])
"""

