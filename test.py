from openpyxl import load_workbook

excel=load_workbook(filename='/Users/biao.huang/Downloads/公海客户20230717132557.xlsx',read_only=True)
ws = excel.get_sheet_by_name('Sheet1')
rows=ws.rows
max_row=ws.max_row #获取行数
#max_column=ws.max_column #获取列数