from sympy import isprime

n = int(input("input number"))

if (isprime(n)):
    print("its prime")
else:
    print("not prime")



# n = int(input("input number"))
# # b = False
# for x in range(2, n-1):
#     if(n % x == 0):
#         b = True
#         break
#     else: b = False

# if(b == True):
#     print("not a prime")

# else: print('prime')
