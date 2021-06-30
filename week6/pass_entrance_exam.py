in_file = open("input.txt", "r", encoding="utf8")
k = int(in_file.readline())
results = []

for line in in_file:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        results.append(newLine)

in_file.close()

results.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]), reverse=True)

final = []
for i in results:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    final.append(sum)
n = len(final)


def contest(n, k, in_list):
    if n <= k:
        return 0
    elif in_list[k] == in_list[0]:
        return 1
    for i in range(k, 0, -1):
        if in_list[i] < in_list[i - 1]:
            return in_list[i - 1]


out_file = open("output.txt", "w", encoding="utf8")
out_file.write(str(contest(n, k, final)))
out_file.close()
