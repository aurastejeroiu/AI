from Model.constants import *


class Controller:
    def __init__(self, map, drone):
        self.map = map
        self.drone = drone

    def best_node(self, nodes):
        queue = list(nodes.keys())
        best_index = 0
        for i in range(len(queue)):
            if nodes[queue[i]] > nodes[queue[best_index]]:
                best_index = i
        result = queue[best_index]
        return result

    def path(self, parents, start_node, final_node):
        current_node = parents[final_node]
        path = [final_node]
        while current_node != start_node:
            path.append(current_node)
            current_node = parents[current_node]
        path.append(start_node)
        print(path)
        path.reverse()
        print(path)
        return path

    def searchAStar(self, mapM, droneD, initialX, initialY, finalX, finalY):
        # TO DO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        open_nodes = {(initialX, initialY): 0}
        visited = []
        parents = {}
        while len(open_nodes.keys()):
            current_node = self.best_node(open_nodes)
            current_distance = open_nodes.pop(current_node)
            visited.append(current_node)
            # print(current_node)
            if current_node[0] == finalX and current_node[1] == finalY:
                return self.path(parents, (initialX, initialY), current_node)

            for d in directions:
                x = current_node[0] + d[0]
                y = current_node[1] + d[1]
                if 0 <= x < mapM.n and 0 <= y < mapM.m:
                    if mapM.surface[x][y] == 0 and (x, y) not in visited:
                        g = current_distance + 1
                        h = abs(finalX - x) + abs(finalY - y)
                        f = g + h
                        print(x, y, f)
                        if (x, y) not in open_nodes:
                            open_nodes[(x, y)] = f
                            parents[(x, y)] = current_node
                        elif open_nodes[(x, y)] > f:
                            parents[(x, y)] = current_node

        # return self.path(parents, (finalX, finalY))

    def searchGreedy(self, mapM, droneD, initialX, initialY, finalX, finalY):
        # TO DO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        # This is a best first search
        # Basically A* with only the heuristic taken into account
        open_nodes = {(initialX, initialY): 0}
        visited = []
        parents = {}
        while len(open_nodes.keys()):
            current_node = self.best_node(open_nodes)
            current_distance = open_nodes.pop(current_node)
            visited.append(current_node)
            # print(current_node)
            if current_node[0] == finalX and current_node[1] == finalY:
                return self.path(parents, (initialX, initialY), current_node)

            for d in directions:
                x = current_node[0] + d[0]
                y = current_node[1] + d[1]
                if 0 <= x < mapM.n and 0 <= y < mapM.m:
                    if mapM.surface[x][y] == 0 and (x, y) not in visited:
                        h = abs(finalX - x) + abs(finalY - y)
                        print(x, y, h)
                        if (x, y) not in open_nodes:
                            open_nodes[(x, y)] = h
                            parents[(x, y)] = current_node
                        elif open_nodes[(x, y)] > h:
                            parents[(x, y)] = current_node

