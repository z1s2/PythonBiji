import requests
import re
import csv
import xlrd

# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据

data = xlrd.open_workbook('人员会议室数据名单.xlsx') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
for i in range(nrows): # 循环逐行打印
    if i == 0: # 跳过第一行
        continue
    print('table.row_values(i)[:13]') # 取前十三列