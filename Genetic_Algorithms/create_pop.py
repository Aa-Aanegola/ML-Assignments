import random
import numpy as np
from client import *
import json
import requests
import copy 

ID = "n3eEadyA2H45SSH97P9JCgWFqajNk8pvx086l1tVwFCEs9sPkT"
MUTATION_PROBABILITY = 0.2
WEIGHT = 0.6

scale = [0, 1e-12, 1e-13, 1e-11, 1e-10, 1e-15, 1e-15, 1e-5, 1e-6, 1e-8, 1e-10]

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None
        
    def set_fitness(self):
        errors = get_errors(ID, self.chromosome)
        self.fitness = WEIGHT * errors[1] + (1-WEIGHT)*errors[0]
        
    # Mutate to change some genes
    def mutate(self):
        new = []
        
        for i in range(11):
            if random.uniform(0, 1) < MUTATION_PROBABILITY:
                new.append(self.chromosome[i] + np.random.uniform(-0.1, 0.1)*scale[i])
            else:
                new.append(self.chromosome[i])
            if new[-1] > 10:
                new[-1] = 10
            if new[-1] < -10:
                new[-1] = -10
        self.chromosome = new


first = Individual(
    [0.0,
      -6.842201948293549e-13,
      -2.3590251021127836e-13,
      3.542816885594752e-11,
      -2.614856688324118e-10,
      -2.1326364830887294e-15,
      9.869990154318963e-16,
      3.491097688584864e-05,
      -2.30650418524083e-06,
      -1.59792834e-08,
      9.98214034e-10
    ])

first.fitness = 342074070573.2653

population = []
population.append(first)

optimal = copy.deepcopy(first)

for i in range(489):
    temp = copy.deepcopy(optimal)
    temp.mutate()
    cur_fit = temp.fitness 
    temp.set_fitness()
    
    if len(population) < 10:
        population.append(copy.deepcopy(temp))
    elif temp.fitness < population[-1].fitness:
        population[-1] = copy.deepcopy(temp)
    
    for i in population:
        print(i.chromosome, i.fitness)
    
    population = sorted(population, key= lambda indi: indi.fitness)


dump = []
for indi in population:
    dump.append((indi.chromosome, indi.fitness))

# print(dump)

with open ('dump.txt', 'w') as write_file:
    json.dump(dump , write_file, indent=2)