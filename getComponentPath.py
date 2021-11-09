import getopt
import sys
import os
from scriptComponents import readComponents
import zipfile
import shutil

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, 'i:', ['foperand'])

if len(opts) < 1:
  print ('usage: add.py -a <first_operand> -b <second_operand>')
else:
  for opt, arg in opts:
    path = arg


#Colocar o path até a pasta do Site]
filename0 = path.split(".")
filename1 = filename0[0].split("/")
filename2 = filename1[-1]

with zipfile.ZipFile(path, 'r') as zip_ref:
    paths = path.split(os.sep)
    path = path.replace(paths[-1],"")
    zip_ref.extractall(path)

readComponents(os.path.join(path, filename2 , 'administrator', 'components'))

shutil.rmtree(os.path.join(path, filename2))

