from PIL import Image, ImageColor, ImageDraw
import numpy as np
from modules import modulo_inverse_matrix as mim



color_mod = 255

def matricies_to_image(rgb):
    (height, width) = rgb[0].shape
    image = Image.new("RGB", (width, height), (255, 255, 255))
    pix = image.load()

    y = 0
    while y < height:

        x = 0
        while x < width:
            pix[x,y] = (rgb[0])[x][y], (rgb[1])[x][y], (rgb[2])[x][y]
            x += 1
        y += 1

    return image

def inv_color_matrix(rgb):
    return mim.inverse_matrix(rgb[0], color_mod), mim.inverse_matrix(rgb[1], color_mod), mim.inverse_matrix(rgb[2], color_mod)

def random_color_matrix(n):
    return mim.random_mod_matrix(0, color_mod, (n,n)), mim.random_mod_matrix(0, color_mod, (n,n)), mim.random_mod_matrix(0, color_mod, (n,n))



def encrypt(image):
    n = image.size[1]

    # Generate ciphers and keys for each color
    cipher_matricies = random_color_matrix(n)
    key_matricies = inv_color_matrix(cipher_matricies)
    test = inv_color_matrix(key_matricies)
    test_im = matricies_to_image(test)
    print(cipher_matricies[2])
    print(test[2])

    cipher_image = matricies_to_image(cipher_matricies)
    key_image = matricies_to_image(key_matricies)
    return cipher_image, key_image, test_im

# Testing
if __name__ == "__main__":
    im = Image.open("Images/2xtest.png")
    (scr, key, check) = encrypt(im)
    check.save("TestResults/check.png")
    scr.save("TestResults/scr.png")
    key.save("TestResults/key.png")
    # outAnswer = decrypt(scr, key)
    # outAnswer.save("TestResults/answer.png")

