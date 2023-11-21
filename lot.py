import random2
usernos = []
luckynos = []
count = 0

for i in range(0,5):
    no = int(input("Enter numbers between 1 to 9:"))
    usernos.append(no)

for i in range(0,5):
    rno = random2.randint(1,9)
    luckynos.append(rno)

print(usernos)
print(luckynos)

for i in range(0,5):
    if usernos[i] == luckynos[i]:
        count = count+1
print("total matched numbers:",count)