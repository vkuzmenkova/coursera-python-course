n = int(input())
places = list(map(int, input().split()))

m = int(input())
shelter_distances = input().split()

shelters = []
for i in range(m):
    shelters.append((int(shelter_distances[i]), i + 1))
shelters.sort()

for place in places:
    if place > shelters[-1][0]:
        answer = shelters[-1][1]
    elif place < shelters[0][0]:
        answer = shelters[0][1]
    else:
        min = 0
        max = len(shelters) - 1
        while max - min > 1:
            mid = (min + max) >> 1
            if place > shelters[mid][0]:
                min = mid
            else:
                max = mid

        if place - shelters[min][0] < shelters[max][0] - place:
            answer = shelters[min][1]
        else:
            answer = shelters[max][1]

    print(answer, end=' ')
print()
