import Image
import ImageEnhance

image = Image.open('cave.jpg')

for x in xrange(image.size[0]):
    for y in xrange(image.size[1]):
        if (x + y) % 2 != 0:
            image.putpixel((x, y), (0, 0, 0))

bright = ImageEnhance.Brightness(image)
image = bright.enhance(2.5)
contrast = ImageEnhance.Contrast(image)
image = contrast.enhance(3.0)
image.show()
image.save('cave2.png')