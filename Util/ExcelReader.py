# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = "E:/Testdata.xlsx"

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
Username = sheet.cell_value(1, 0)
Password = sheet.cell_value(1, 1)

