
#********************************************************************************************************
#Crea un nuevo pdf llamado fileName en la ruta definida com pathDir, a partir de varios pdf separados
#********************************************************************************************************

from PyPDF2 import PdfFileMerger, PdfFileReader
import os


def fetchFiles(path, fileName):
    output = PdfFileMerger(strict=False)
    for root, dirs, files in os.walk(path):
        for myfile in files:
            if(myfile.endswith(".pdf")):
                fileAppend=os.path.join(root, myfile)
                print(os.path.join(root, myfile))
                output.append(PdfFileReader(fileAppend,"rb"))

    output.write(path+"/"+fileName+".pdf")
def main():
    pathDir="agruegue aqui el directorio que desee, con los archivos pdf"
    fileName="Nuevo Archivo"
    fetchFiles(pathDir,fileName)    


if __name__=="__main__":
    main()