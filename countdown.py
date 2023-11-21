from _datetime import *

dt = datetime.now()

hr = dt.hour
mn = dt.minute
se = dt.second

h = 23-hr
m = 59-mn
s = 59-se

print('Sales starts in: ',h,' hours ',m,' minutes and',s,' seconds')