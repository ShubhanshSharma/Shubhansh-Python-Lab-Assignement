
def check(n):
    str_n = str(n)
    rev = str_n[::-1]
    if (str_n == rev):
        print("it is palindrome")
    
    else: print("not")

print(check(int(input("enter number to check palindrome: "))))