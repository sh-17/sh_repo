from _datetime import *

dt = datetime.now()

hr = dt.hour
d = dt.strftime('%w')

print(hr)
print(type(hr))
print(d)
print(type(d))

if d=="1" or d=="6":
    if hr==10 or hr==11:
        print("50% off")