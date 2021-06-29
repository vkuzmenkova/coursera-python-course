set_of_possibles = set(range(1, int(input()) + 1))
temp_set = set()
updated_possibles = set_of_possibles
line = ''

while line != 'HELP':
    line = input()
    if line == 'YES':
        updated_possibles.intersection_update(temp_set)
    elif line == 'NO':
        set_of_possibles -= temp_set
    elif line == 'HELP':
        for num in sorted(updated_possibles):
            print(num, end=' ')
        break
    else:
        temp_set = set(map(int, line.split()))
