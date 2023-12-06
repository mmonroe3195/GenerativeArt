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

# creating image2 object having alpha 
"""img1 = faces[0] 
img2 = mouth[0] 
img3 = hats[0] 
img2 = img2.resize(img1.size) 
img2 = img2.convert('RGBA')
img1 = img1.convert('RGBA')
print(img1.mode)
print(img2.mode)"""

  
# using alpha_composite 

people = []
for i in range(3):
    img = Image.alpha_composite(faces[random.randint(0, len(faces) - 1)], hats[random.randint(0, len(hats) - 1)])
    img = Image.alpha_composite(img, shirt[random.randint(0, len(shirt) - 1)])
    img = Image.alpha_composite(img, eyes[random.randint(0, len(eyes) - 1)])
    img = Image.alpha_composite(img, mouth[random.randint(0, len(mouth) - 1)])
    img = Image.alpha_composite(img, nose[random.randint(0, len(nose) - 1)])
    people.append(img)

for i in range(10):
    print(random.randint(0, len(eyes) - 1))


img.show() 
img1 = people[0]
img2 = people[1]
img3 = people[2]


# how to combine 2 imgs
new_image = Image.new('RGB',(3 * img1.size[0], img1.size[1]), (250,250,250))
new_image.paste(img2,(0,0))
new_image.paste(img1,(img1.size[0],0))
new_image.paste(img3,(2 * img1.size[0],0))
new_image.show()
