m = 25
n = 35


def one():
    print(m + n)  # m and n are global variables


one()


def two():
    i = 40
    j = 50
    print(i + j)  # i and j are local variables


two()


# case 1:funciotn call insid other function

def three():
    print("function three called")


def four():
    print("function four called")

    three()


four()


# case 2: define and call function inside a function

def five():
    print("Five called")

    def six():
        print("six called")

    six()

five()

# case 3:define function inside a function and calle outside the function

def seven():
    print("Seven called")

    def eight():
        print("Eight called")


seven()
