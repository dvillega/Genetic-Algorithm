import numpy as np
from bitarray import bitarray
""" Population for genetic algorithm - Pattern Rec Prog Assign 1
If we pass true to the constructor then the population will initialize as
random"""

class Chromosome(object):

    def __init__(self,geneLength,numGenes,betaMax,initialize=True):
        self.geneLength = geneLength
        self.fitness = 0.0
        self.betaMax = betaMax
        self.genes = []
        self.numGenes = numGenes
        if initialize:
            for i in xrange(self.numGenes):
                self.genes.append(bitarray(np.binary_repr(np.random.randint(0,2**self.geneLength),width=self.geneLength)))

    def betaFromGene(self,gene):
        # Expects a numpy array of bools as a gene, returns a
        # real value beta from our gene
        delta = float(self.betaMax)/(2**self.geneLength)
        beta = delta
        for i,val in enumerate(gene):
            foo = 2**(self.geneLength-(i+1)) * val
            beta += (foo * delta)
        return beta

    def copyGenes(self,genes):
        self.genes = genes

    def betas(self):
        newBetas = []
        for elem in self.genes:
            newBetas.append(self.betaFromGene(elem))
        return np.array(newBetas)

    def randomizeGenes(self):
        # Randomize this chromosome's genes
        self.genes = []
        for i in xrange(self.numGenes):
            self.genes.append(bitarray(np.binary_repr(
                np.random.randint(0,2**self.geneLength),width=self.geneLength)))

    def mutateGene(self):
        pos = np.random.randint(0,self.geneLength*self.numGenes)
        genePos = pos / self.geneLength
        flipBit = pos % self.geneLength
        print genePos,flipBit
        self.genes[genePos][flipBit] = not self.genes[genePos][flipBit]



class Population(object):

    # Constructor 
    def __init__(self,geneLength,betaMax,popSize,mutationRate=0.025,initialize=True):
        self.pop= []
        self.betaMax = betaMax
        self.geneLength = geneLength
        self.mutationRate = mutationRate
        self.popSize = popSize
        self.numGenes = 7
        if initialize:
            for i in xrange(popSize):
                self.pop.append(Chromosome(self.geneLength,self.numGenes,self.betaMax))
        else:
            for i in xrange(popSize):
                self.pop.append(Chromosome(self.geneLength,self.numGenes,self.betaMax,False))

    # Returns sorted by fitness population
    def sortedPopulation(self):
        self.pop = sorted(self.pop,key = lambda x: x.fitness, reverse=True)
        return self.pop

    # Returns the top percent of our population according to fitness
    # Default 10%
    def eliteSet(self,percent = 10):
        length = len(self.pop) * percent / 100
        return self.sortedPopulation()[0:length]

    # Apply update your pos1 and pos2 genes
    def applyCrossover(self,pos1,pos2,genes):
        self.pop[pos1].genes = genes[0]
        self.pop[pos2].genes = genes[1]
        if np.random.random < self.mutationRate:
            self.pop[pos1].mutateGene()
        if np.random.random < self.mutationRate:
            self.pop[pos2].mutateGene()

    # return 2 selected genes crossed over
    def crossover(self,pos1,pos2):
        first = self.pop[pos1].genes
        second = self.pop[pos2].genes
        firstString = [x for sublist in first for x in sublist]
        secondString = [x for sublist in second for x in sublist]
        pos = np.random.randint(0,len(firstString))
        newFirst = firstString[:pos]
        newSecond = secondString[:pos]
        newFirst.extend(secondString[pos:])
        newSecond.extend(firstString[pos:])
        newGenes = []
        newGenes.append([bitarray(newFirst[i:i+self.geneLength]) for i in
                range(0,len(newFirst),self.geneLength)])
        newGenes.append([bitarray(newSecond[i:i+self.geneLength]) for i in
                range(0,len(newSecond),self.geneLength)])
        return newGenes
