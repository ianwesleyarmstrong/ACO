from Haversine import Haversine
from Graph import Graph
from Ant import Ant
import numpy as np
import pandas as pd
import time


class AntColony(object):


    #constructor
    def __init__(self, graph, alpha = 1, beta = 10,q = 1, decay = 0.5, iterations=100, antNumber = 10):
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
        self.graph = graph
        
        

    def findShortestPath(self, graph):
        start = time.time()
        
        
        bestCost = float('inf')
        bestPath = []
        for iter in range(self.iterations):
            #print(iter)
            # create ants
            ants = [Ant(self, graph, self.alpha, self.beta, self.decay) for _ in range(self.antNumber)]
            for ant in ants:
                for i in range(graph.size):
                    ant.pickNext()
                ant.totalCost += graph.matrix[ant.route[-1]][ant.route[0]]
                #check for best cost
                if ant.totalCost < bestCost:
                    bestCost = ant.totalCost
                    bestPath = [] + ant.route
                #update ant pheromones
                ant.updatePheromoneChange()
            self.updatePheromoneMatrix(graph, ants)
        stop = time.time()
        totalTime = stop - start
        return bestPath, bestCost, totalTime
            
        
    def updatePheromoneMatrix(self, graph, ants):
        for i, row in enumerate(graph.pheromone):
            for j, col in enumerate(row):
                graph.pheromone[i][j] *= self.decay
                # update based on ant delta
                for ant in ants:    
                    graph.pheromone[i][j] += ant.pheromoneChange[i][j]
        
        
        
    


