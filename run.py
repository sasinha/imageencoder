import image_encoder as ie
from PIL import Image


user_image_name_full = input("Please enter your image name: ")
user_image_name = user_image_name_full.split(".")[0]
extension = "." + user_image_name_full.split(".")[1]
user_image = Image.open(user_image_name_full)
operation_type = (input("Would you like to (E)ncrypt or (D)ecrypt? ")).lower()
if operation_type == 'e':
    scrambled_image, key_image = ie.encrypt(user_image)
    scrambled_image.save(user_image_name + "_scrambled" + extension)
    key_image.save(user_image_name + "_key" + extension)

elif operation_type == "d":
    key_image = Image.open(input("Please enter your key image name: "))
    unscrambled_image = ie.decrypt(user_image, key_image)
    unscrambled_image.save(user_image_name + "_unscrambled" + extension)