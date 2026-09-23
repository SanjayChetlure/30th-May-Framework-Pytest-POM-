import openpyxl

openpyxl.load_workbook()
workbook = openpyxl.load_workbook("D:\Python\Workspace\30th May Framework (Pytest+POM)\TestData\SwagLab.xlsx")
sheet=workbook['Sheet1']     #workbook.active


rowSize=sheet.max_row
print(rowSize)


colSize=sheet.max_column    #return col size of 1st row
print(colSize)
