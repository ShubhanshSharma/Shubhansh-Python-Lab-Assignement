list1 = [86, 7, 20, 60, 2, 5]

list2 = [86,60,20,7,5,2]

def sorted_check(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


print("list is sorted: ", sorted_check(list2))