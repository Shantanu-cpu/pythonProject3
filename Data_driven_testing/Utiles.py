# import openpyxl
#
#
# def No_of_rows(file_name, sheet_name):
#         workbook = openpyxl.load_workbook(file_name)
#         sheet = workbook.get_sheet_by_name(sheet_name)
#         return sheet.max_row
#
# def No_of_col(file_name, sheet_name):
#         workbook = openpyxl.load_workbook(file_name)
#         sheet = workbook.get_sheet_by_name(sheet_name)
#         return sheet.max_column
#
# def read_data(file_name, sheet_name, rownum, colnum):
#         workbook = openpyxl.load_workbook(file_name)
#         sheet = workbook.get_sheet_by_name(sheet_name)
#         return sheet.cell(rownum, colnum).value
#
# def write_data(file_name, sheet_name, rownum, colnum, data):
#         workbook = openpyxl.load_workbook(file_name)
#         sheet = workbook.get_sheet_by_name(sheet_name)
#         sheet.cell(rownum, colnum).value = data
#         workbook.save(file_name)
#
#
#
# class Form:
#         def row(self,filename,sheet):
#                 workbook=openpyxl.load_workbook(filename)
#                 sheet=workbook.get_sheet_by_name(sheet)
#                 return sheet.max_row
#
#
#         def col(self,filename,sheet):
#                 workbook=openpyxl.load_workbook(filename)
#                 sheet=workbook.get_sheet_by_name(sheet)
#                 return sheet.max_column
#
#
#
#         def read(self,filename,sheet,rownum,colnum):
#                 workbook=openpyxl.load_workbook(filename)
#                 sheet=workbook.get_sheet_by_name(sheet)
#                 return sheet.cell(rownum,colnum).value
#
#
#         def write(self,filename,sheet,rownum,colnum,data):
#                 workbook=openpyxl.load_workbook(filename)
#                 sheet=workbook.get_sheet_by_name(sheet)
#                 sheet.cell(rownum,colnum).value=data
#                 workbook.save(filename)






















































