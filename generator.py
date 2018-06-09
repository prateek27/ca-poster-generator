import xlrd
from PIL import Image
from PIL import Image, ImageDraw, ImageFont


file_location="/Users/jasjyotsingh/Documents/CB_Intern/CA_poster/elective.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

#sheet = workbook.sheet_by_name()
#print(sheet.cell_value(0,0))

for row in range(1, sheet.nrows):
    img= Image.open('poster.jpg')

    name=str(sheet.cell_value(row,3))
    ph=str(sheet.cell_value(row,1))
    code=str(int(sheet.cell_value(row,2)))
    
    img.save(str(code) + '.jpg')

    font_type_name = ImageFont.truetype('Arial.ttf', 100)
    font_type_ph = ImageFont.truetype('Arial.ttf', 85)
    font_type_code = ImageFont.truetype('Arial.ttf', 150)

    draw = ImageDraw.Draw(img)
    draw.text(xy=(2020,2580), text=name, fill=(255,69,0),font=font_type_name)
    draw.text(xy=(2080,2700), text=ph, fill=(255,69,0),font=font_type_ph)
    draw.text(xy=(2130,1720), text=code, fill=(255,69,0),font=font_type_code)
    
    img.save(str(code) + '.jpg')

    



