import os
from PIL import Image
images = os.listdir("./dir_with_image") # Le dossier qui contient vos images

compteur = 0

for im in images:
    img = Image.open("./dir_with_image/" + im)
    img.save("./images_format/image_" + str(compteur) + ".jpg")
    transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    transposed_img.save("./images_format/flip_" + str(compteur) + ".png")
    alpha = transposed_img.copy()
    alpha.putalpha(128)
    alpha.save("./images_format/version_" + str(compteur) + ".png")
    alpha2 = transposed_img.copy()
    alpha2.putalpha(185)
    alpha2.save("./images_format/version2_" + str(compteur) + ".png")
    os.remove("./dir_with_image/" + im)
    compteur = compteur + 1