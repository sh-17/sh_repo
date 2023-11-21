import numpy as np
import xlrd

location = ("MYDATA.xlsx")
openfile = xlrd.open_workbook(location)
sheet = openfile.sheet_by_index(0)

print(sheet)