# coding: utf-8
import data
import fitness
import population
c9 = data.DataSet('C9')
dList = [c9]
dList
def calculateZScore(self,_betas,_dataSetList,model):
    """
    Calculates Zscore (F3) for a chromosome
        _chromosome is the chromosome
        _dataSetList is a list of DataSet objects
    """

    totalNumProts = sum([x.numProts for x in _dataSetList])
    totalF3 = 0.0
    zScoreAvg = 0.0
    zScore = {}

    for dSet in _dataSetList:
        perFileF3 = 0.0
        for protein in dSet:
            eNative = np.dot(protein.getNative(model),_betas)
            eBetters = np.dot(protein.eData,_betas)
            eAvg = np.mean(eBetters)
            eSd = np.std(eBetters)
            perFileF3 += (eNative - eAvg) / eSd
        zScore[dSet.name] = perFileF3 / dSet.numProts
    for k,v in enumerate(zScore):
        zScoreAvg += zScore[v]
    zScoreAvg /= float(len(zScore))
    return zScore,zScoreAvg
betaModel1 = np.array([3.97265625,0.31738281,3.7421875,0.16113281,0.07421875,1.02636719,0.45605469])
import numpy as np
betaModel1 = np.array([3.97265625,0.31738281,3.7421875,0.16113281,0.07421875,1.02636719,0.45605469])
calculateZScore(betaModel1,dList,1)
def calculateZScore(_betas,_dataSetList,model):
    """
    Calculates Zscore (F3) for a chromosome
        _chromosome is the chromosome
        _dataSetList is a list of DataSet objects
    """

    totalNumProts = sum([x.numProts for x in _dataSetList])
    totalF3 = 0.0
    zScoreAvg = 0.0
    zScore = {}

    for dSet in _dataSetList:
        perFileF3 = 0.0
        for protein in dSet:
            eNative = np.dot(protein.getNative(model),_betas)
            eBetters = np.dot(protein.eData,_betas)
            eAvg = np.mean(eBetters)
            eSd = np.std(eBetters)
            perFileF3 += (eNative - eAvg) / eSd
        zScore[dSet.name] = perFileF3 / dSet.numProts
    for k,v in enumerate(zScore):
        zScoreAvg += zScore[v]
    zScoreAvg /= float(len(zScore))
    return zScore,zScoreAvg
calculateZScore(betaModel1,dList,1)
def calculateZScore(_betas,_dataSetList,model):
    """
    Calculates Zscore (F3) for a chromosome
        _chromosome is the chromosome
        _dataSetList is a list of DataSet objects
    """

    totalNumProts = sum([x.numProts for x in _dataSetList])
    totalF3 = 0.0
    zScoreAvg = 0.0
    zScore = {}

    for dSet in _dataSetList:
        perFileF3 = 0.0
        for protein in dSet:
            print protein
            print protein.getNative(model)
            eNative = np.dot(protein.getNative(model),_betas)
            eBetters = np.dot(protein.eData,_betas)
            eAvg = np.mean(eBetters)
            eSd = np.std(eBetters)
            perFileF3 += (eNative - eAvg) / eSd
        zScore[dSet.name] = perFileF3 / dSet.numProts
    for k,v in enumerate(zScore):
        zScoreAvg += zScore[v]
    zScoreAvg /= float(len(zScore))
    return zScore,zScoreAvg
calculateZScore(betaModel1,dList,1)
c9.setModel(1)
calculateZScore(betaModel1,dList,1)
def calculateZScore(_betas,_dataSetList,model):
    """
    Calculates Zscore (F3) for a chromosome
        _chromosome is the chromosome
        _dataSetList is a list of DataSet objects
    """

    totalNumProts = sum([x.numProts for x in _dataSetList])
    totalF3 = 0.0
    zScoreAvg = 0.0
    zScore = {}

    for dSet in _dataSetList:
        perFileF3 = 0.0
        for protein in dSet:
            eNative = np.dot(protein.getNative(model),_betas)
            eBetters = np.dot(protein.eData,_betas)
            eAvg = np.mean(eBetters)
            eSd = np.std(eBetters)
            perFileF3 += (eNative - eAvg) / eSd
        zScore[dSet.name] = perFileF3 / dSet.numProts
    for k,v in enumerate(zScore):
        zScoreAvg += zScore[v]
    zScoreAvg /= float(len(zScore))
    return zScore,zScoreAvg
betaModel2 = np.array([2.4375,	3.11523438, 3.32421875,	1.47363281,	2.2265625,	1.19921875,	1.35644531,	3.03613281,	2.29980469,	3.31542969,	3.80664062,	0.97753906,	0.01953125,	0.20703125])
betaModel2
c9.setModel(2)
calculateZScore(betaModel2,dList,2)
betaModel3 = np.array([3.40722656,	3.45898438,	1.94042969,	0.66894531,	2.26074219,	1.56054688,	0.20019531,	2.32226562,	2.03320312,	3.63964844,	1.328125,	0.04394531,	2.98046875,	0.60351562,	2.22753906,	0.86523438,	2.07714844,	1.03222656,	3.453125,	0.33496094,	0.0390625])
c9.setModel(3)
calculateZScore(betaModel3,dList,3)
betaModel4 = np.array([3.51855469,	3.1015625,	0.22753906,	1.4609375,	1.953125,	0.12890625,	1.05175781,	0.29785156])
c9.setModel(4)
calculateZScore(betaModel4,dList,4)
betaModel2 = np.array([2.4375,	3.03613281,	3.11523438,	2.29980469,	3.32421875,	3.31542969,	1.47363281,	3.80664062,	2.2265625,	0.97753906,	1.19921875	,0.01953125,	1.35644531,	0.20703125])
c9.setModel(2)
calculateZScore(betaModel2,dList,2)
dList[0].setModel(2)
calculateZScore(betaModel2,dList,2)
betaModel3 = np.array([3.40722656,	2.32226562,	2.22753906,	3.45898438,	2.03320312,	0.86523438,	1.94042969,	3.63964844,	2.07714844,	0.66894531,	1.328125,	1.03222656,	2.26074219,	0.04394531,	3.453125	,1.56054688,	2.98046875,	0.33496094,	0.20019531,	0.60351562,	0.0390625])
c9.setModel(3)
calculateZScore(betaModel3,dList,3)
betaModel5 = np.array([1.21484375,	1.4375,	3.49902344,	1.42675781,	3.19726562,	2.078125,	1.44628906,	0.21386719,	3.74121094,	3.23730469,	1.73242188,	1.94824219,	0.04589844,	0.94824219,	0.15722656])
c9.setModel(5)
calculateZScore(betaModel5,dList,5)
betaModel6 = np.array([0.09082031,	2.34863281,	0.4609375,	3.03125,	3.36523438,	2.09960938,	2.81347656,	1.59277344,	3.22558594,	1.7265625,	3.52441406,	1.38378906,	2.92480469,	3.15136719,	3.90234375,	3.5546875,	0.11523438,	1.01953125,	1.109375,	0.15429688,	0.66894531,	0.01757812])
c9.setModel(6)
calculateZScore(betaModel6,dList,6)