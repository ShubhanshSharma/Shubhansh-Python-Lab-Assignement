
def find(list):
    sm, la = list[0], list[0]

    for x in list:
        if x > la:
            la = x
        if x < sm:
            sm = x
        
    print(f"\nlargest no. is {la} \n\nsmallest no. is {sm}\n")    


example = [8999,4,3,2,1]

find(example)