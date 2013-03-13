import numpy as np
from bitarray import bitarray
""" Population for genetic algorithm - Pattern Rec Prog Assign 1
If we pass true to the constructor then the population will initialize as
random"""

class Population(object):

    def __init__(self,initialize,geneLength,betaMax):
        self.pop= []
        self.betaMax = betaMax
        self.geneLength = geneLength
        if initialize:
            for i in xrange(200):
                self.pop.append((self.randBitGeneM1(),float(i)))

    # Generates a random length bit gene
    def randBitGeneM1(self):
        # The bin function truncates leading zeros,
        # so we need the while loop to make sure all 
        # genes are of appropriate length
        foo = bin(np.random.randint(0,2**self.geneLength))[2:]
        while(len(foo) != self.geneLength):
            foo = "0" + foo
        returnVal = bitarray(foo)
        for i in xrange(6):
            foo = bin(np.random.randint(0,2**self.geneLength))[2:]
            while (len(foo) != self.geneLength):
                foo = "0" + foo
            returnVal.extend(bitarray(foo))
        return returnVal

    def sortedPopulation(self):
        self.pop = sorted(self.pop,key = lambda x: x[1], reverse=True)
        return self.pop

    # Can loop through and update population fitness scores as we go

    # Currently covers 0-max beta values
    def bit2BGene(self,bitVals):
        length = len(bitVals)
        delta = float(self.betaMax)/(2**length)
        beta = delta
        for i,elem in enumerate(bitVals):
            foo = 2**(length-(i+1)) * elem
            beta += (foo * delta)
        return beta

    def bit2BChromo(self,bitVals):
        # Split chromosome into 4 len bit arrays
        splits = [bitVals[i:i+4] for i in range(0,len(bitVals), 4)]
        newBetas = []
        for elem in splits:
            newBetas.append(self.bit2BGene(elem))
        return np.array(newBetas)

    # Returns the top percent of our population according to fitness
    # Default 10%
    def eliteSet(self,percent = 10):
        length = len(self.pop) * percent / 100
        return self.sortedPopulation()[0:length]

    # Applies mutation to all but the elite set - skip random set
    def mutationSet(self,popToMutate):
        # Mutation code here
         pass

    # Apply crossover to all but the elite set - skip random
    def crossoverSet(self):
        # Crossover code here
        pass
