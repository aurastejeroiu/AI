from repository import *
from domain import *
import matplotlib.pyplot as plt
import numpy as np
import threading


class Controller():
    def __init__(self, repo=Repository()):
        # args - list of parameters needed in order to create the controller
        self.repo = repo
        self.map = repo.getMap()
        pass

    def iteration(self, population, args=None):
        # args - list of parameters needed to run one iteration
        # a iteration:
        # selection of the parrents
        # create offsprings by crossover of the parents
        # apply some mutations
        # selection of the survivors
        print("Best:", population.Best, "Average:", population.Average)
        individuals = population.selection(population.Size // 2)
        offsprings = Population(population.map, 0, population.IndividualSize)

        index = 0
        for _ in range(len(individuals) // 2):
            off1, off2 = individuals[index].crossover(individuals[index + 1], 1)
            offsprings.add(off1)
            offsprings.add(off2)
            index += 2

        for _ in range(len(individuals) // 2):
            parents = sample(individuals, 2)
            off1, off2 = parents[0].crossover(parents[1], 1)
            offsprings.add(off1)
            offsprings.add(off2)

        # for i in range(len(individuals)//2):
        #     # parents = sample(individuals, 2)
        #     # off1, off2 = parents[0].crossover(parents[1], 1)
        #     off1, off2 = individuals[i].crossover(
        #         individuals[randint(0, len(individuals)-1)], 1)
        #     offsprings.add(off1)
        #     offsprings.add(off2)
        #     # # print(off1, off2)
        #     # off1, off2 = individuals[index+1].crossover(
        #     #     Individual(population.IndividualSize), 1)
        #     # offsprings.add(off1)
        #     # offsprings.add(individuals[index])

        # for i in range(len(individuals)//4):
        #     parent = individuals[i]
        #     off1, off2 = parent.crossover(
        #         Individual(population.IndividualSize), 1)
        #     offsprings.add(parent)
        #     offsprings.add(off2)

        # for i in range(len(individuals)//2):
        #     offsprings.add(Individual(population.IndividualSize))

        for off in offsprings.Individuals:
            off.mutate(0.02)

        # print(offsprings)
        return offsprings
        pass

    def run(self, initial_population, args=None):
        # args - list of parameters needed in order to run the algorithm

        # until stop condition
        #    perform an iteration
        #    save the information need it for the statistics

        # show some graphs
        new_population = self.iteration(initial_population)
        # return the results and the info for statistics
        new_population.evaluate()
        self.repo.setPopulation(new_population)
        self.repo.save_to_file()
        return new_population

    def solver(self, iterations=100, population_size=50, individual_size=10, args=None):
        # args - list of parameters needed in order to run the solver

        # create the population,
        # run the algorithm
        # return the results and the statistics
        # population = Population(self.map, population_number, max_steps)

        population = self.repo.createPopulation(
            population_size, individual_size
        )
        average = []
        standard_deviation = []
        population.evaluate()
        # average.append(population.Average)
        for _ in range(iterations):
            # x = threading.Thread(target=self.create_graphs, args=(population,))
            # x.start()
            average.append(population.Average)
            # standard_deviation.append(np.std(population.Fitness))
            standard_deviation.append(np.std(population.Fitness))
            # print(population.Fitness)
            self.create_graphs(average, standard_deviation)
            population = self.run(population)
            # print(standard_deviation)

        # self.create_graphs(average)
        # x = threading.Thread(target=self.create_graphs, args=(population,))
        # x.start()

        return population

        pass

    def setRepo(self, new_repo):
        self.repo = new_repo
        self.map = new_repo.getMap()

    def create_graphs(self, average, standard_deviation, best=0):
        # plt.
        plt.plot(average, label="Average Fitness")
        plt.plot(standard_deviation, label="Standard Deviation")
        # plt.plot([best])
        # print(average)
        plt.ylabel('Value')
        plt.xlabel('Iteration Number')
        # x = threading.Thread(target=plt.show(), args=(1,))
        # x.start()
        plt.legend()
        plt.draw()
        plt.pause(1)
        plt.clf()
