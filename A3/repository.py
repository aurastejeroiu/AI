# -*- coding: utf-8 -*-

import pickle
from domain import *


class Repository():
    def __init__(self, population=Population, map=Map(), file_name="default.txt"):
        self.__population = population
        self.cmap = map
        self.file_name = file_name

    def createPopulation(self,  population_size, individual_size):
        # args = [populationSize, individualSize] -- you can add more args
        self.__population = Population(self.cmap, population_size, individual_size)
        return self.__population

    # TO DO : add the other components for the repository:
    #    load and save from file, etc
    def getMap(self):
        return self.cmap

    def getPopulation(self):
        return self.__population

    def setMap(self, new_map):
        self.cmap = new_map

    def save_to_file(self):
        with open(self.file_name, "wb") as f:
            pickle.dump(self, f)

    def setPopulation(self, new_population):
        self.__population = new_population

    def load_from_file(self):
        with open(self.file_name, "rb") as f:
            dummy = pickle.load(f)
            self.__population = dummy.__population
            self.cmap = dummy.cmap
            self.file_name = dummy.file_name
