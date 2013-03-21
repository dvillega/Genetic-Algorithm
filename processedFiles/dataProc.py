#!/usr/bin/python

class Data(object):
    """
    Container to hold our dataObjects before writing them out cleanly
    """
    def __init__(self,betaVals):
        self.betaVals = betaVals
        self.c9F1 = 0.0
        self.c9F2 = 0.0
        self.c8F1 = 0.0
        self.c8F2 = 0.0
        self.mF1 = 0.0
        self.mF2 = 0.0
        self.rF1 = 0.0
        self.rF2 = 0.0
        self.tF1 = 0.0
        self.tF2 = 0.0
        self.rZ = 0.0
        self.c8Z = 0.0
        self.mZ = 0.0
        self.tZ = 0.0
        self.Zavg  = 0.0

import os
import sys

target = sys.argv[1]
os.chdir(target)
path = os.getcwd()
foo = os.walk(path)
bar = foo.next()
x = [elem for elem in bar[2] if elem[-4:] == '.dat']

#Outputs
outfh = open('dataTotals' + path[-6:] + '.csv','w')

masterInfo = {}

for elem in x:
    fh = open(elem)
    lines = fh.readlines()
    length = len(lines)
    lines = [line.strip() for line in lines]
    # Error handling for runs that were stopped prior to completion
    try:
        betaStart = lines.index('Final')
    except ValueError:
        continue
    fooList = lines[betaStart+1:len(lines)-7]
    betaVals = ' '.join(fooList)
    masterInfo[elem] = Data(betaVals)
    # Add C8
    bar = masterInfo.get(elem)
    foo = lines[length-7].split()
    bar.c8F1 = float(foo[2])
    bar.c8F2 = float(foo[4])

    # Add M
    foo = lines[length-6].split()
    bar.mF1 = float(foo[2])
    bar.mF2 = float(foo[4])

    # Add R
    foo = lines[length - 5].split()
    bar.rF1 = float(foo[2])
    bar.rF2 = float(foo[4])

    # Add T
    foo = lines[length-4].split()
    bar.tF1 = float(foo[2])
    bar.tF2 = float(foo[4])

    # Add C9 
    foo = lines[length-3].split()
    bar.c9F1 = float(foo[2])
    bar.c9F2 = float(foo[5])

    # Add Zscores
    foo = lines[length-2].split()
    bar.rZ = float(foo[2][7:-3])
    bar.c8Z = float(foo[4][7:-3])
    bar.mZ = float(foo[6][7:-3])
    bar.tZ = float(foo[8][7:-3])
    bar.Zavg = float(lines[length-1][7:-1])

outfh.write("File,Zavg,betas,c8F1,c8f2,c8f3,mf1,mf2,mf3,rf1,rf2,rf3,tf1,tf2,tf3,c9f1,c9f2\n")

# Concatenate all info into a final CSV - one run maximum per row
for k,v in masterInfo.items():
    outfh.write(k)
    outfh.write(",")
    outfh.write(str(v.Zavg))
    outfh.write(",")
    outfh.write(str(v.betaVals))
    outfh.write(",")
    outfh.write(str(v.c8F1))
    outfh.write(",")
    outfh.write(str(v.c8F2))
    outfh.write(",")
    outfh.write(str(v.c8Z))
    outfh.write(",")
    outfh.write(str(v.mF1))
    outfh.write(",")
    outfh.write(str(v.mF2))
    outfh.write(",")
    outfh.write(str(v.mZ))
    outfh.write(",")
    outfh.write(str(v.rF1))
    outfh.write(",")
    outfh.write(str(v.rF2))
    outfh.write(",")
    outfh.write(str(v.rZ))
    outfh.write(",")
    outfh.write(str(v.tF1))
    outfh.write(",")
    outfh.write(str(v.tF2))
    outfh.write(",")
    outfh.write(str(v.tZ))
    outfh.write(",")
    outfh.write(str(v.c9F1))
    outfh.write(",")
    outfh.write(str(v.c9F2))
    outfh.write("\n")

outfh.close()
