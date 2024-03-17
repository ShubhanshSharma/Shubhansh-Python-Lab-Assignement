


n = int(input("enter the range: "))

mult = lambda x: x*10 

table = [mult(num) for num in range(1,n+1)]

print("the table is", table)