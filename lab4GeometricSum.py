# using Recursion:
a , b = 1, 1
def geo_sum( a, r, b):
    if n<b:
        return
    print(a, end=", ")
    if n == b:
        print("sum is: ", a)
        return
    
    geo_sum(a*r , r, b+1)
    

r = float(input("enter ratio: "))
n = int(input("enter range: "))    
print("series:", end=" ") 
geo_sum(1,r,1)