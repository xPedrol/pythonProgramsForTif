# Não utilizado
import os

from PIL import Image

size = (100, 100)
directory = input("Enter the directory: ")
print("Files in directory: % s" % directory)
accepted_formats = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp']
for infile in os.listdir(directory):
    ext = infile.split('.')[-1].lower()
    if (ext not in accepted_formats):
        continue
    print("File: % s" % infile)
    outfile = directory + "resized\\" + infile
    # if infile != outfile:
    try:
        im = Image.open(directory + infile)
        # width, height = im.size
        # # Recude width in 10%
        # newWidth = width - (width * 20 / 100)
        # # Recude height in 10%
        # newHeight = height - (height * 20 / 100)
        # tuple = (newWidth, height)
        # im.thumbnail(tuple, Image.LANCZOS)
        im.save(outfile, quality=50, optimize=True)
    except IOError:
        print("cannot create thumbnail for '%s'" % infile)
    print("-----------------")
