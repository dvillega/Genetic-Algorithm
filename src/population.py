import numpy as np
from bitarray import bitarray
""" Population for genetic algorithm - Pattern Rec Prog Assign 1
If we pass true to the constructor then the population will initialize as
random"""

class Population(object):

    def __init__(self,initialize):
        self.pop= []
        if initialize:
            for i in xrange(200):
                self.pop.append((self.rand4BitGeneM1(),float(i)))

    # Generates a random 4 bit gene
    def rand4BitGeneM1(self):
        # The bin function truncates leading zeros,
        # so we need the while loop to make sure all 
        # genes are of len 4
        foo = bin(np.random.randint(0,16))[2:]
        while(len(foo) != 4):
            foo = "0" + foo
        a = bitarray(foo)
        for i in xrange(7):
            foo = bin(np.random.randint(0,16))[2:]
            while (len(foo) != 4):
                foo = "0" + foo
            a.extend(bitarray(foo))
        return a

    def sortedPopulation(self):
        self.pop = sorted(self.pop,key = lambda x: x[1], reverse=True)
        return self.pop

    # Can loop through and update population fitness scores as we go

    def bit2BSingle(self,bitVals):
        length = len(bitVals)
        delta = 0.125
        beta = 0.125
        for i,elem in enumerate(bitVals):
            foo = 2**(length-(i+1)) * elem
            beta += (foo * delta)
        return beta

    def bit2BChromo(self,bitVals):
        # Split chromosome into 4 len bit arrays
        splits = [bitVals[i:i+4] for i in range(0,len(bitVals), 4)]
        newBetas = []
        for elem in splits:
            newBetas.append(self.bit2BSingle(elem))
        return np.array(newBetas)

    def eliteSet(self,percent):
        length = len(self.pop) * percent / 100
        return self.sortedPopulation()[0:length]
