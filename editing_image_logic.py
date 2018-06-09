from PIL import Image, ImageDraw, ImageFont

img= Image.open('poster.jpg')
img.save('poster3.jpg')

font_type_name = ImageFont.truetype('Arial.ttf', 100)
font_type_ph = ImageFont.truetype('Arial.ttf', 85)
font_type_code = ImageFont.truetype('Arial.ttf', 150)

draw = ImageDraw.Draw(img)
draw.text(xy=(2020,2580), text="Jasjyot Singh", fill=(255,69,0),font=font_type_name)
draw.text(xy=(2080,2700), text="9760782624", fill=(255,69,0),font=font_type_ph)
draw.text(xy=(2130,1720), text="CB1001", fill=(255,69,0),font=font_type_code)

img.save('poster3.jpg')
