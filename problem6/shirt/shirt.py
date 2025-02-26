import sys
from PIL import Image,ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (sys.argv[1].split(".")[1] !=  sys.argv[2].split(".")[1]):
    sys.exit("Input and output have different extensions")
elif not(os.path.splitext(sys.argv[2])[1].lower() in ['.jpg','.jpeg','.png']):
    sys.exit("Invalid input")
try:  
    with Image.open("shirt.png") as shirt:
        with Image.open(sys.argv[1]) as pic:
            size = shirt.size
            new_img = ImageOps.fit(pic,size)
            new_img.paste(shirt,shirt)
            new_img.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist.")