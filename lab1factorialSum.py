
rangee = int(input("Enter range"))

fact = 1
res = 0

for i in range(1,rangee+1):
    fact = fact*i
    res =res +  i/fact
print(res)
