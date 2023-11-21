from _datetime import *

dt = datetime.now()
print(dt)

print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.year)
print(dt.month)
print(dt.date)

output1=dt.strftime('%a')
print(output1)

output2=dt.strftime('%A')
print(output2)

output3=dt.strftime('%b')
print(output3)

output4=dt.strftime('%B')
print(output4)

output5=dt.strftime('%y')
print(output5)

output6=dt.strftime('%Y')
print(output6)

output7=dt.strftime('%H')
print(output7)

output8=dt.strftime('%I')
print(output8)

output9=dt.strftime('%p')
print(output9)

output10=dt.strftime('%j')
print(output10)

output11=dt.strftime('%U')
print(output11)

output12=dt.strftime('%w')
print(output12)

output13=dt.strftime('%X')
print(output13)


