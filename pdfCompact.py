import subprocess

input_file = "D:\Download\\ATA 1877-1881.pdf"
output_file = "D:\Download\\arquivo_comprimido.pdf"

def compress_pdf(input_file, output_file):
    command = [
        "gswin64c", "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dNOPAUSE", "-dQUIET", "-dBATCH", "-q",
        "-dPDFSETTINGS=/ebook/",
        "-o",
        output_file,
        input_file
    ]

    subprocess.call(command, shell=True)

