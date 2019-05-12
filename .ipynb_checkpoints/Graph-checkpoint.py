import numpy as np
from Haversine import Haversine

class Graph(object):
    
    
    def __init__(self, cities):
        self.matrix = self.createCityMatrix(cities)
        self.size = len(cities) - 1
        self.pheromone = [[1 / (self.size * self.size) for j in range(self.size)] for i in range(self.size)]
        
    def createCityMatrix(self, cities):
        # expensive to preform. N^2 operation time
        # diagonal is 0
        size = len(cities)
        cityMatrix = []
        for i in range(size - 1):
            row = []
            for j in range(size - 1):
                c1 = cities.Coordinates[i]
                c2 = cities.Coordinates[j]
                row.append(Haversine(c1, c2))
            cityMatrix.append(row)
        return cityMatrix