import os
import numpy as np
import csv

""" Master Data handling code"""

class DataFile(object):
    """ One protein file from a given DataSet
    Represented as a numpy array"""
    def __init__(self):
        pass

    def __init__(self,fpath):
        self.data = np.genfromtxt(fpath,delimiter=',')[1:]
        Ereg = self.data[:,5]
        rows = len(Ereg)
        Ep1 = self.data[:,6]
        Ep2 = self.data[:,7]
        Enp = self.data[:,8]
        Ephi = self.data[:,9]
        Epsi = self.data[:,10]
        Esa = self.data[:,11]
        self.TMScore = self.data[:,4]
        self.Serial = self.data[:,0]
        self.Native = self.data[:,2]
        self.eData = np.column_stack((Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa))
#        self.eData = np.reshape(self.eData,(rows,7))


class DataSet(object):
    """ DataSet for Protein Energy Function Project in Pattern Rec
        Initialization will load all files as numpy 2d arrays with appropriate
        info
        Walk all files in that directory, open each csv, store it in memory
        close the files"""

    def __init__(self,name):
        self.name = name
        self.dataSetPath = "../data/DataSet" + name
        self.dataFiles = {}
        foo = os.walk(self.dataSetPath)
        bar = foo.next()
        for elem in bar[2]:
            self.dataFiles[elem] = DataFile(self.dataSetPath + "/" + elem)
