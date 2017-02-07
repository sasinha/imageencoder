from PIL import Image
import numpy as np
from modules import modulo_inverse_matrix as mim


def rgb_to_energy(rgb):
    hex_val = ""
    for color in rgb:
        if len(str(color)) < 2:
            hex_val += "0" + hex(color)[2:]
        else:
            hex_val += hex(color)[2:]

    return int(hex_val, 16)


def color_array(image):
    width, height = image.size
    pix = image.load()
    image_matrix = np.empty([height, width])

    y = 0
    while y < height:

        x = 0
        while x < width:
            energy_val = rgb_to_energy(pix[x, y])
            image_matrix[x,y] = energy_val
            x += 1
        y += 1

    return image_matrix


if __name__ == "__main__":
    im = Image.open("Images/2xtest.png")
    pix = im.load()
    print(rgb_to_energy(pix[0,0]))
    print(rgb_to_energy(pix[0,1]))
    print(rgb_to_energy(pix[1,0]))
    print(rgb_to_energy(pix[1,1]))
    print(rgb_to_energy((255,9,9)))
    print(color_array(im))

