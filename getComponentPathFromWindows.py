import zipfile
import os
from scriptComponents import readComponents
import shutil

def getPathFromWindows(path, sqlpath):
    #Colocar o path até a pasta do Site]
    filename0 = path.split(".")
    filename1 = filename0[0].split(os.sep)
    filename2 = filename1[-1]

    with zipfile.ZipFile(path, 'r') as zip_ref:
        paths = path.split(os.sep)
        path = path.replace(paths[-1],"")
        path = os.path.join(path,filename2)
        zip_ref.extractall(path)

    readComponents(os.path.join(path , 'administrator', 'components'), sqlpath)

    shutil.rmtree(os.path.join(path))
