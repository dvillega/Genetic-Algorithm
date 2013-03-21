import os
import sys

path = sys.argv[1]
os.chdir(path)
foo = os.walk(os.getcwd())
bar = foo.next()
x = [elem for elem in bar[2] if (elem[-4:] == '.dat')]

# Have all the files
