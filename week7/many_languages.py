data = []

for i in range(int(input())):
    temp = []
    for j in range(int(input())):
        temp.append(input())
    data.append(temp)

everybody_knows = set(data[0])
at_least_one_knows = set(data[0])

for item in data:
    everybody_knows.intersection_update(set(item))
    at_least_one_knows.update(set(item))

print(len(everybody_knows))
for lang in everybody_knows:
    print(lang)
print(len(at_least_one_knows))
for lang in at_least_one_knows:
    print(lang)
