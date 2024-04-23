from random import *
import pygame
import sys
from pygame.locals import *
from Model.dmap import DMap
from Model.drone import Drone
from Model.environment import Environment
from Model.utils import *


# define a main function
def play(e, size=20):
    # print(str(e))

    # we create the map
    m = DMap(size)

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("Assets/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("drone exploration")

    # we position the drone somewhere in the area
    x = randint(0, size - 1)
    y = randint(0, size - 1)
    # while e.surface[x][y] != 0:
    #     print(x, y, m.surface[x][y])
    #     x = randint(0, 19)
    #     y = randint(0, 19)

    # cream drona
    d = Drone(x, y)

    # create a surface on screen that has the size of 800 x 480
    screen = pygame.display.set_mode((40 * size, 20 * size))
    screen.fill(WHITE)
    screen.blit(e.image(), (0, 0))

    # define a variable to control the main loop
    running = True

    # main loop
    visited = set()
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == KEYDOWN:
                # use this function instead of move
                # d.move(m)
                pass
        # d.moveDSF(m)
        m.markDetectedWalls(e, d.x, d.y)
        screen.blit(m.image(d.x, d.y, visited), (20 * size, 0))
        pygame.display.flip()
        running, visited = d.moveDSF(m)

    pygame.time.wait(2000)
    pygame.quit()


def ui():
    while True:
        print("0. Exit")
        print("1. Use default map.")
        print("2. Create random map.")
        print("3. Load a map")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            # we create the environment
            e = Environment()
            e.loadEnvironment("Assets/test2.map")
            play(e)
        elif choice == "2":
            while True:
                try:
                    size = int(input("size > "))
                    fill = float(input("fill > "))
                    e = Environment(size)
                    e.randomMap(fill)
                    play(e, size)
                    save = input("Save this map? (y/n) ")
                    if save == "y":
                        name = input("Map name: ")
                        e.saveEnvironment("Assets/" + name + ".map")
                    break
                except ValueError as e:
                    print(e)
                    pass
        elif choice == "3":
            e = Environment()
            map_name = input("Map name > ")
            e.loadEnvironment("Assets/" + map_name + ".map")
            play(e, e.size)
