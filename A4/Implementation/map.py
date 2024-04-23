import numpy
import random
import pickle
import pygame

from constants import *


class Map:
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = numpy.zeros((n, m))
        self.pheromone_level = numpy.zeros((n, m))
        self.sensors = []
        self.minimum_distance_between_sensors = {}
        # print(self.surface)

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random.random() <= fill:
                    self.surface[i][j] = 1

    def saveMap(self, numFile="test.map"):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    @property
    def Sensors(self):
        return self.sensors

    @Sensors.setter
    def Sensors(self, list_of_sensors):
        self.sensors = list_of_sensors
        # for i in range(self.n):
        #     for j in range(self.m):
        #         if self.surface[i][j] == 2:
        #             self.surface[i][j] = 0
        for sensor in list_of_sensors:
            self.surface[sensor[0]][sensor[1]] = 2

    def loadMap(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            self.sensors = dummy.sensors
            self.pheromone_level = dummy.pheromone_level
            # self.minimum_distance_between_sensors = dummy.minimum_distance_between_sensors
            f.close()

    def image(self, colour=BLUE, background=WHITE):
        imagine = pygame.Surface((20*self.n, 20*self.m))

        brick = pygame.Surface((20, 20))
        brick.fill(BLUE)

        sensor = pygame.Surface((20, 20))
        sensor.fill(RED)

        imagine.fill(WHITE)
        for i in range(self.n):
            for j in range(self.m):
                if (self.surface[i][j] == 1):
                    imagine.blit(brick, (j * 20, i * 20))
                elif (self.surface[i][j] == 2):
                    imagine.blit(sensor, (j * 20, i * 20))

        return imagine

    def image_path(self, visited, finalX = -1,  finalY = -1):
        imagine = pygame.Surface((20*self.n, 20*self.m))

        brick = pygame.Surface((20, 20))
        brick.fill(BLUE)

        visited_brick = pygame.Surface((20, 20))
        visited_brick.fill(GREEN)

        seen_by_sensor = pygame.Surface((20, 20))
        seen_by_sensor.fill(YELLOW)

        sensor = pygame.Surface((20, 20))
        sensor.fill(RED)

        imagine.fill(WHITE)
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) in visited:
                    imagine.blit(visited_brick, (j * 20, i * 20))
                elif self.surface[i][j] == 3:
                    imagine.blit(seen_by_sensor, (j * 20, i * 20))
                elif (self.surface[i][j] == 2):
                    imagine.blit(sensor, (j * 20, i * 20))
                if (self.surface[i][j] == 1):
                    imagine.blit(brick, (j * 20, i * 20))

        return imagine

    def image_sensors(self, seen_squares):
        imagine = pygame.Surface((20*self.n, 20*self.m))

        brick = pygame.Surface((20, 20))
        brick.fill(BLUE)

        seen_by_sensor = pygame.Surface((20, 20))
        seen_by_sensor.fill(YELLOW)


        sensor = pygame.Surface((20, 20))
        sensor.fill(RED)

        imagine.fill(WHITE)
        for i in range(self.n):
            for j in range(self.m):
                if (i,j) in seen_squares:
                    imagine.blit(seen_by_sensor, (j * 20, i * 20))
                elif (self.surface[i][j] == 1):
                    imagine.blit(brick, (j * 20, i * 20))
                if (self.surface[i][j] == 2):
                    imagine.blit(sensor, (j * 20, i * 20))

        return imagine

    def mark(self, seen, value):
        for point in seen:
            self.surface[point[0]][point[1]] = value

# m = Map()
