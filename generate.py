from PIL import Image 
import os
import random

# Given a folder name in a subdirectory, gets all the png images in that folder
def getPNGS(folder):
    images = []
    directory = os.listdir(os.getcwd() + "/" + folder)
    for file in directory:
        if file[-4:] == ".png":
            path = "./" + folder + "/" + file
            images.append(Image.open(path))

    return images

# Number of total images to make
for index in range(len(getPNGS("foreground"))):
    
    # Getting all pngs from their respective folders
    background = getPNGS("background")
    faces = getPNGS("faces")
    mouth = getPNGS("mouth")
    nose = getPNGS("nose")
    shirt = getPNGS("shirt")
    eyes = getPNGS("eyes")
    hats = getPNGS("hats")
    foreground = getPNGS("foreground")

    people = []
    foreground = foreground[index]

    # Creating people randomly
    for i in range(170):
        img = Image.alpha_composite(background[random.randint(0, len(background) - 1)], faces[random.randint(0, len(faces) - 1)])
        img = Image.alpha_composite(img, hats[random.randint(0, len(hats) - 1)])
        img = Image.alpha_composite(img, shirt[random.randint(0, len(shirt) - 1)])
        img = Image.alpha_composite(img, eyes[random.randint(0, len(eyes) - 1)])
        img = Image.alpha_composite(img, mouth[random.randint(0, len(mouth) - 1)])
        img = Image.alpha_composite(img, nose[random.randint(0, len(nose) - 1)])
        img = Image.alpha_composite(img, foreground)
        people.append(img)

    # Sets the total size of the image
    new_image = Image.new('RGB',(17 * people[0].size[0], 10 * people[0].size[1]), (250,250,250))

    person_counter = 0

    # Populates the image with various different people
    for j in range(10):
        for i in range(17):
            new_image.paste(people[person_counter],(i * people[person_counter].size[0],j * people[person_counter].size[1]))
            person_counter += 1
    
    
    # Adds other alterations to the photos randomly such as tilt
    other_alterations = [new_image.rotate(45), new_image, new_image.rotate(20), new_image, new_image.convert('1'), new_image, new_image.convert('L'), new_image, new_image.rotate(-40), new_image, new_image.rotate(-90), new_image.convert('L'), new_image]
    print(index)
    other_alterations[index].show()
   