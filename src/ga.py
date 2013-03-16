""" Genetic Algorithm """

import data
import fitness
import population
import copy
from time import time

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

model = 1

c8 = data.DataSet('C8',model)
R = data.DataSet('R',model)
M = data.DataSet('M',model)
T = data.DataSet('T',model)

dataSetList = [c8, R, M, T]

loadTime = time() - start



FIT = fitness.Fitness(True)
pop1 = population.Population(12,4.0,200,numGenes=f(model),mutationRate=0.025,initialize=True)
pop2 = population.Population(12,4.0,200,numGenes=f(model),mutationRate=0.025,initialize=False)
outFH = open('output.txt','w')
for elem in pop1:
    elem.fitness = FIT.calculateTotalFitness(elem.betas(),dataSetList)
pop1.sortPopulation()
outFH.write('Starting Population \n')
outFH.write(str(pop1) + '\n')
outFH.write(pop1.topBetas())
outFH.write('\n')

for i in xrange(100):
    pop2.stepGeneration(pop1)
    for elem in pop2:
        elem.fitness = FIT.calculateTotalFitness(elem.betas(),dataSetList)
    pop2.sortPopulation()
    pop1 = copy.deepcopy(pop2)

pop1.sortPopulation()
outFH.write('\n\nFinal\n')
outFH.write(str(pop1) + '\n')
outFH.write(pop1.topBetas())
outFH.close()


end = time()
elapsed = end - start
elapsed /= 60.0
loadTime /= 60.0
print "Time Loading: " + str(loadTime) + '\n'
print "Time Processing: " + str((elapsed - loadTime)) + '\n'
print "Time per step: " + str((elapsed - loadTime) / 100) + '\n'
print "Minutes spent Total: " + str(elapsed) + '\n'
