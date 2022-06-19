from PIL import Image, ImageEnhance


# image = Image.open("new_logo.png")


def image_enhance(image_name, contrast, color, sharpness, brightness, save=False):
    image = Image.open(image_name)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Color(image).enhance(color)
    image = ImageEnhance.Sharpness(image).enhance(sharpness)
    image = ImageEnhance.Brightness(image).enhance(brightness)
    if save:
        image.save(image_name.replace(".", "_") + "_edited.png")
    image.show()


image_enhance("new_logo.png", 3, 3, 3, 3, True)
