import os

size = (100, 100)
directory = input("Enter the directory: ")
print("File in directory: % s" % directory)
fileBaseName = "CSM.02.INV"
searchFor = ["Codice", "Códice", "Auto"]
convertKey = "needConvert"


# CSM.02.INV.1718.84.1790.00001
# CSM.02.INV.ANO.CODICE.AUTO.NOME_ARQV


def readDirectory(dir, parentDir=None):
    fullDir = parentDir + "\\" + dir
    if os.path.isdir(fullDir):
        for file in os.listdir(fullDir):
            readDirectory(file, fullDir)
    else:
        ext = dir.split(".")[-1]
        if ext != "tif" and ext != "tiff":
            return
        splitDir = (parentDir.split("\\")[-1]).split(" ")
        contained = [a in splitDir for a in searchFor]
        if True in contained:
            if not convertKey in dir and "CSM" not in dir:
                # remove file
                os.remove(fullDir)
                print("Removed % s" % dir)
                return
            if "CSM" in dir:
                return
            ano = splitDir[0]
            codice = splitDir[2]
            auto = splitDir[4]
            fullName = fileBaseName + "." + ano + "." + codice + "." + auto + "." + dir
            # remove needConvert from file name
            fullName = fullName.replace(convertKey + ".", "")
            # rename file
            os.rename(fullDir, parentDir + "\\" + fullName)
            print("Renamed % s to % s" % (dir, fullName))


for infile in os.listdir(directory):
    readDirectory(infile, directory)
    print("-----------------")
