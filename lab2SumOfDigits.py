
def sum(n):
    # converting int to string to read each digit
    str_n = str(n)

    sum = 0

    # reading each digit
    for digit in str_n:
        sum = sum + int(digit)
    
    return sum

print(sum(int(input("enter no: "))))