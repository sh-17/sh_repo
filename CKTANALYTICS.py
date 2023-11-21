import xlrd
import numpy as np

location = ("MYDATA.xlsx")
openfile = xlrd.open_workbook(location)
sheet = openfile.sheet_by_index(0)

print(sheet.cell_value(0,0))
