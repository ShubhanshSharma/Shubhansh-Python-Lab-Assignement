
def fibonacci(a):
    
    m = 0
    n = 1

    for x in range (a):
        sum = m + n
        n = m
        m = sum

    return sum

print(fibonacci(int(input("enter the range: "))))    
