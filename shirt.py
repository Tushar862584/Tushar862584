import sys
from PIL import Image , ImageOps
from os.path import splitext


if len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
         sys.exit("Too many command-line arguments")
file1 = splitext(sys.argv[1])
file2 = splitext(sys.argv[2])
print(file1)
print(file2)
if file1[1] not  in [".jpg" , ".jepg" , ".png"]:
    sys.exit("invalid input")
if file2[1] not  in [".jpg" , ".jepg" , ".png"]:
    sys.exit("invalid output")
if file1[1].lower() !=  file2[1].lower():
    sys.exit("input and output have different extension")
try :
      image = Image.open(sys.argv[1])
except FileNotFoundError:
         sys.exit("input does not exist")
shirt = Image.open("shirt.png")
size =shirt.size
muppet = ImageOps.fit(image ,size)
muppet.paste(shirt ,shirt)
muppet.save(sys.argv[2])
