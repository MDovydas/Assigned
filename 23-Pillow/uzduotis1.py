from PIL import Image
import requests
import os

img_ = requests.get("https://github.com/robotautas/kursas/blob/master/PIL/logo.png?raw=true")
im = open("logo.png", "wb")
im.write(img_.content)
im.close()
im = Image.open("logo.png")
# print(im.size)
# im.show()
box = (0, 28, 128, 100)
crop_image = im.crop(box)
crop_image.show()
crop_image.save("new_logo.png")
print(crop_image.size)
os.remove("logo.png")