import os

import ocrmypdf

def ocr_pdf(input_file, output_file):
    try:
        ocrmypdf.ocr(input_file, output_file, deskew=True, optimize=3)
        print(f"OCR realizado com sucesso. O arquivo '{output_file}' foi criado.")
    except Exception as e:
        print(f"Ocorreu um erro durante o OCR: {str(e)}")

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
        ocr_pdf(fullDir, root_output_path + newDir)
        # ocr_pdf(fullDir, fullDir)


for infile in os.listdir(root_input_path):
    readDirectory(infile, root_input_path)
    print("---------------------------------------------------------")



# Chamando a função para realizar o OCR
# ocr_pdf(input_path, output_path)
