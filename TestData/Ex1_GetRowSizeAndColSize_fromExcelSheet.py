import openpyxl


#issue with ( ) in project name
workbook=openpyxl.load_workbook("D:\Python\Workspace\8thNov_pytestFramework\TestData\SwagLab.xlsx")
sheet=workbook['Sheet2']


rowSize=sheet.max_row
print(rowSize)


colSize=sheet.max_column    #return col size of 1st row
print(colSize)
