import qrcode
from PIL import Image, ImageDraw ,ImageFont
fnt = ImageFont.truetype('static/include/font/Arial.ttf', 18)
qr = qrcode.make('tor_na_ja')
draw = ImageDraw.Draw(qr)
draw.text((145,260),text = "test",font=fnt)
qr.show()
#qr.save('myqrcode.jpg')
