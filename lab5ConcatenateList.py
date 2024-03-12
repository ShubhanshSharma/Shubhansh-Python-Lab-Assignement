
def concatenate(list , n):
    concatenated_list = []
    for x in range (1, n+1):
        for y in list:
            x = str(x)
            concatenated_list += {y+x}
            
    print(concatenated_list)

example = [ 'p' , 'q' ]            
concatenate(example,5)