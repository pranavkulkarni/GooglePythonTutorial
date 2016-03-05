#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  domain = "http://" + filename.split('_')[1]
  f = open(filename, 'rU')
  log = f.read()
  f.close()
  #use regex to read the paths (?<=GET)(.*puzzle.*)(?=HTTP)   (.*GET)\s(\S)\s(HTTP.*)
  #tuples = re.findall(r'(?<=GET)(.*puzzle.*)(?=HTTP)', log)
  tuples = re.findall(r'(?<=GET)(.*puzzle.*)(?=HTTP)', log)
  s = set()
  if tuples is not None:
    for tuple in tuples:
      s.add(domain + tuple.strip())
  else:
    print "something wrong!"
  #print listOfUrls  
  s = sorted(s)
  return s
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  print "Retrieving..."  
  s = ''
  for i in range(len(img_urls)):
    xFileName = dest_dir + "/img" + str(i)
    s = s + "<img src=\"img" + str(i) + "\">"
    urllib.urlretrieve(img_urls[i], xFileName)
  #now create the index html file in target directory
  htmlFile = open(dest_dir + '/index.html', 'w')
  htmlFile.write('<html>\n')
  htmlFile.write('<body>\n')
  htmlFile.write(s + '\n')
  htmlFile.write('</html>\n')
  htmlFile.write('</body>')
  htmlFile.close()

###########################################

def read_urls_2(filename): # for placeImages
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  domain = "http://" + filename.split('_')[1]
  f = open(filename, 'rU')
  log = f.read()
  f.close()
  #use regex to read the paths (?<=GET)(.*puzzle.*)(?=HTTP)   (.*GET)\s(\S)\s(HTTP.*)
  #tuples = re.findall(r'(?<=GET)(.*puzzle.*)(?=HTTP)', log)
  tuples = re.findall(r'(?<=GET)(.*puzzle.*)(?=HTTP)', log)
  s = set()
  if tuples is not None:
    for tuple in tuples:
      match = re.search(r'(.*)-(.*)-(.*)', tuple.strip())
      if match:
        #print "hurray"
        s.add(domain + tuple.strip())
      else:
        print "*** Does not work!"
  else:
    print "something wrong!"
  #print listOfUrls  
  s = sorted(s, key = customSortKey)
  return s

def customSortKey(g):
  temp = g.split('.jpg')[0]
  return temp.split('-')[-1]


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
