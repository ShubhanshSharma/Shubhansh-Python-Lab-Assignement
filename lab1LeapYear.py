year = int(input("enter a Year"))

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print("it's leap")
    
else: print("not a leap")        