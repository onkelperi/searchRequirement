#!/usr/bin/env python

import subprocess
import os

def main():
  fp = open('ReqList.txt', 'r')
  lines = fp.readlines()
  for line in lines:
    ExecuteSearch(line.rstrip())
  fp.close()


def ExecuteSearch(ReqNumber):
  OutputText = "%s"%ReqNumber
  BashCall = 'grep -r --include \*.h \"TC_REQUIREMENT(\\"%s\\")\" *' % ReqNumber
  result = subprocess.Popen(BashCall, shell=True, stdout=subprocess.PIPE)
  SearchResult = result.communicate()[0]
  if (SearchResult != ''):
    # The requirement was found
    OutputText = OutputText + ";found" + ";" + SearchResult
  else:
    # The requirement was not found
    OutputText = OutputText + ";missing"
  OutputText = OutputText + ";" + BashCall
  print OutputText  
  

if __name__ == "__main__":
    main()


