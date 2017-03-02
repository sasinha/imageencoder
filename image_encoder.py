from PIL import Image
from modules import image_matrix_relation as imr
from modules import rgb_matrix_math as rgb_mm

color_mod = 256

def encrypt(image):
    # get dimensions for square image keys
    n = image.size[1]

    # Generate ciphers and keys for each color
    cipher_matricies = rgb_mm.random_color_matrix(n, color_mod)
    key_matricies = rgb_mm.inv_color_matrix(cipher_matricies, color_mod)
    input_image_matricies = imr.image_to_matricies(image)

    # Create scrambled image matricies
    scr_image_matricies = rgb_mm.trip_mod_dot(cipher_matricies, input_image_matricies, color_mod)

    # turn scrambled matricies and key matricies back into image
    scr_image = imr.matricies_to_image(scr_image_matricies)
    key_image = imr.matricies_to_image(key_matricies)

    return scr_image, key_image


def decrypt(scr_im, key_image):
    # Turn images into matricies
    scr_matricies = imr.image_to_matricies(scr_im)
    key_matricies = imr.image_to_matricies(key_image)

    # dot key with image to produce unscrambled matricies
    unscr_matricies = rgb_mm.trip_mod_dot(key_matricies, scr_matricies, color_mod)

    # return unscrambled image
    return imr.matricies_to_image(unscr_matricies)



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

