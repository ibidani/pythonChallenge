from PIL import Image

img = Image.open("oxygen.png")
rows = img.size[0]
cols = img.size[1]
count = ""
for x in range(1,rows,7):
    pix = img.getpixel((x,45))
    if pix[0] == pix[1] == pix[2]:
        count = count +str(unichr(pix[0]))
print count
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
# integrity