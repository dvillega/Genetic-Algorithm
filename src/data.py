import os
import numpy as np
import csv

""" Master Data handling code"""

class DataFile(object):
    """ One protein file from a given DataSet
    Represented as a numpy array"""
    def __init__(self):
        pass

    """ Model Complexity
    1 = linear
    2 = quadratic
    3 = cubic
    4,5,6 are 1,2,3 with y-intercept
    """
    def __init__(self,fpath,model):
        self.data = np.genfromtxt(fpath,delimiter=',')[1:]
        self.indexNative = np.where(self.data[:,2])
        self.nativeRow = self.data[self.indexNative,:].flatten()
        self.data = np.delete(self.data,self.indexNative,0)
        Ereg = self.data[:,5]
        Ep1 = self.data[:,6]
        Ep2 = self.data[:,7]
        Enp = self.data[:,8]
        Ephi = self.data[:,9]
        Epsi = self.data[:,10]
        Esa = self.data[:,11]
        self.TMScore = self.data[:,3]
        self.Serial = self.data[:,0]
        self.Native = self.data[:,1]
        self.numProts = np.shape(self.data)[0]
        if model == 1:
            self.eData = np.column_stack((Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa))
        elif model == 2:
            Ereg2 = self.square(Ereg)
            Ep12 = self.square(Ep1)
            Ep22 = self.square(Ep2)
            Enp2 = self.square(Enp)
            Ephi2 = self.square(Ephi)
            Epsi2 = self.square(Epsi)
            Esa2 = self.square(Esa)
            self.eData = np.column_stack((Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                        Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2))
        elif model == 3:
            Ereg2 = self.square(Ereg)
            Ep12 = self.square(Ep1)
            Ep22 = self.square(Ep2)
            Enp2 = self.square(Enp)
            Ephi2 = self.square(Ephi)
            Epsi2 = self.square(Epsi)
            Esa2 = self.square(Esa)
            Ereg3 = np.power(Ereg,3)
            Ep13 = np.power(Ep1,3)
            Ep23 = np.power(Ep2,3)
            Enp3 = np.power(Enp,3)
            Ephi3 = np.power(Ephi,3)
            Epsi3 = np.power(Epsi,3)
            Esa3 = np.power(Esa,3)
            self.eData = np.column_stack((Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                        Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2,
                                        Ereg3,Ep13,Ep23,Enp3,Ephi3,Epsi3,Esa3))
        elif model == 4:
            ones = np.ones(Ereg.shape)
            self.eData = np.column_stack((ones,Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa))
        elif model == 5:
            ones = np.ones(Ereg.shape)
            Ereg2 = self.square(Ereg)
            Ep12 = self.square(Ep1)
            Ep22 = self.square(Ep2)
            Enp2 = self.square(Enp)
            Ephi2 = self.square(Ephi)
            Epsi2 = self.square(Epsi)
            Esa2 = self.square(Esa)
            self.eData = np.column_stack((ones,Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                        Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2))
        elif model == 6:
            ones = np.ones(Ereg.shape)
            Ereg2 = self.square(Ereg)
            Ep12 = self.square(Ep1)
            Ep22 = self.square(Ep2)
            Enp2 = self.square(Enp)
            Ephi2 = self.square(Ephi)
            Epsi2 = self.square(Epsi)
            Esa2 = self.square(Esa)
            Ereg3 = np.power(Ereg,3)
            Ep13 = np.power(Ep1,3)
            Ep23 = np.power(Ep2,3)
            Enp3 = np.power(Enp,3)
            Ephi3 = np.power(Ephi,3)
            Epsi3 = np.power(Epsi,3)
            Esa3 = np.power(Esa,3)
            self.eData = np.column_stack((ones,Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                        Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2,
                                        Ereg3,Ep13,Ep23,Enp3,Ephi3,Epsi3,Esa3))
        else:
            print "WHAT THE DEUCE!!! NO MODEL SELECTED!!!"



    def square(self,col):
        sign = np.sign(col)
        square = np.square(col)
        return np.multiply(sign,square)


class DataSet(object):
    """ DataSet for Protein Energy Function Project in Pattern Rec
        Initialization will load all files as numpy 2d arrays with appropriate
        info
        Walk all files in that directory, open each csv, store it in memory
        close the files"""

    def __init__(self,name,model):
        self.name = name
        self.dataSetPath = "../data/DataSet" + name
        self.dataFiles = {}
        foo = os.walk(self.dataSetPath)
        bar = foo.next()
        for elem in bar[2]:
            self.dataFiles[elem] = DataFile(self.dataSetPath + "/" + elem,model)
        self.numTotalProts = 0
        for k,v in enumerate(self.dataFiles):
            self.numTotalProts += self.dataFiles[v].numProts
        self.numProts = len(self.dataFiles)

    def __iter__(self):
        for k,v in enumerate(self.dataFiles):
            yield self.dataFiles[v]
