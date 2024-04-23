

# import the pygame module, so you can use it
import pickle
import pygame
import time
from pygame.locals import *
from random import random, randint
import numpy as np
from Model.drone import Drone
from Model.map import Map
from Model.constants import *
from Controller.controller import Controller


def dummysearch():
    # example of some path in test1.map from [5,7] to [7,11]
    return [[5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [6, 11], [7, 11]]


def displayWithPath(image, path):
    mark = pygame.Surface((20, 20))
    mark.fill(GREEN)
    for move in path:
        image.blit(mark, (move[1] * 20, move[0] * 20))

    return image


# define a main function
def play(option=None):

    # we create the map
    m = Map()
    # m.randomMap()
    # m.saveMap("test2.map")
    # m.loadMap("Assets/test1.map")
    m.randomMap(0)

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("Assets/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Path in simple environment")

    # we position the drone somewhere in the area
    x = randint(0, 19)
    y = randint(0, 19)

    # create drona
    d = Drone(x, y)

    controller = Controller(m, d)
    # create a surface on screen that has the size of 400 x 480
    screen = pygame.display.set_mode((400, 400))
    screen.fill(WHITE)

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            if event.type == KEYDOWN:
                d.move(m)  # this call will be erased

        screen.blit(d.mapWithDrone(m.image()), (0, 0))
        pygame.display.flip()

    # path = dummysearch()
    if option == "1":
        path = controller.searchAStar(m, d, 0, 0, 5, 5)
    elif option == "2":
        path = controller.searchAStar(m, d, 0, 0, 5, 5)
    print(path)
    screen.blit(displayWithPath(m.image(), path), (0, 0))

    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
