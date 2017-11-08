import re
import sys
import os.path
import hashlib

PATH = sys.argv[1]
filemd5 = {}
f = open("duplicate_list", "w")

def visit(arg, dirname, filenames):
  for filename in filenames:
    sys.stdout.write('.')
    if not(os.path.isdir(dirname + "\\" + filename)):
      md5 = hashlib.md5(open(dirname + "\\" + filename,'rb').read()).hexdigest()
      if md5 in filemd5:
        f.write(filemd5[md5] + ";" + dirname + "\\" + filename + "\n")
      else:
        # sys.stdout.write(".")
        filemd5[md5] = dirname + "\\" + filename

os.path.walk(PATH, visit, None)

f.close()
