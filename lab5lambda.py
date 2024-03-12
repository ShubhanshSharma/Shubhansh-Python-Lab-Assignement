
numbers = [1, 2, 3, 4, 5, 8, 16, 32, 64]

check = lambda x: x != 0 and (x == 1 or (x % 2 == 0 and check(x // 2)))

# lambda function returns true or false only for each item in the iterable 


# Filter funciton: 2 arguments:- 
#                               a. function: it could return true or false
#                               b. iterable: list or array
print("Numbers in the list that are powers of 2 without using bits:", list(filter(check, numbers)))
