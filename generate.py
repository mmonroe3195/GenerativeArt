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

foregrounds = getPNGS("foreground")
image_parts = [getPNGS("background"), getPNGS("faces"), getPNGS("hats"), getPNGS("shirt"), 
               getPNGS("eyes"), getPNGS("mouth"),getPNGS("nose")]

# Making different pictures. The number of pictures will be equal to the number of foregrounds in the foreground folder 
for index, foreground in enumerate(foregrounds):
    people = []

    # Creating people randomly
    for i in range(170):
        img = Image.alpha_composite(image_parts[0][random.randint(0, len(image_parts[0]) - 1)], image_parts[1][random.randint(0, len(image_parts[1]) - 1)])
        for part in image_parts[2:]:
            img = Image.alpha_composite(img, part[random.randint(0, len(part) - 1)])
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
    other_alterations[index].show()
   