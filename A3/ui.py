# -*- coding: utf-8 -*-


# imports
from gui import *
from controller import *
from repository import *
from domain import *
import datetime


class UI:
    def __init__(self):
        self.repo = Repository()
        self.controller = Controller()
        self.iterations = 20
        self.population_size = 100
        self.population_gene_size = 10

    @staticmethod
    def menu():
        print("0.Exit")
        print("1.Create Random Map")
        print("2.Load a Population")
        print("3.Save a Population")
        print("4.Visualize current Population")

    def run(self):
        while True:
            self.menu()
            option = input("choice > ")
            if option == "0":
                break
            elif option == "1":
                current_map = Map()
                current_map.randomMap()
                self.repo.setMap(current_map)

                self.controller.setRepo(self.repo)

                start_time = datetime.datetime.now()
                population = self.controller.solver(
                    self.iterations,
                    self.population_size,
                    self.population_gene_size
                )
                end_time = datetime.datetime.now()

                print("Execution time:", end_time-start_time)

                best = population.Best
                print(best.path)
                movingDrone(current_map, best.path)

            elif option == "2":
                file_name = input("file name > ")
                self.repo.file_name = file_name
                self.repo.load_from_file()
                population = self.repo.getPopulation()
                # population.evaluate()
                best = population.Best
                print(best.path)
                movingDrone(self.repo.getMap(), best.path)

            elif option == "3":
                file_name = input("file name > ")
                self.repo.file_name = file_name
                self.repo.save_to_file()

            elif option == "4":
                movingDrone(
                    self.repo.getMap(),
                    self.repo.getPopulation().Best.path
                )

                # controller = Controller(current_map, repo)
                # best = max(res)
                # b = population[res.index(best)]
                # # print(res)
                # print(b.path)
                # paths = []
                # for p in population:
                #     paths.append(p.path)
                # display_paths(current_map, paths)
                # print(paths[0])
                # for p in population.Individuals:
                #     movingDrone(current_map,p.path)
                # movingDrone(current_map,b.path)
                # population.evaluate()


if __name__ == "__main__":
    ui = UI()
    ui.run()

# create a menu
#   1. map options:
#         a. create random map
#         b. load a map
#         c. save a map
#         d visualise map
#   2. EA options:
#         a. parameters setup
#         b. run the solver
#         c. visualise the statistics
#         d. view the drone moving on a path
#              function gui.movingDrone(currentMap, path, speed, markseen)
#              ATTENTION! the function doesn't check if the path passes trough walls
