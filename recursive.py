no = int(input("Enter number"))

def fact(no):
    if no<=0:
        return 'invalid'
    elif no==1:
        return 1
    else:
        return  no * fact(no-1)

x = fact(no)
print(x)
