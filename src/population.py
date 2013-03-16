import numpy as np
from bitarray import bitarray
""" Population for genetic algorithm - Pattern Rec Prog Assign 1
If we pass true to the constructor then the population will initialize as
random"""


class Chromosome(object):

    def __init__(self,geneLength,numGenes,betaMax,initialize=True):
        self.geneLength = geneLength
        self.fitness = 0.0
        self.chromosomeLength = geneLength * numGenes
        self.fVals = {}
        self.betaMax = betaMax
        self.genes = []
        self.numGenes = numGenes
        if initialize:
            for i in xrange(self.numGenes):
                self.genes.append(bitarray(np.binary_repr(np.random.randint(0,2**self.geneLength),width=self.geneLength)))

    def betaFromGene(self,gene):
        # returns a real value beta from our gene
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

    def mutateGene(self,mutationRate):
        numMutations = int(mutationRate * float(self.chromosomeLength) / 100.0)
        for i in xrange(numMutations):
            pos = np.random.randint(0,self.chromosomeLength)
            genePos = pos / self.geneLength
            flipBit = pos % self.geneLength
            self.genes[genePos][flipBit] = not self.genes[genePos][flipBit]

    def __str__(self):
        return 'Total Fitness = ' + str(self.fitness)
#        returnVal = ",".join( [ str(element)[10:10+self.geneLength] for element in self.genes ] )
#        return returnVal + ',fitness=' + str(self.fitness)

class Population(object):

    # Constructor 
    def __init__(self,geneLength,betaMax,popSize,numGenes=7,initialize=True):
        self.pop= []
        self.betaMax = betaMax
        self.geneLength = geneLength
        self.popSize = popSize
        self.numGenes = numGenes
        if initialize:
            for i in xrange(popSize):
                self.pop.append(Chromosome(self.geneLength,self.numGenes,self.betaMax))
        else:
            for i in xrange(popSize):
                self.pop.append(Chromosome(self.geneLength,self.numGenes,self.betaMax,False))
        self.sortPopulation()

    # Sorts population by fitness 
    def sortPopulation(self):
        self.pop = sorted(self.pop,key = lambda x: x.fitness, reverse=True)

    # Returns the top percent of our population according to fitness
    # Default 10%
    def eliteSet(self,percent = 10):
        length = (self.popSize * percent) / 100
        return self.pop[0:length]

    # Apply update your pos1 and pos2 genes
    def applyCrossover(self,pos1,pos2,genes):
        self.pop[pos1].genes = genes[0]
        self.pop[pos2].genes = genes[1]
        self.pop[pos1].mutateGene(np.random.random_integers(5,50))
        self.pop[pos2].mutateGene(np.random.random_integers(5,50))

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

    # Increment this empty population as the GA step of our parameter
    # Population
    #       1- Copy the otherPop's eliteSet into our top 10%
    #       2- Take randomized crossover for 80% (Implement roulette choice)
    #       3- While taking crossovers we are doing mutations
    #       4- Fill last 10% with random
    def stepGeneration(self, otherPop):
        self.pop[0:(self.popSize /10)] = otherPop.eliteSet()
        popTotFit = sum([chromosome.fitness for chromosome in otherPop.pop])

        # Take the normalized fitness as our probabilities to pass to 
        # numpy.random.choice
        wheelProb = [(chromosome.fitness / popTotFit) 
                for chromosome in otherPop.pop]

        # For 40% of the population size, we will step by two and apply crossovers
        for i in xrange((self.popSize * 4) / 10):
            # Randomly choose 2 pos w/o replacement using
            # normalized fitness as our probability
            choices = np.random.choice(range(self.popSize),2,replace=False,p=wheelProb)
            nextPos = (self.popSize / 10) + (i*2)
            self.applyCrossover(nextPos,nextPos + 1,otherPop.crossover(choices[0],choices[1]))
        # Randomize last 10% 
        for elem in self.pop[(self.popSize/10) * 9:]:
            elem.randomizeGenes()

    def topBetas(self):
        # + str(self.pop[0].fVals) + '\n'
        return str(self.pop[0].betas()) + '\n'

    def __iter__(self):
        for elem in self.pop:
            yield elem

    def __str__(self):
        return "\n".join( [ str(element) for element in self.pop] )

