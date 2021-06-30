n = int(input())
results = []
for i in range(n):
    line = input().split()
    results.append([line[0], int(line[1])])

results.sort(key=lambda x: x[1], reverse=True)

for i in results:
    print(i[0])
