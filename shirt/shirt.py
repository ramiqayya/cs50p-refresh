import PIL
import sys
import os

import PIL.Image
import PIL.ImageOps

file1,ext1=os.path.splitext(sys.argv[1].lower()) #seperates file one extention
file2,ext2=os.path.splitext(sys.argv[2].lower()) #seperates file two extention

acceptable=[".jpeg",".png",".jpg"] #acceptable extentions

if len(sys.argv)< 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif ext1 not in  acceptable or ext2 not in acceptable:
    sys.exit("Invalid input")
elif ext1 != ext2:
    sys.exit("Input and output have different extensions")


try:
    with PIL.Image.open(sys.argv[1]) as im,PIL.Image.open("shirt.png") as shirt:
        size1 =shirt.size

        im1=PIL.ImageOps.fit(im, size1)
        # print(im1)
        im1.paste(shirt,(0,0),shirt)
        im1.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File does not found")
