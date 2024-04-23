from controller import *
import pygame
import time

n = 20
m = 20
map = Map(n, m)
pygame.init()
screen = pygame.display.set_mode((20 * n, 20 * m))
screen.fill(WHITE)
screen.blit(map.image(), (0, 0))
pygame.display.flip()
# map.randomMap()
map.loadMap("default3.map")
# map.loadMap("default50-50-20.map")
# sensors = [(1, 2), (15, 4), (5, 15), (10, 10), (19, 18)]

# sensors = []
# for i in range(7):
#     x = random.randint(0, n-1)
#     y = random.randint(0, m-1)
#     sensors.append((x, y))
# map.Sensors = sensors
# map.saveMap("default3.map")

# # map.saveMap("40pe40.map")
# map.saveMap("default50-50-20.map")
c = Controller(screen, map)
print(c.compute_sensors())

# res = c.searchAStar(map, 1, 2, 15, 4, screen)

# paths = c.compute_minimum_distance_between_sensors()
# print(paths)
# minim = numpy.inf
# for _ in range(7):
#     ant_path = c.compute_one_ant()
#     res = []
#     for i in range(len(ant_path)-1):
#         key = (ant_path[i], ant_path[i+1])
#         if key not in paths:
#             key = (ant_path[i+1], ant_path[i])
#             res.extend(paths[key].path[::-1])
#         else:
#             res.extend(paths[key].path)
#     length = len(res)
#     # print(length)
#     if minim > length:
#         print(ant_path)
#         minim = length
#         simply_the_best = res

simply_the_best = c.run()
# map.saveMap("default50-50-20.map")
# print(simply_the_best)
screen.blit(map.image_path([]), (0, 0))
pygame.display.flip()
time.sleep(5)
for i in range(len(simply_the_best)):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.time.delay(25)
    sal = simply_the_best[:i]
    screen.blit(map.image_path(sal), (0, 0))
    pygame.display.flip()
    pygame.display.update()
time.sleep(20)

# print(res)

# print(map.surface)


