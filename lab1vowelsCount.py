
def is_vowel(n):
    n = n.lower()
    if (n == 'a' or n=='e' or n=='i' or n=='o' or n=='u'):
        # print("true")
        return True
    else:
        # print("false") 
        return False

# is_vowel('t')

def main(word):
    count = 0
    for ch in word:
        if is_vowel(ch) == True:
            count = count + 1
    print(count)            

name = str(input("enter string: "))
main(name)    