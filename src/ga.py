""" Genetic Algorithm """

import data
import fitness
import population
import copy
import sys
from time import time


# Utility mapping to switch on argv model selection
def f(x):
    key = str(x)
    return {
      1:7,
      2:14,
      3:21,
      4:8,
      5:15,
      6:22,
    }[x]

start = time()

model = int(sys.argv[1])

outFilePath = sys.argv[2]
generations = int(sys.argv[3])

c8 = data.DataSet('C8')
R = data.DataSet('R')
M = data.DataSet('M')
T = data.DataSet('T')

dataSetList = [c8, R, M, T]
for elem in dataSetList:
    elem.setModel(model)

loadTime = time() - start



FIT = fitness.Fitness(True)
pop1 = population.Population(12,4.0,200,numGenes=f(model),mutationRate=0.025,initialize=True)
pop2 = population.Population(12,4.0,200,numGenes=f(model),mutationRate=0.025,initialize=False)
outFH = open(outFilePath,'w')
for elem in pop1:
    elem.fitness = FIT.calculateTotalFitness(elem,dataSetList)
pop1.sortPopulation()
outFH.write('Starting Population \n')
outFH.write(pop1.topBetas())

for i in xrange(generations):
    print "Generation: " + str(i)
    pop2.stepGeneration(pop1)
    for elem in pop2:
        elem.fitness = FIT.calculateTotalFitness(elem,dataSetList)
    pop2.sortPopulation()
    outFH.write(pop2.topBetas())
    pop1 = copy.deepcopy(pop2)

pop1.sortPopulation()
outFH.write('\n\nFinal\n')
topPop=pop1.pop[0]
outFH.write(str(topPop.betas()) + '\n')
outFH.close()

# Calculate C9 info
c9 = data.DataSet('C9',model)
topFitC9 = fit.calculateFitness(topPop,C9)
outFH.write('F1 = ' + str(-topFitC9[0]) + ' F2 = ' + str(topFitC9[1]) + '\n')

end = time()
elapsed = end - start
elapsed /= 60.0
loadTime /= 60.0
print "Time Loading: " + str(loadTime) + '\n'
print "Time Processing: " + str((elapsed - loadTime)) + '\n'
print "Time per step: " + str((elapsed - loadTime) / generations) + '\n'
print "Minutes spent Total: " + str(elapsed) + '\n'
