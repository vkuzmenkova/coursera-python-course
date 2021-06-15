"""
В выборах Президента Российской Федерации побеждает кандидат,
набравший свыше половины числа голосов избирателей.
Если такого кандидата нет, то во второй тур
выборов выходят два кандидата, набравших наибольшее число голосов.

"""

election_results = {}
number_of_votes = 0

file = open('input.txt', 'r', encoding="utf-8")

for line in file:
    temp = line.rstrip()
    if temp in election_results:
        election_results[temp] += 1
    else:
        election_results[temp] = 1
    number_of_votes += 1

file.close()

is_winner_found = False

file = open('output.txt', 'w', encoding="utf-8")

for result in election_results:
    if election_results[result] > number_of_votes / 2:
        is_winner_found = True
        file.write(result)

if not is_winner_found:
    list_d = list(election_results.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    file.write(list_d[0][0] + '\n')
    file.write(list_d[1][0] + '\n')

file.close()
