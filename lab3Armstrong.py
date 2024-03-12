
def armstrong(n):
    str_n = str(n)
    power = 0
    sum = 0
    for y in str_n:
        power += 1 
    # print(power)
    for x in str_n:
        sum = sum + int(x)**power    
        
    if (n == int(sum)):
        print(" it is armstrong")
    else: print("not")

armstrong(int(input("enter no:  ")))