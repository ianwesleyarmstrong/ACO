import numpy as np
import pandas as pd
import random
from Graph import Graph


class Ant(object):
    
    
    def __init__(self, AntColony, graph, alpha=1, beta = 10, q = 0.5):
  
        self.alpha = alpha
        self.beta = beta
        self.q = q
        self.graph = graph
        self.route = []
        self.open = [i for i in range(graph.size)]
        self.pheromoneChange = []
        start = np.random.randint(0, graph.size-1)
        #print(self.start)
        self.curr = start
        self.totalCost = 0.0
        self.visibility = [[0 if i == j else 1 / graph.matrix[i][j] for j in range(graph.size)] for i in range(graph.size)]
        self.route.append(start)
        self.open.remove(start)
        #print(self.open)
    
    def pickNext(self):
        denom = 0
        for place in self.open:
            #print('place ' + str(place))
            denom += self.graph.pheromone[self.curr][place] ** self.alpha * self.visibility[self.curr][place] ** self.beta
            probs = [0 for i in range(self.graph.size)]
            for i in range(self.graph.size):
                try:
                    self.open.index(i)
                    probs[i] = self.graph.pheromone[self.curr][i] ** self.alpha * \
                                self.visibility[self.curr][i] ** self.beta / denom
                except ValueError:
                    pass
            #select using probability roulette
            selected = self.open[0]
            rand = random.random()
            #print(rand)
            for i, prob in enumerate(probs):
                rand -= prob
                #print(rand)
                if rand <= 0:
                    selected = i
                    break
            #print(self.open)
            #print(selected)
            self.open.remove(selected)
            self.route.append(selected)
            self.totalCost += self.graph.matrix[self.curr][selected]
            self.curr = selected
            
            
            
    
    def updatePheromoneChange(self):
        self.pheromoneChange = [[0 for j in range(self.graph.size)] for i in range(self.graph.size)]
        for place in range(1, len(self.route)):
            i = self.route[place-1]
            j = self.route[place]
            self.pheromoneChange[i][j] = self.q / self.totalCost
            
                
        
    
    