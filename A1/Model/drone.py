import pygame
from Model.utils import *
from Model.environment import Environment


class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = set()
        self.moves = []

    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1

        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < 19:
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def moveDSF(self, detectedMap):
        # TO DO!
        # rewrite this function in such a way that you perform an automatic
        # mapping with DFS

        pygame.time.wait(15)
        self.visited.add((self.x, self.y))
        for d in directions:
            new_x = self.x + d[0]
            new_y = self.y + d[1]
            if 0 <= new_x < detectedMap.size and 0 <= new_y < detectedMap.size:
                if detectedMap.surface[new_x][new_y] == 0:
                    if (new_x, new_y) not in self.visited:
                        self.moves.append((self.x, self.y))
                        self.moves.append(((new_x, new_y)))
                        self.visited.add((new_x, new_y))
                        break  # this break makes it go deeper
        if len(self.moves) > 0:
            new_location = self.moves.pop()
            self.x = new_location[0]
            self.y = new_location[1]
            return True, self.visited
        return False, self.visited
