import os
import numpy as np
import csv

class Protein(object):
    def __init__(self):
        self.Ereg = 0.0
        self.Ep1 = 0.0
        self.Ep2 = 0.0
        self.Enp = 0.0
        self.Ephi = 0.0
        self.Epsi = 0.0
        self.Esa = 0.0
        self.TMScore = 0.0
        self.Serial = ''
        self.FileName = ''
        self.Native = False

    def __init__(self,Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,TMScore,Serial,FileName,Native):
        self.Ereg = Ereg
        self.Ep1 = Ep1
        self.Ep2 = Ep2
        self.Enp = Enp
        self.Ephi = Ephi
        self.Epsi = Epsi
        self.Esa = Esa
        self.TMScore = TMScore
        self.Serial = Serial
        self.FileName = FileName
        self.Native = Native


class DataFile(object):
    """ One protein file from a given DataSet """
    def __init__(self):
        pass

    def __init__(self,fpath):
        fh = open(fpath)
        reader = csv.reader(fh)
        reader.next()
        self.data = {}
        self.protFiles = {}
        for elem in reader:
            self.data[elem[0]] = Protein(float(elem[5]),
                float(elem[6]), float(elem[7]),
                float(elem[8]), float(elem[9]),
                float(elem[10]), float(elem[11]),
                float(elem[4]),elem[0],
                elem[1],bool(elem[2]))
        fh.close()



class DataSet(object):
    """ DataSet for Protein Energy Function Project in Pattern Rec
        Initialization will load all files as numpy 2d arrays with appropriate
        info
        Walk all files in that directory, open each csv, store it in memory
        close the files"""
    
    def __init__(self):
        pass

    def __init__(self,name):
        self.name = name
        self.dataSetPath = "../data/DataSet" + name
        self.dataFiles = []
        foo = os.walk(self.dataSetPath)
        bar = foo.next()
        for elem in bar[2]:
            self.dataFiles.append(DataFile(self.dataSetPath + "/" + elem))
