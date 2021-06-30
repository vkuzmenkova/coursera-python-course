in_file = open('input.txt', 'r', encoding='utf8')
out_file = open('output.txt', 'w', encoding='utf8')

participants = []

for line in in_file:
    temp = line.split()
    participants.append((temp[0], temp[1], temp[3]))

participants.sort()

for line in participants:
    print(*line, file=out_file)

in_file.close()
out_file.close()
