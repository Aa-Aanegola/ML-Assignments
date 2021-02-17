import random
import numpy as np
from Local_Data.client import *

ID = "n3eEadyA2H45SSH97P9JCgWFqajNk8pvx086l1tVwFCEs9sPkT"

weight_file = open("overfit.txt", "r")
weights = weight_file.read()
weights = weights.replace('[', '')
weights = weights.replace(']', '')
weights = weights.replace(' ', '')
weights = weights.replace('\n', '')
weights = weights.split(',')
for i in range(len(weights)):
    weights[i] = float(weights[i])

overfit = np.array(weights)

POPULATION_SIZE = 10
MUTATION_PROBABILITY = 0.05
ELITE_PERCENTAGE = 0.2
BREED_PERCENTAGE = 0.6
generations = 9

def gen_chromosome():
    return np.random.uniform(low=-1e-13, high=1e-13, size=(11, ))

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None

        
    # Calculate the fitness of the individual (lexicographic distance)
    def set_fitness(self):
        #self.fitness = [np.random.uniform(1, 100), np.random.uniform(1, 100)]
        self.fitness = get_errors(ID, self.chromosome)

        
    # Mutate to change some genes
    def mutate(self):
        new = []
        for i in self.chromosome:
            if random.uniform(0, 1) < MUTATION_PROBABILITY:
                new.append(i+np.random.uniform(-1e-14, 1e-14))
            else:
                new.append(i)
        self.chromosome = new
        
        
# Create offspring, returns tuple of 2 offspring
def mate(indi1, indi2):
    child1 = []
    for gene1, gene2 in zip(indi1.chromosome, indi2.chromosome):
        if random.uniform(0, 1) < 0.5:
            child1.append(gene1)
        else:
            child1.append(gene2)
    
    return Individual(child1)

population = []

for i in range(1):
    population.append(Individual(gen_chromosome()))

for i in range(generations):
    print(f"Generation: {i}")
    
    for indi in population:
        indi.mutate()
        indi.set_fitness()
    
    population = sorted(population, key= lambda indi: (indi.fitness[1], indi.fitness[0]))
    
    for indi in population:
        print(indi.fitness)
    
    next_gen = []
    
    next_gen.extend(population[:int(ELITE_PERCENTAGE*POPULATION_SIZE)])
    
    for i in range(POPULATION_SIZE - int(ELITE_PERCENTAGE*POPULATION_SIZE)):
        p1 = random.choice(population[:int(BREED_PERCENTAGE*POPULATION_SIZE)])
        p2 = random.choice(population[:int(BREED_PERCENTAGE*POPULATION_SIZE)])
        child = mate(p1, p2)
        next_gen.append(child)
    
    population = next_gen
    
# dump = []
# for indi in population:
#     indi.set_fitness()
#     dump.append((indi.chromosome, indi.fitness))

# print(dump)

# with open ('dump.txt', 'w') as write_file:
#     json.dump(dump , write_file, indent=2)