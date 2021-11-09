import getopt
import sys
from scriptComponents import readComponents

# Get the arguments from the command-line except the filename
argv = sys.argv[1:]


# Define the getopt parameters
# opts, args = getopt.getopt(argv, 'a:b:', ['foperand', 'soperand'])
opts, args = getopt.getopt(argv, 'i:', ['foperand'])
# Check if the options' length is 2 (can be enhanced)
if len(opts) < 1:
  print ('usage: add.py -a <first_operand> -b <second_operand>')
else:
  # Iterate the options and get the corresponding values
  for opt, arg in opts:
    path = arg
    print(path)

readComponents(path)

