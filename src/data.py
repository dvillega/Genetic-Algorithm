import os
import numpy as np
import csv

""" Master Data handling code"""

class DataFile(object):
    """ One protein file from a given DataSet
    Represented as a numpy array

    Model Complexity
    1 = linear
    2 = quadratic
    3 = cubic
    4,5,6 are 1,2,3 with y-intercept

    Memory footprint is on the order of 100MBs - I'm going to keep everything
    in memory...
    """
    def __init__(self,fpath):
        self.data = np.genfromtxt(fpath,delimiter=',')[1:]
        self.indexNative = np.where(self.data[:,2])
        self.nativeRow = self.data[self.indexNative,:].flatten()
        self.data = np.delete(self.data,self.indexNative,0)

        # Linear Features
        self.Ereg = self.data[:,5]
        self.Ep1 = self.data[:,6]
        self.Ep2 = self.data[:,7]
        self.Enp = self.data[:,8]
        self.Ephi = self.data[:,9]
        self.Epsi = self.data[:,10]
        self.Esa = self.data[:,11]

        # Y-intercept
        self.ones = np.ones(self.Ereg.shape)

        # Quadratic Features
        self.Ereg2 = self.square(self.Ereg)
        self.Ep12 = self.square(self.Ep1)
        self.Ep22 = self.square(self.Ep2)
        self.Enp2 = self.square(self.Enp)
        self.Ephi2 = self.square(self.Ephi)
        self.Epsi2 = self.square(self.Epsi)
        self.Esa2 = self.square(self.Esa)

        # Cubic Features
        self.Ereg3 = np.power(self.Ereg,3)
        self.Ep13 = np.power(self.Ep1,3)
        self.Ep23 = np.power(self.Ep2,3)
        self.Enp3 = np.power(self.Enp,3)
        self.Ephi3 = np.power(self.Ephi,3)
        self.Epsi3 = np.power(self.Epsi,3)
        self.Esa3 = np.power(self.Esa,3)

        # Other relevant info
        self.TMScore = self.data[:,3]
        self.Serial = self.data[:,0]
        self.Native = self.data[:,1]
        self.numProts = np.shape(self.data)[0]


        # Default Model 1
        self.eData = None

    def setModelInfo(self,model):
        """
        Set our data to whichever Model is chosen
        """
        if model == 1:
            self.eData = np.column_stack((self.Ereg,self.Ep1,self.Ep2,self.Enp,self.Ephi,self.Epsi,self.Esa))
        elif model == 2:
            self.eData = np.column_stack((self.Ereg,self.Ep1,self.Ep2,self.Enp,self.Ephi,self.Epsi,self.Esa,
                self.Ereg2,self.Ep12,self.Ep22,self.Enp2,self.Ephi2,self.Epsi2,self.Esa2))
        elif model == 3:
            self.eData = np.column_stack((self.Ereg,self.Ep1,self.Ep2,self.Enp,self.Ephi,self.Epsi,self.Esa,
                self.Ereg2,self.Ep12,self.Ep22,self.Enp2,self.Ephi2,self.Epsi2,self.Esa2,
                self.Ereg3,self.Ep13,self.Ep23,self.Enp3,self.Ephi3,self.Epsi3,self.Esa3))
        elif model == 4:
            self.eData = np.column_stack((self.ones,self.Ereg,self.Ep1,self.Ep2,self.Enp,self.Ephi,self.Epsi,self.Esa))
        elif model == 5:
            self.eData = np.column_stack((self.ones,self.Ereg,self.Ep1,self.Ep2,self.Enp,self.Ephi,self.Epsi,self.Esa,
                self.Ereg2,self.Ep12,self.Ep22,self.Enp2,self.Ephi2,self.Epsi2,self.Esa2))
        elif model == 6:
            self.eData = np.column_stack((self.ones,self.Ereg,self.Ep1,self.Ep2,self.Enp,self.Ephi,self.Epsi,self.Esa,
                self.Ereg2,self.Ep12,self.Ep22,self.Enp2,self.Ephi2,self.Epsi2,self.Esa2,
                self.Ereg3,self.Ep13,self.Ep23,self.Enp3,self.Ephi3,self.Epsi3,self.Esa3))
        else:
            print "WHAT THE DEUCE!!! NO MODEL SELECTED!!!"

    def getNative(self,model):
        Ereg = self.nativeRow[5]
        Ep1 = self.nativeRow[6]
        Ep2 = self.nativeRow[7]
        Enp = self.nativeRow[8]
        Ephi = self.nativeRow[9]
        Epsi = self.nativeRow[10]
        Esa = self.nativeRow[11]
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
        ones = np.ones(1)

        if model == 1:
            return np.column_stack((Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa))
        elif model == 2:
            return np.column_stack((Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                    Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2))
        elif model == 3:
            return np.column_stack((Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                    Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2,
                                    Ereg3,Ep13,Ep23,Enp3,Ephi3,Epsi3,Esa3,))
        elif model == 4:
            return np.column_stack((ones,Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa))
        elif model == 5:
            return np.column_stack((ones,Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                    Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2))
        elif model == 6:
            return np.column_stack((ones,Ereg,Ep1,Ep2,Enp,Ephi,Epsi,Esa,
                                    Ereg2,Ep12,Ep22,Enp2,Ephi2,Epsi2,Esa2,
                                    Ereg3,Ep13,Ep23,Enp3,Ephi3,Epsi3,Esa3,))
        else:
            print "CHOSE WRONG MODEL FOR NATIVE"

    def square(self,col):
        sign = np.sign(col)
        square = np.square(col)
        return np.multiply(sign,square)


class DataSet(object):
    """ 
    DataSet for Protein Energy Function Project in Pattern Rec

    Initialization will load all files as numpy 2d arrays with appropriate
    info
    Walk all files in that directory, open each csv, store it in memory
    close the files
    """

    def __init__(self,name):
        self.name = name
        self.dataSetPath = "../data/DataSet" + name
        self.dataFiles = {}
        foo = os.walk(self.dataSetPath)
        bar = foo.next()
        for elem in bar[2]:
            self.dataFiles[elem] = DataFile(self.dataSetPath + "/" + elem)
        self.numTotalProts = 0
        for k,v in enumerate(self.dataFiles):
            self.numTotalProts += self.dataFiles[v].numProts
        self.numProts = len(self.dataFiles)

    def setModel(self,model):
        for k,v in enumerate(self.dataFiles):
            self.dataFiles[v].setModelInfo(model)

    def __iter__(self):
        for k,v in enumerate(self.dataFiles):
            yield self.dataFiles[v]
