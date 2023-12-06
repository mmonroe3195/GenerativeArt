# importing image class from PIL package 
from PIL import Image 
import os
import random

def getPNGS(folder):
    images = []
    directory = os.listdir(os.getcwd() + "/" + folder) # your directory path
    for file in directory:
        if file[-4:] == ".png":
            path = "./" + folder + "/" + file
            images.append(Image.open(path))

    return images

# creating image object 
faces = getPNGS("faces")
mouth = getPNGS("mouth")
nose = getPNGS("nose")
shirt = getPNGS("shirt")
eyes = getPNGS("eyes")
hats = getPNGS("hats")

people = []
for i in range(40):
    img = Image.alpha_composite(faces[random.randint(0, len(faces) - 1)], hats[random.randint(0, len(hats) - 1)])
    img = Image.alpha_composite(img, shirt[random.randint(0, len(shirt) - 1)])
    img = Image.alpha_composite(img, eyes[random.randint(0, len(eyes) - 1)])
    img = Image.alpha_composite(img, mouth[random.randint(0, len(mouth) - 1)])
    img = Image.alpha_composite(img, nose[random.randint(0, len(nose) - 1)])
    people.append(img)

img1 = people[0]
img2 = people[1]
img3 = people[2]

# combining 10 randomly generated people horizonally
new_image = Image.new('RGB',(10 * people[0].size[0], 5 * people[0].size[1]), (250,250,250))
for j in range(7):
    for i in range(11):
        new_image.paste(people[i],(0,0))
        new_image.paste(people[i],(i * people[i].size[0],j * people[i].size[1] - 20))

new_image.show()
