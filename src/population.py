import numpy as np
import bitarray as bit
""" Population for genetic algorithm - Pattern Rec Prog Assign 1"""

class Population(object):

    def __init__(self,initialize):
        self.pop= []
        if initialize:
            for i in xrange(200):
                self.pop.append((self.rand4BitChromosomeM1(),float(i)))

    def rand4BitChromosomeM1(self):
        a = bit.bitarray(bin(np.random.randint(0,16))[2:])
        for i in xrange(7):
            a.extend(bit.bitarray(bin(np.random.randint(0,16))[2:]))
        return a

    def sortedPopulation(self):
        self.pop = sorted(self.pop,key = lambda x: x[1], reverse=True)
        return self.pop
