import xlrd
from PIL import Image

file_location="/Users/jasjyotsingh/Documents/CB_Intern/CA_poster/ca_data.xl"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
#sheet = workbook.sheet_by_name()
#print(sheet.cell_value(0,0))

for row in range(sheet.nrows):
    name=sheet.cell_value(row,0)
    ph=sheet.cell_value(row,1)
    code=sheet.cell_value(row,2)
    img=Image.open('poster.jpg')


