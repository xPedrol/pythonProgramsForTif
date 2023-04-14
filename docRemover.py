import os
directory = input("Enter the directory: ")


def readDirectory(dir, parentDir=None):
    fullDir = parentDir + "\\" + dir
    if os.path.isdir(fullDir):
        for file in os.listdir(fullDir):
            readDirectory(file, fullDir)
    else:
        ext = dir.split(".")[-1]
        if "doc" in ext:
            os.remove(fullDir)
            print("Removed % s" % (fullDir))


for infile in os.listdir(directory):
    readDirectory(infile, directory)
    print("-----------------")
