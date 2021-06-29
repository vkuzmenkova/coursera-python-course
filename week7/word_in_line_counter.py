"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте,
сколько раз оно встречалось в этом тексте ранее.
"""
file = open("input.txt", "r")
list_of_words = file.read().split()
file.close()
counts = {}
for word in list_of_words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 0

    print(counts[word], end=" ")