
def add_items(list):
    total = 0
    for item in list:       
            total += item
    return total

example = [1, 2, 3, 4, 5]

print("Sum of items in the list:", add_items(example))
