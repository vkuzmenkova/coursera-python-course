file = open("input.txt", "r", encoding="utf-8")
text = file.read().split('\n')
file.close()

participants = []

for line in text:
    temp = line.split()
    participants.append([f"{temp[0]} {temp[1]}", int(temp[3])])

participants.sort(key=lambda x: x[0])

file = open("output.txt", "w", encoding="utf-8")

for i in range(len(participants) - 1):
    file.write(f"{participants[i][0]} {participants[i][1]}\n")
file.write(f"{participants[i][0]} {participants[i][1]}")

file.close()
