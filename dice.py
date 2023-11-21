import random2

no = int(input("Enter number of dice"))

dice1 = random2.randint(1,6)
dice2 =random2.randint(1,6)

def d1(dice1):
    print('dice value:',dice1)
def d2(dice1,dice2):
    print('dice 1 value',dice1,'dice 2 value',dice2)

if no==1:
    d1(dice1)
elif no==2:
    d2(dice1,dice2)
else:
    print("Enter 1 or 2")
