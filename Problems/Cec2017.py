import random
import numpy as np

class Cec2017():

    def __init__(self):
        self.information = {}

    def generate_information(self, function, low, high, dimention, alpha = 1):
        self.information = {
            "low" : low,
            "hight": high,
            "dimention": dimention,
            "function": function,
            "alpha": alpha
        }

    def energy(self, solution, information):
        return - self.information["function"]([solution])[0]

    def generate_initial_solution(self, information):
        solution = np.random.uniform(low=self.information["low"],
                                     high=self.information["hight"],
                                     size=self.information["dimention"]).tolist()

        return solution

    def random_neighbour(self, solution):
        neighbour = solution[:]
        index = random.randint(0, len(solution) - 1)
        alpha = random.uniform(-self.information["alpha"], self.information["alpha"])

        neighbour[index] += alpha
        return neighbour