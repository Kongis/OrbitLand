from cgi import test
import os, glob
import os.path
from unicodedata import name
from PIL import Image
raw_image = Image.open("Person_Textures.png")
left = 0
upper = 0
right = 48
lower = 96
#image_crop = raw_image.crop((left,upper,right,lower))
#image_show = image_crop.show()
#print (str(dir) + str(x) + ".png")
#image_crop.save(str(dir) + str(x) + ".png")

#image_crop.save("Test"".png")
row_1 = ["basic_standing_right","basic_standing_back", "basic_standing_left", "basic_standing_front"]
row_2 = ["indle_standing_right","indle_standing_back", "indle_standing_left", "indle_standing_front"]
row_3 = ["walking_right","walking_back", "walking_left", "walking_front"]
def basic_standing():
    path = "Finish_Products/Basic Standing/"
    x = 0
    lower_1 = 96
    upper_1 = 0
    right_1 = 48
    left_1 = 0
    raw_image = Image.open("Person_Textures.png")
    while x < 4:
        image_crop1 = raw_image.crop((left_1, upper_1, right_1, lower_1))
        name = row_1[x]
        image_crop1.save("Finish_Products/Basic_Standing/" + str(name) + ".png")
        right_1 = right_1 + 48
        left_1 = left_1 + 48
        x = x + 1
    return print("Hotovo")
        
def indle_standing():
    path = "Finish_Products/Basic Standing/"
    x = 0
    y = 0
    z = 0
    w = 1
    lower_1 = 192
    upper_1 = 96
    right_1 = 48
    left_1 = 0
    raw_image = Image.open("Person_Textures.png")
    while x < 24:
        if w > 6:
            w = 1
        if x >= 0 and x < 6:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 0 
            #print (left_1, right_1)
            name = row_2[z]
            image_crop.save("Finish_Products/Animation\Indle_Standing/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
        elif x > 5 and x < 12:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 1
            name = row_2[z]
            image_crop.save("Finish_Products/Animation\Indle_Standing/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
        elif x > 11 and x < 18:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 2
            name = row_2[z]
            image_crop.save("Finish_Products/Animation\Indle_Standing/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
        elif x > 17 and x < 24:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 3 
            name = row_2[z] 
            image_crop.save("Finish_Products/Animation\Indle_Standing/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
    return print ("Hotovo")            

def walking():
    path = "Finish_Products/Basic Standing/"
    x = 0
    y = 0
    z = 0
    w = 1
    lower_1 = 288
    upper_1 = 192
    right_1 = 48
    left_1 = 0
    raw_image = Image.open("Person_Textures.png")
    while x < 24:
        if w > 6:
            w = 1
        if x >= 0 and x < 6:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 0 
            #print (left_1, right_1)
            name = row_3[z]
            image_crop.save("Finish_Products/Animation/Walking/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
        elif x > 5 and x < 12:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 1
            name = row_3[z]
            image_crop.save("Finish_Products/Animation/Walking/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
        elif x > 11 and x < 18:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 2
            name = row_3[z]
            image_crop.save("Finish_Products/Animation/Walking/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
        elif x > 17 and x < 24:
            image_crop = raw_image.crop((left_1, upper_1, right_1, lower_1))
            z = 3 
            name = row_3[z] 
            image_crop.save("Finish_Products/Animation/Walking/" + str(name) + str(w) + ".png")
            x = x + 1
            right_1 = right_1 + 48
            left_1 = left_1 + 48
            w = w + 1
    return print ("Hotovo") 

basic_standing()
indle_standing()      
walking()