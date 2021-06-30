def CountSort(array):
    count_array = [0 for i in range(101)]
    final_array = []

    for i in array:
        count_array[i] += 1

    for i in range(len(count_array)):
        if count_array[i] != 0:
            for j in range(count_array[i]):
                final_array.append(i)

    return final_array


print(*CountSort(list(map(int, input().split()))))
