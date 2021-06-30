in_file = open('input.txt', 'r', encoding='utf8')
out_file = open('output.txt', 'w', encoding='utf8')

participants = []

for line in in_file:
    line1 = line.split()
    participants.append((line1[0], line1[1], line1[3]))

participants.sort()

for line in participants:
    print(*line, file=out_file)

in_file.close()
out_file.close()
