from PIL import Image, ImageColor, ImageDraw
import numpy as np
from modules import modulo_inverse_matrix as mim


def rgb_to_energy(rgb):
    hex_val = ""
    for color in rgb:
        hex_to_add = hex(color)[2:]
        if len(hex_to_add) < 2:
            hex_val += "0" + hex_to_add
        else:
            hex_val += hex_to_add

    return int(hex_val, 16)


def energy_to_rgb(energy):
    hex_string = hex(energy)[2:]
    buffer = ""

    while len(buffer + hex_string) < 6:
        buffer += "0"

    hex_string = buffer + hex_string

    return ImageColor.getrgb("#" + hex_string)


def matrix_to_image(image_matrix):
    (height, width) = image_matrix.shape
    image = Image.new("RGB", (width, height), (255, 255, 255))
    pix = image.load()

    y = 0
    while y < height:

        x = 0
        while x < width:
            pix[x,y] = energy_to_rgb(image_matrix[x][y])
            x += 1
        y += 1

    return image


def color_array(image):
    width, height = image.size
    pix = image.load()
    image_matrix = np.empty([height, width], dtype=int)

    y = 0
    while y < height:

        x = 0
        while x < width:
            energy_val = rgb_to_energy(pix[x, y])
            image_matrix[x,y] = energy_val
            x += 1
        y += 1

    return image_matrix


def encrypt(image, color_mod = 16777215):
    im_matrix = color_array(image)
    n = image.size[1]
    cipher_matrix = mim.random_mod_matrix(0, color_mod, (n,n))
    key_matrix = mim.inverse_matrix(cipher_matrix, color_mod)
    scrambled_image_matrix = np.mod(np.dot(cipher_matrix, im_matrix), color_mod)




if __name__ == "__main__":
    im = Image.open("Images/2xtest.png")
    pix = im.load()
    print(pix[0,0])
    print(pix[0,1])
    print(rgb_to_energy(pix[0,1]))
    print(rgb_to_energy(pix[1,0]))
    print(rgb_to_energy(pix[1,1]))
    print(rgb_to_energy((255,9,9)))
    print(color_array(im))
    print(ImageColor.getrgb("#" + hex(16777215)[2:]))
    print(energy_to_rgb(325))
    a = color_array(im)
    b = matrix_to_image(a)
    b.save("TestResults/im_test.png")

