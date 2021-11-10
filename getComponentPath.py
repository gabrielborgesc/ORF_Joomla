import getopt
import sys
import os
from scriptComponents import readComponents
import zipfile
import shutil
import platform
from getComponentPathFromWindows import getPathFromWindows
from getComponentPathFromLinux import getPathFromLinux

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, 'i:', ['foperand'])

if len(opts) < 1:
  print ('usage: add.py -i <input absolute filename>')
else:
  for opt, arg in opts:
    path = arg


if(platform.system()=="Windows"):
    getPathFromWindows(path)

elif(platform.system()=="Linux"):
    getPathFromLinux(path)

else:
    print("Sistema operacional Inválido")