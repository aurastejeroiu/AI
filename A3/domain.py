# -*- coding: utf-8 -*-

from random import *
from utils import *
import numpy as np
import datetime



# the glass gene can be replaced with int or float, or other types
# depending on your problem's representation


class Gene:
    def __init__(self):
        # random initialise the gene according to the representation
        # gene is a list of m elements (number of steps before battery dies) - well now it isn't anymore :)
        # values in the range 0-3 representing the possible moves up, right, down, left
        # TODO: seed = ?
        seed(datetime.datetime.now())
        self.value = randint(0, 3)
        pass

    def __str__(self):
        return str(self.value)


class Individual:
    def __init__(self, size=0, initial_position=(9, 9)):
        self.__size = size
        self.__x = [Gene() for i in range(self.__size)]
        self.__f = None
        self.score = -1
        self.path = []
        self.initial_position = initial_position

    def distance_from_start(self):
        initial_x = self.initial_position[0]
        initial_y = self.initial_position[1]
        final_x = self.path[self.__size - 1][0]
        final_y = self.path[self.__size - 1][1]
        return abs(final_x - initial_x) + abs(final_y - initial_y)

    def fitness(self, map):
        # print(map)
        # compute the fitness for the indivisual
        # and save it in self.__f
        # fitness will be defined by the size of the area that an individual discovered
        # for i in range(map.n):
        #     for j in range(map.m):
        #         if self.surface[i][j] == -1:
        path = [self.initial_position]
        for i in range(1, len(self.__x)):
            d = directions[self.__x[i].value]
            last = path[-1]
            x = last[0] + d[0]
            y = last[1] + d[1]
            path.append((x, y))

        self.path = path
        self.score = 0
        # print(path)
        seen = {}
        for i in range(len(path)):
            for j in range(i + 1):
                for var in directions:
                    x = path[j][0]
                    y = path[j][1]
                    while ((0 <= x + var[0] < map.n and
                            0 <= y + var[1] < map.m) and
                           map.surface[x + var[0]][y + var[1]] != 1):
                        x = x + var[0]
                        y = y + var[1]
                        seen[(x, y)] = 1
            x = path[j][0]
            y = path[j][1]
            if not (0 <= x < map.n and 0 <= y < map.m):
                self.score -= 20
            elif map.surface[x][y] == 1:
                self.score -= 10

        self.score += len(seen)
        distance = self.distance_from_start()
        self.score -= distance * 10
        # print(len(seen))
        return self.score

    def setGene(self, genes):
        self.__x = genes

    def __str__(self):
        result = "[ "
        for g in self.__x:
            result += str(g) + ", "
        result += ("] Fitness = " + str(self.score))
        return result

    @property
    def Score(self):
        return self.score

    @property
    def Size(self):
        return self.__size

    @property
    def Gene(self):
        return self.__x

    def mutate(self, mutateProbability=0.2):
        for _ in range(self.Size):
            seed(datetime.datetime.now())
            if random() < mutateProbability:
                index = randint(0, self.Size - 1)
                self.__x[index] = Gene()
            pass
            # perform a mutation with respect to the representation
            # this would just replace a value from the gene with a random one

    def crossover(self, otherParent, crossoverProbability=0.8):
        offspring1, offspring2 = Individual(
            self.__size), Individual(self.__size)
        seed(datetime.datetime.now())
        if random() < crossoverProbability:
            # perform the crossover between the self and the otherParent
            # I think of using an N-cutting point crossover for this
            # I believe that if we do some average between parents or permutations on this
            # specific representation we will not advance, only by chance maybe ?
            othergene = otherParent.Gene
            mid = randint(0, self.Size - 1)
            # print(mid)
            # print(self.__size)
            off1_gene = self.__x[:mid]
            off2_gene = othergene[:mid]
            off1_gene.extend(othergene[mid:])
            off2_gene.extend(self.__x[mid:])
            # print(off1_gene)
            offspring1.setGene(off1_gene)
            offspring2.setGene(off2_gene)

        return offspring1, offspring2


class Population:
    def __init__(self, current_map, populationSize=0, individualSize=0):
        self.__populationSize = populationSize
        self.__v = [Individual(individualSize)
                    for x in range(populationSize)]
        self.map = current_map

    def evaluate(self):
        # evaluates the population
        results = []
        for x in self.__v:
            results.append(x.fitness(self.map))
        # maybe also sort them by their fitness
        return results, self.__v

    def selection(self, k=0):
        # perform a selection of k individuals from the population
        # and returns that selection
        # the best k

        self.__v.sort(key=lambda x: x.score, reverse=True)
        return self.__v[:k]
        pass

    def add(self, individual):
        self.__v.append(individual)
        self.__populationSize += 1

    @property
    def Best(self):
        self.__v.sort(key=lambda x: x.score, reverse=True)
        return self.__v[0]

    @property
    def Average(self):
        res = 0
        for x in self.__v:
            res += x.score
        return res / self.Size

    @property
    def Individuals(self):
        return self.__v

    @property
    def Size(self):
        # return self.__populationSize
        return len(self.__v)

    @property
    def IndividualSize(self):
        return self.__v[0].Size

    @property
    def Fitness(self):
        fitness = []
        for i in self.__v:
            fitness.append(i.Score)
        return fitness

    def __str__(self):
        result = "Population: \n"
        for i in self.__v:
            result += str(i) + '\n'
        return result


class Map():
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string
