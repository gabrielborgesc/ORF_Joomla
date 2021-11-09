import getopt
import sys
import os
from scriptComponents import readComponents

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, 'i:', ['foperand'])

if len(opts) < 1:
  print ('usage: add.py -a <first_operand> -b <second_operand>')
else:
  for opt, arg in opts:
    path = arg


#Colocar o path até a pasta do Site

readPlugins(os.path.join(path, 'plugins'))

