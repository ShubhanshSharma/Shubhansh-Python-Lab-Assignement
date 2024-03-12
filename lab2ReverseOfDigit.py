
def func(n):
    
    str_n = str(n)
    rev = ""
    for digit in str_n:
        rev = str(digit) + rev

    return rev

print(func(233))

# method 2
print(str("cmhgmktyssu")[ : : -1])