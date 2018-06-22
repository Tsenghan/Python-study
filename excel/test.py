'''功能-将excel中的数据导入为列表。'''
#导入模块
import openpyxl
from openpyxl import *
#导入工作簿文件
book1 = load_workbook('test.xlsx')
#导入工作表
sheet1 = book1['Sheet1']
#获取数据总行数
row_total = sheet1.max_row

list = []
for i in range(row_total):
    #index为单元格的名称，默认数据放在A:A列
    index = 'B'+str(i+1)
    #获取单元格值
    cell_temp  = sheet1[index].value
    #扩充列表
    list.append(cell_temp)
print(list)
