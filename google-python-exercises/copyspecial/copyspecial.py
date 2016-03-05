#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  files = os.listdir(dir)
  #reg expression to see if it is a special file containing character w
  paths = []
  for file in files:
    match = re.search(r'__\w+__', file)
    if match is not None:
      #print os.path.abspath(os.path.join(dir, file))
      paths.append(os.path.abspath(os.path.join(dir, file)))
  return paths


def copy_to(paths, dir):
  if os.path.exists(dir): #paths is a list of all absolute paths of the files to be copied
    for path in paths:
      shutil.copy(path, dir)
  else:
    os.mkdir(dir)
    for path in paths:
      shutil.copy(path, dir) 

def zip_to(paths, zippath):
  cmd = 'zip -j ' + zippath + ' '+ ' '.join(paths) #zippath is the complete path of the zip file
  print "Command to run: ", cmd   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(1)
  

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  print args
  dir = ''
  if args[0] == '--dir':
    dir = args[1]
    specialPaths = get_special_paths(dir)
  print specialPaths  
  toDir = ''
  for arg in args:
    if arg == '--todir':
      toDir = args[args.index('--todir')+1]
    if arg == '--tozip':
      toZip = args[args.index('--tozip')+1]  
  #copy_to(specialPaths, toDir)
  specialPaths = [s.replace(' ', '\ ') for s in specialPaths] ##required to avoid spaces in directory names and hence escape sequence
  zip_to(specialPaths, toZip)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
