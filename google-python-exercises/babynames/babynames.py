#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'rU')
  string = f.read()
  f.close()
  match = re.search(r'Popularity in \d\d\d\d', string)
  if match is not None:
      year = re.search(r'\d\d\d\d', match.group())
      #print "Year = ", year.group()
  
  tuples = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)', string)  
  ranksDict = {}
  for tuple in tuples:
      if tuple[1] not in ranksDict: # boyname
          ranksDict[tuple[1]] = tuple[0]
      if tuple[2] not in ranksDict:
          ranksDict[tuple[2]] = tuple[0]    
  ranksDict = sorted(ranksDict.items())
  #print ranksDict
  
  finalList = []
  finalList.append(year.group())
  for k,v in ranksDict:
      finalList.append(k + ' ' + v)
  #print finalList      
  return finalList


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)
  
  files = os.listdir(".")
  htmlFiles = [file for file in files if file.endswith(".html")]
  for file in htmlFiles:
      finalList = extract_names(file)
      f = open(file + '.summary', 'w')
      for record in finalList:
          print record
          f.write(record)
          f.write('\n')
      f.close()    
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
