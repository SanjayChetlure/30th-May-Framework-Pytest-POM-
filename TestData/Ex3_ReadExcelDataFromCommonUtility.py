from Utility.CommonFunction import UtilityClass

data1=UtilityClass.readDataFromExcel(1,1)
print(data1)

data2=UtilityClass.readDataFromExcelWithSheetName("Sheet2",1,1)
print(data2)