from PIL import Image
import os

for file in os.listdir("/Users/jun"):
    if file.endswith(".jpg"):
        background = Image.open(file)
        imageA = background.convert('RGBA')
        widthA , heightA = imageA.size
        foreground = Image.open("logo.png")
        imageB = foreground.convert('RGBA')
        widthB , heightB = imageB.size
        
        newWidthB = int(widthA/3)
        newHeightB = int(heightB/widthB*newWidthB)
        imageB_resize = imageB.resize((newWidthB, newHeightB))
        right_upper = (widthA - newWidthB, 0)
        
        background.paste(imageB_resize, right_upper, imageB_resize)
        #background.show()
        rename = file.split('.')[0]
        #print (rename)
        background.save( rename+"1.jpg" )
