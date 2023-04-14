# Rename and convert tif files to tif pyramidal
import os

size = (100, 100)
directory = input("Enter the directory: ")
print("File in directory: % s" % directory)
fileBaseName = "CSM.02.INV"
searchFor = ["Codice", "Códice", "Auto"]


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
            if "CSM" in dir:
                return
            ano = splitDir[0]
            codice = splitDir[2]
            auto = splitDir[4]
            newFullDir = parentDir + "\\" + fileBaseName + "." + ano + "." + codice + "." + auto + "." + dir
            try:
                os.system(
                    'vips tiffsave "' + fullDir + '" "' + newFullDir + '" --compression=jpeg --Q=75 --tile --tile-width=256 --tile-height=256 --pyramid')
            except:
                print("Error in VIPS")
            os.remove(fullDir)
            print("Renamed % s to % s" % (dir, newFullDir))


for infile in os.listdir(directory):
    readDirectory(infile, directory)
    print("-----------------")
