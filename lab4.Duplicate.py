
def rem(list):
    unique_list = []

    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


example = [1, 2, 3, 2, 4, 5, 1, 3]

print("List with duplicates removed:", rem(example))
