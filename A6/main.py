import random

import math
import pygame

EQUILIBRIUM = False
GREY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
WIDTH = 1000
HEIGHT = 1000

# ANIMATION_MODE = False
ANIMATION_MODE = True

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("k means clustering")
screen.fill(WHITE)
pygame.display.update()

CENTROID_RADIUS = 7


class Point:
    def __init__(self, label, x, y, color=GREY):
        self.label = label
        self.computed_label = ""
        self.x = x
        self.y = y
        self.color = color
        self.color_name = ""
        self.points = []

    def __str__(self):
        return self.label + " " + str(self.x) + " " + str(self.y)

    def add(self, point):
        self.points.append(point)

    def recenter(self):
        sum_x = sum_y = 0
        for p in self.points:
            sum_x += p.x
            sum_y += p.y

        if len(self.points):
            self.x = sum_x / len(self.points)
            self.y = sum_y / len(self.points)

        if not EQUILIBRIUM:
            self.points = []

    def compute_statistics(self, all_points):

        self.recompute_labels()

        true_positives = true_negatives = false_positive = false_negatives = 0

        for point in self.points:
            if point.label == self.label:
                true_positives += 1
            else:
                false_positive += 1
        for point in all_points:
            if point not in self.points:
                if point.computed_label != self.label:
                    if point.label != self.label:
                        true_negatives += 1
                    else:
                        false_negatives += 1
        print("true positives: ", true_positives, "; true negatives: ", true_negatives, "; false positive: ",
              false_positive, "; false negatives:", false_negatives)

        accuracy = (true_positives + true_negatives) / (
                true_positives + true_negatives + false_positive + false_negatives)
        precision = true_positives / (true_positives + false_positive)

        # if true_positives + false_negatives == 0:
        #     rappel = math.inf
        # else:

        rappel = true_positives / (true_positives + false_negatives)

        # if precision + rappel == 0:
        #     score = math.inf
        # else:

        score = 2 * precision * rappel / (precision + rappel)

        return accuracy, precision, rappel, score

    def recompute_labels(self):
        labels = {}
        maximum = -math.inf
        dominant_label = ""
        for p in self.points:
            if p.label in labels:
                labels[p.label] += 1
            else:
                labels[p.label] = 1
            if maximum < labels[p.label]:
                maximum = labels[p.label]
                dominant_label = p.label

        for p in self.points:
            p.computed_label = dominant_label
        self.label = dominant_label


def drawCircle(point, radius=3, color=None):
    pos = (point.x * 50 + 500, point.y * -50 + 500)
    if color is None:
        color = point.color

    # border for centroids
    if radius != 3:
        pygame.draw.circle(screen, WHITE, pos, radius * 2)

    pygame.draw.circle(screen, color, pos, radius)
    if ANIMATION_MODE:
        pygame.display.update()


def distance(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def recenter(centroids, points):
    global EQUILIBRIUM
    for point in points:
        minim = math.inf
        closest = None
        for c in centroids:
            d = distance(point, c)
            if d < minim:
                point.color = c.color
                minim = d
                closest = c
        closest.add(point)
        # drawCircle(point)

    if EQUILIBRIUM:
        return

    for point in points:
        drawCircle(point)

    done = True
    for c in centroids:
        drawCircle(c, CENTROID_RADIUS, WHITE)
        old_x = c.x
        old_y = c.y
        c.recenter()
        if old_y != c.y or old_x != c.x:
            done = False
        drawCircle(c, CENTROID_RADIUS)

    if done:
        EQUILIBRIUM = True
        print("We have reached equilibrium")

    pygame.display.update()


def print_statistics(clusters, points):
    for c in clusters:
        # print(c.points)
        # continue
        accuracy, precision, rappel, score = c.compute_statistics(points)
        print("Label: ", c.label, "-", c.color_name)
        print("Accuracy: " + str(accuracy))
        print("Precision: " + str(precision))
        print("Rappel: " + str(rappel))
        print("Score: " + str(score))
        print("\n")


def main():
    centroids = []
    for _ in range(4):
        x = (random.random() - 0.5) * 10
        y = (random.random() - 0.5) * 10
        c = Point("A", x, y)
        centroids.append(c)

    centroids[0].color = RED
    centroids[1].color = GREEN
    centroids[2].color = BLUE
    centroids[3].color = BLACK
    centroids[0].color_name = "RED"
    centroids[1].color_name = "GREEN"
    centroids[2].color_name = "BLUE"
    centroids[3].color_name = "BLACK"
    # centroids[4].color = PURPLE

    for c in centroids:
        drawCircle(c, CENTROID_RADIUS)

    points = []
    with open("dataset.csv") as file:
        for line in file:
            tokens = line.strip("\n").split(",")
            label = tokens[0]
            if label!="label":
                x = float(tokens[1])
                y = float(tokens[2])
                entry = Point(label, x, y)
                points.append(entry)

            # print(entry)
            # minim = math.inf
            # closest = None
            # for c in centroids:
            #     d = distance(entry, c)
            #     if d < minim:
            #         entry.color = c.color
            #         minim = d
            #         closest = c
            # drawCircle(entry)

    recenter(centroids, points)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if ANIMATION_MODE:
            pygame.time.delay(1000)
        if EQUILIBRIUM:
            running = False
        recenter(centroids, points)

    print_statistics(centroids, points)

    pygame.time.delay(200000)


main()
