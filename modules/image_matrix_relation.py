from PIL import Image
import numpy as np


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