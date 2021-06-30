def merge(list1, list2):
    if len(list1) < len(list2):
        list1, list2 = list2, list1
    i = 0
    j = 0
    final_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        elif list1[i] >= list2[j]:
            final_list.append(list2[j])
            j += 1
    if i == len(list1):
        while j < len(list2):
            final_list.append(list2[j])
            j += 1
    else:
        while i < len(list1):
            final_list.append(list1[i])
            i += 1
    return final_list


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*merge(list1, list2))
