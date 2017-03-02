from PIL import Image, ImageColor, ImageDraw
import numpy as np
from modules import modulo_inverse_matrix as mim


def rgb_to_energy(rgb):
    hex_val = ""
    if type(rgb) == int:
        hex_to_add = hex(rgb)[2:]
        if len(hex_to_add) < 2:
            hex_val += "0" + hex_to_add
        else:
            hex_val += hex_to_add
    else:
        for color in rgb:
            hex_to_add = hex(color)[2:]
            if len(hex_to_add) < 2:
                hex_val += "0" + hex_to_add
            else:
                hex_val += hex_to_add

    return int(hex_val, 16)



def energy_to_rgb(energy):
    hex_string_total = "#"

    for color in energy:
        hex_string = hex(color)[2:]
        hex_string = ("0" * (2 * len(hex_string))) + hex_string
        hex_string_total += hex_string

    return ImageColor.getrgb(hex_string_total)


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
    im_r = np.empty([height, width], dtype=int)
    im_g = np.empty([height, width], dtype=int)
    im_b = np.empty([height, width], dtype=int)

    y = 0
    while y < height:

        x = 0
        while x < width:
            im_r[x,y] = rgb_to_energy((pix[x, y])[0])
            im_g[x,y] = rgb_to_energy((pix[x, y])[1])
            im_b[x,y] = rgb_to_energy((pix[x, y])[2])
            x += 1
        y += 1

    return (im_r, im_g, im_b)


color_mod = 255


def encrypt(image):
    im_matrix = color_array(image)
    n = image.size[1]
    key_matrix = mim.random_mod_matrix(0, color_mod, (n,n))
    cipher_matrix = mim.inverse_matrix(key_matrix, color_mod)
    print("ciph")
    scrambled_image_matrix = np.mod(np.dot(cipher_matrix, im_matrix), color_mod)
    return matrix_to_image(scrambled_image_matrix), matrix_to_image(key_matrix)


def decrypt(scrambled_image, key_image):
    scrambled_image_matrix = color_array(scrambled_image)
    key_matrix = color_array(key_image)
    unscrambled_matrix = np.mod(np.dot(key_matrix, scrambled_image_matrix), color_mod)
    return matrix_to_image(unscrambled_matrix)


# Testing
if __name__ == "__main__":
    im = Image.open("Images/2xtest.png")
    pix = im.load()
    im_r = np.empty([3, 3], dtype=int)
    im_r[2,2] = pix[0,0][0]
    print(im_r)
    # print(pix[0,0])
    # print(pix[0,1][0])
    # print(rgb_to_energy(pix[0,1]))
    # print(rgb_to_energy(pix[1,0]))
    # print(rgb_to_energy(pix[1,1]))
    # print(rgb_to_energy((255)))
    # print(color_array(im))
    # print(ImageColor.getrgb("#" + hex(16777215)[2:]))
    # print(energy_to_rgb(325))
    # a = color_array(im)
    # b = matrix_to_image(a)
    # b.save("TestResults/im_test.png")
    # (scr, key) = encrypt(im)
    # scr.save("TestResults/scr.png")
    # key.save("TestResults/key.png")
    # outAnswer = decrypt(scr, key)
    # outAnswer.save("TestResults/answer.png")

