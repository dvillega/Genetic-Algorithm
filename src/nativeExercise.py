# coding: utf-8
import data
import fitness
import population
def loadData(model):
    """

    """
    c8 = data.DataSet('C8')
    R = data.DataSet('R')
    M = data.DataSet('M')
    T = data.DataSet('T')

    dataSetList = [c8, R, M, T]
    for elem in dataSetList:
        elem.setModel(model)
    return dataSetList
loadData(1)
dataSetList = loadData(1)
c9 = data.DataSet('C9')
numpy
import numpy as np
pop1 = population.Population(4,2,200)
pop1
pop1.pop[0]
pop1.pop[0].betas()
native = np.array([1.0,0.0,0.0,0.0,0.0,0.0])
native
native = np.array([1.0,0.0,0.0,0.0,0.0,0.0,0.0])
fit = fitness.Fitness(False)
native = population.Chromosome(4,7,2.0,True)
native
native.genes
native.betas()
native.genes
native.genes[0]
from bitarray import bitarray
test = bitarray('1000')
test
native.genes[0] = test
native.genes
native.betas()
test = bitarray('0111')
native.genes[0] = test
native.betas()
test = bitarray('0000')
native.betas()
native.genes[1] = test
native.betas()
native = np.array[1.0,0.0,0.0,0.0,0.0,0.0,0.0]
native = np.array([1.0,0.0,0.0,0.0,0.0,0.0,0.0])
native
sumTMScores = 0.0
totF1 = 0.0
for protein in dataSetList[0]:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eBetter)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eBetter, protein.TMScore)[0]
    
for protein in dataSetList[0]:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
import scipy.stats as stats
for protein in dataSetList[0]:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
f1 = totF1 / dataSetList[0].numProts
f2 = sumTMScores / dataSetList[0].numProts
print f1,f2
sumTMScores = 0.0
sumTMScores = 0.0
dSet = dataSetList[1]
for protein in dataSetList[0]:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
    
sumTMScores = 0.0
totF1 = 0.0
for protein in dSet:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
f1 = totF1 / dSet.numProts
f2 = sumTMScores / dSet.numProts
print f1,f2
sumTMScores = 0.0
totF1 = 0.0
for protein in dSet:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
f1 = totF1 / dSet.numProts
f2 = sumTMScores / dSet.numProts
print dSet.name,f1,f2
dSet = dataSetList[2]
sumTMScores = 0.0
totF1 = 0.0
for protein in dSet:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
f1 = totF1 / dSet.numProts
f2 = sumTMScores / dSet.numProts
print dSet.name,f1,f2
dSet = dataSetList[3]
sumTMScores = 0.0
totF1 = 0.0
for protein in dSet:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
f1 = totF1 / dSet.numProts
f2 = sumTMScores / dSet.numProts
print dSet.name,f1,f2
c9
dSet = c9
sumTMScores = 0.0
totF1 = 0.0
for protein in dSet:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
f1 = totF1 / dSet.numProts
f2 = sumTMScores / dSet.numProts
print dSet.name,f1,f2
native
c9
c9 = data.DataSet('C9')
c9.setModel(1)
dSet = c9
sumTMScores = 0.0
totF1 = 0.0
for protein in dSet:
    eNative = np.dot(protein.eData,native)
    indexTM = np.argmin(eNative)
    sumTMScores += protein.TMScore[indexTM]
    totF1 += stats.pearsonr(eNative, protein.TMScore)[0]
f1 = totF1 / dSet.numProts
f2 = sumTMScores / dSet.numProts
print dSet.name,f1,f2
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
calculateZScore(native,dataSetList,1)
dataSetList
dataSetList = [dataSetList c9]
dataSetList = [dataSetList,c9]
dataSetList
calculateZScore(native,dataSetList,1)
dataSetList
dataSetList[0]
listD = dataSetList[0]
listD.append(c9)
listD
calculateZScore(native,listD,1)