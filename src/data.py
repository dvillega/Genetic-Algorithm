import os
import numpy as np

class DataSet:
""" DataSet for Protein Energy Function Project in Pattern Rec

Initialization will load all files as numpy 2d arrays with appropriate info

"""

    #Constructor - Takes name of DataSet
    def __init__(self,name):
        self.name = name
        self.path = "../data/" + name
        self.data = {}

"""
Walk all files in that directory
open each csv
store it in memory
close the files"""
