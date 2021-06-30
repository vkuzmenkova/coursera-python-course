file = open('input.txt', 'r', encoding="utf-8")
text = file.read().split('\n')
file.close()

k = int(text[0])
text.remove(text[0])
results = []


def scores_sum(x):
    return x[0] + x[1] + x[2]


for line in text:
    temp = list(map(int, line.split()[-3:]))
    if temp[0] >= 40 and temp[1] >= 40 and temp[2] >= 40:
        results.append(temp)

results.sort(key=scores_sum, reverse=True)
final_scores = list(map(scores_sum, results))
passed_score = final_scores[k - 1]
if final_scores.count(passed_score) > 1:
    passed_score = final_scores[final_scores.index(passed_score) - 1]

file = open('output.txt', 'w', encoding='utf-8')
file.write(str(passed_score))
file.close()
