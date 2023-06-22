import os
import shutil

root_input_path = "D:\\Documentos Câmara\\Arquivo da Câmara de Viçosa"
root_output_path = "D:\\VicosaDocumentos"


def readDirectory(dir, parentDir=None):
    fullDir = parentDir + "\\" + dir
    if os.path.isdir(fullDir):
        for file in os.listdir(fullDir):
            readDirectory(file, fullDir)
    else:
        # remove root_input_path from fullDir
        newDir = fullDir.replace(root_input_path, "")
        # split new dir by /
        fileDir = newDir.split("\\")[1]
        # verify if fileDir exists in root_output_path
        if not os.path.exists(root_output_path + '\\' + fileDir):
            os.mkdir(root_output_path + '\\' + fileDir)

        # verify if file exists in root_output_path
        if os.path.exists(root_output_path + newDir):
            print(f"O arquivo '{root_output_path + newDir}' já existe.")
        else:
            shutil.copy2(fullDir, root_output_path + newDir)
            print(f"O arquivo '{root_output_path + newDir}' foi copiado.")


for infile in os.listdir(root_input_path):
    readDirectory(infile, root_input_path)
    print("---------------------------------------------------------")

# Chamando a função para realizar o OCR
# ocr_pdf(input_path, output_path)
