def suming(n):
    sum = 0
    for x in range (n+1):
        sum += x
    return sum    

print(suming(int(input("enter the number: "))))
