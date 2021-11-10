
import zipfile
import os
from scriptComponents import readComponents
import shutil

def getPathFromLinux(path, sqlpath):
  #Colocar o path até a pasta do Site]
  filename0 = path.split(".")
  filename1 = filename0[0].split("/")
  filename2 = filename1[-1]

  with zipfile.ZipFile(path, 'r') as zip_ref:
      paths = path.split(os.sep)
      path = path.replace(paths[-1],"")
      zip_ref.extractall(path)

  readComponents(os.path.join(path, filename2 , 'administrator', 'components'), sqlpath)

  shutil.rmtree(os.path.join(path, filename2))

