import random


class Ant:
    def __init__(self, starting_sensor, energy=32):
        self.path = []
        self.energy_given = []  # how much energy for each sensor
        self.visited_sensors = [starting_sensor]
        self.energy = energy

    def choose_sensor(self, map, distances_between_sensors, pheromone_level, sensors_visibility, alpha=0.8, beta=1.5):

        last_sensor = self.visited_sensors[-1]
        # print(last_sensor)
        possible_sensors = []
        # print(distances_between_sensors)
        for sensor_tuple in distances_between_sensors:
            if distances_between_sensors[sensor_tuple].Length <= self.energy:
                if sensor_tuple[0] == last_sensor and sensor_tuple[1] not in self.visited_sensors:
                    possible_sensors.append([sensor_tuple[1], distances_between_sensors[sensor_tuple]])
                if sensor_tuple[1] == last_sensor and sensor_tuple[0] not in self.visited_sensors:
                    possible_sensors.append([sensor_tuple[0], distances_between_sensors[sensor_tuple]])

        # print(possible_sensors)

        desirability = []
        for s in possible_sensors:
            key = (s[0], last_sensor)
            if key not in pheromone_level.keys():
                key = (last_sensor, s[0])
            distance = s[1].Length
            if pheromone_level[key] != 0:
                desirability.append((1 / distance ** beta) * (pheromone_level[key] ** alpha))
            else:
                desirability.append((1 / distance ** beta))

        # roulette
        s = sum(desirability)
        # print(desirability)
        if s == 0:
            return "No more sensors"
        p = [desirability[i] / s for i in range(len(desirability))]
        p = [sum(p[0:i + 1]) for i in range(len(p))]
        r = random.random()
        i = 0
        while r > p[i]:
            i = i + 1
        the_chosen_one = possible_sensors[i][0]
        # print(the_chosen_one)

        # while the_chosen_one in self.visited_sensors:
        #     the_chosen_one = random.choice(map.sensors)

        self.visited_sensors.append(the_chosen_one)

        # if len(self.visited_sensors) == 1:
        # # aici alegem cat lasam
        # lasam = random.randint(0, 5)
        # if lasam > self.energy_left:
        #     lasam = random.randint(0, 5)
        #
        # self.energy_left -= lasam
        # seen = 0
        # for i in range(lasam):
        #     seen += sensors_visibility[the_chosen_one][i]
        #

        key = (the_chosen_one, last_sensor)
        if key not in pheromone_level:
            key = (last_sensor, the_chosen_one)

        # pheromone_level[key] += (1 + energy_left_to_sensor)
        pheromone_level[key] += 1
        self.energy -= distances_between_sensors[key].Length
        # print(self.energy)

        # print(self.visited_sensors)
        return the_chosen_one


class Population:
    def __init__(self, size=5):
        self.ants = [Ant() for _ in range(size)]
        self.size = size


class Path:
    def __init__(self, path):
        self.path = path
        self.length = len(path)
        self.pheromone_level = []

    @property
    def Length(self):
        return self.length
