file = open("input.txt", "r", encoding="utf8")
text = file.read().split('\n')
file.close()

participants = []

for line in text:
    temp = line.split()
    participants.append([f"{temp[0]} {temp[1]}", int(temp[3])])

participants.sort(key=lambda x: x[0])

file = open("output.txt", "w", encoding="utf8")
for i in participants:
    file.write(f"{i[0]} {i[1]}\n")
file.close()
