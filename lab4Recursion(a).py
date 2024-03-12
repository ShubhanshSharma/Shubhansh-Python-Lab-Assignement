def int_part(n):
    if n < 1:
        return
    int_part(n//2)
    print( n%2 , end="")

def fraction_part(n, bit = 8):
    if bit==0:
        return
    n=n*8
    print(int(n), end="")
    fraction_part( n-int(n) , bit-1)

num = float(input("enter number: "))\

int_part(int(num))
print( "." , end="")
fraction_part(num - int(num)) 