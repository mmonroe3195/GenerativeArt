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

# number of images to make
for image in range(4):
    # creating image object 
    background = getPNGS("background")
    faces = getPNGS("faces")
    mouth = getPNGS("mouth")
    nose = getPNGS("nose")
    shirt = getPNGS("shirt")
    eyes = getPNGS("eyes")
    hats = getPNGS("hats")


    people = []
    for i in range(170):
        img = Image.alpha_composite(background[random.randint(0, len(background) - 1)], faces[random.randint(0, len(faces) - 1)])
        img = Image.alpha_composite(img, hats[random.randint(0, len(hats) - 1)])
        img = Image.alpha_composite(img, shirt[random.randint(0, len(shirt) - 1)])
        img = Image.alpha_composite(img, eyes[random.randint(0, len(eyes) - 1)])
        img = Image.alpha_composite(img, mouth[random.randint(0, len(mouth) - 1)])
        img = Image.alpha_composite(img, nose[random.randint(0, len(nose) - 1)])
        people.append(img)

    new_image = Image.new('RGB',(17 * people[0].size[0], 10 * people[0].size[1]), (250,250,250))

    person_counter = 0
    for j in range(10):
        for i in range(17):
            new_image.paste(people[person_counter],(i * people[person_counter].size[0],j * people[person_counter].size[1]))
            person_counter += 1
    
    
    other_alterations = [new_image.rotate(45),new_image.rotate(20), new_image, new_image.convert('L'), new_image.convert('1')]
    #other_alterations[random.randint(0, len(other_alterations) - 1)].show()

    new_image.show()
new_image.putalpha(127)
#new_image.show()
   