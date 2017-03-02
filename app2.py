from PIL import Image, ImageColor, ImageDraw
import numpy as np
from modules import modulo_inverse_matrix as mim



color_mod = 256

def image_to_matricies(image):
    width, height = image.size
    pix = image.load()
    im_r = np.empty([height, width], dtype=int)
    im_g = np.empty([height, width], dtype=int)
    im_b = np.empty([height, width], dtype=int)

    y = 0
    while y < height:

        x = 0
        while x < width:
            im_r[x,y] = (pix[x, y])[0]
            im_g[x,y] = (pix[x, y])[1]
            im_b[x,y] = (pix[x, y])[2]
            x += 1
        y += 1

    return (im_r, im_g, im_b)



def matricies_to_image(rgb):
    (width, height) = rgb[0].shape
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

def trip_mod_dot(m1, m2, mod):
    print("trip mod: ", np.mod(np.dot(m1[0], m2[0]), mod))
    return np.mod(np.dot(m1[0], m2[0]), mod), np.mod(np.dot(m1[1], m2[1]), mod), np.mod(np.dot(m1[2], m2[2]), mod)

def inv_color_matrix(rgb):
    return mim.inverse_matrix(rgb[0], color_mod), mim.inverse_matrix(rgb[1], color_mod), mim.inverse_matrix(rgb[2], color_mod)

def random_color_matrix(n):
    return mim.random_mod_matrix(0, color_mod, (n,n)), mim.random_mod_matrix(0, color_mod, (n,n)), mim.random_mod_matrix(0, color_mod, (n,n))


def encrypt(image):
    n = image.size[1]

    # Generate ciphers and keys for each color
    cipher_matricies = random_color_matrix(n)
    key_matricies = inv_color_matrix(cipher_matricies)
    cipher_image = matricies_to_image(cipher_matricies)

    input_image_matricies = image_to_matricies(image)
    scr_image_matricies = trip_mod_dot(cipher_matricies, input_image_matricies, color_mod)
    scr_image = matricies_to_image(scr_image_matricies)
    key_image = matricies_to_image(key_matricies)
    print("scr matricies:")
    for x in range(0,3):
        print(scr_image_matricies[x])

    return scr_image, key_image


def decrypt(scr_im, key_image):
    scr_matricies = image_to_matricies(scr_im)
    key_matricies = image_to_matricies(key_image)
    print("scr check:")
    for x in range(0,3):
        print(scr_matricies[x])
    unscr_matricies = trip_mod_dot(key_matricies, scr_matricies, color_mod)
    for x in range(0,3):
        print(unscr_matricies[x])
    return matricies_to_image(unscr_matricies)



# Testing
if __name__ == "__main__":
    im = Image.open("Images/2xtest.png")
    # pix = im.load()
    # print(pix[0,0])
    # print(pix[0,1])
    # print(pix[1,0])
    # print(pix[1,1])
    # f= image_to_matricies(im)
    # print(f[0])
    # print(f[1])
    # print(f[2])
    (scr, key) = encrypt(im)
    scr.save("TestResults/scr.png")
    key.save("TestResults/key.png")
    outAnswer = decrypt(scr, key)
    outAnswer.save("TestResults/answer.png")

