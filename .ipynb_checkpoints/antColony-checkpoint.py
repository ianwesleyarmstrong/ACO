from haversine import haversine
import numpy as np
import pandas as pd

class antColony:


    #constructor
    def __init__(self, cities, alpha = 1, beta = 5, decay = 0.1, iterations=100, antNumber = 10):
        """
        arguments:
            alpha: pheremone importance
            beta: distance importance
            decay: how much the pheremone path will "evaporate"
            iterations: # of times the algorithm will run
            antNumber: # of ants searching per iteration
            cities: Pandas dataframe containing city names and latitude/longitude coordinates
        """
        self.alpha = alpha
        self.beta = beta
        self.decay = decay
        self.iterations = iterations
        self.antNumber = antNumber
        self.cities = cities
        self.cityMatrix = self.createCityMatrix()
        self.pheremones = np.ones(self.cityMatrix.shape) / len(self.cityMatrix)
        self.visibility = 1/self.cityMatrix
        self.visibility[self.visibility==np.inf] = 0

    def findShortestPath(self):
        self.path = None
        
        for i in range(self.iterations):
            self.alpha = 1
    
    
    def pickCity(self):
        self.alpha = 3
        
    def createCityMatrix(self):
        # expensive to preform. N^2 operation time
        # diaganol is 0
        size = self.cities.shape[0]
        cityMatrix = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                c1 = self.cities.Coordinates[i]
                c2 = self.cities.Coordinates[j]
                cityMatrix[i,j] = haversine(c1, c2)
                cityMatrix[j,1] = cityMatrix[i,j]
        return cityMatrix


