import pygame, numpy as np
from Model.utils import *

class DMap:
    def __init__(self, size = 20):
        self.__n = size
        self.__m = size
        self.size = size
        self.surface = np.zeros((self.__n, self.__m))
        for i in range(self.__n):
            for j in range(self.__m):
                self.surface[i][j] = -1

    def markDetectedWalls(self, e, x, y):
        #   To DO
        # mark on this map the wals that you detect
        wals = e.readUDMSensors(x, y)
        i = x - 1
        if wals[UP] > 0:
            while (i >= 0) and (i >= x - wals[UP]):
                self.surface[i][y] = 0
                i = i - 1
        if i >= 0:
            self.surface[i][y] = 1

        i = x + 1
        if wals[DOWN] > 0:
            while (i < self.__n) and (i <= x + wals[DOWN]):
                self.surface[i][y] = 0
                i = i + 1
        if i < self.__n:
            self.surface[i][y] = 1

        j = y + 1
        if wals[LEFT] > 0:
            while (j < self.__m) and (j <= y + wals[LEFT]):
                self.surface[x][j] = 0
                j = j + 1
        if j < self.__m:
            self.surface[x][j] = 1

        j = y - 1
        if wals[RIGHT] > 0:
            while (j >= 0) and (j >= y - wals[RIGHT]):
                self.surface[x][j] = 0
                j = j - 1
        if j >= 0:
            self.surface[x][j] = 1

        return None

    def image(self, x, y, visited_set):

        imagine = pygame.Surface((21 * self.size, 21 * self.size))
        brick = pygame.Surface((20, 20))
        empty = pygame.Surface((20, 20))
        visited = pygame.Surface((20, 20))
        empty.fill(WHITE)
        brick.fill(BLACK)
        visited.fill(GREEN)
        imagine.fill(GRAYBLUE)

        for i in range(self.__n):
            for j in range(self.__m):
                if self.surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
                elif self.surface[i][j] == 0:
                    if (i,j) in visited_set:
                        imagine.blit(visited, (j * 20, i * 20))
                    else:
                        imagine.blit(empty, (j * 20, i * 20))

        drona = pygame.image.load("Assets/drona.png")
        imagine.blit(drona, (y * 20, x * 20))
        return imagine

