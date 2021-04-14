import random
import numpy as np
from client import *
import json
import requests
from tabulate import tabulate


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

scale = [0, 1e-13, 1e-13, 1e-11, 1e-10, 1e-15, 1e-16, 1e-5, 1e-6, 1e-8, 1e-9]


POPULATION_SIZE = 10
MUTATION_PROBABILITY = 0.08
ELITE_PERCENTAGE = 0.2
BREED_PERCENTAGE = 0.6
GENERATIONS = 90
WEIGHT = 0.5


fd = open('gen.txt', 'w')
fd2 = open('bef_mut.txt', 'w')

def gen_chromosome():

    chromosome = []
    if random.randint(0, 1) == 0:
        for i in range(11):
            chromosome.append(np.random.uniform(-10, 10)*scale[i])
    else:
        for i in range(11):
            x = random.uniform(10, 99)
            if random.randint(0, 1) == 0:
                x *= -1
            chromosome.append(x * scale[i])
        
    return chromosome



class Individual:
    id = 0
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.train = None
        self.val = None
        self.fitness = None
        self.id = Individual.id
        Individual.id += 1
        self.parents = (None, None)
        
    # Calculate the fitness of the individual (lexicographic distance)
    def set_fitness(self):
        errors = get_errors(ID, self.chromosome)
        self.train = errors[0]
        self.val = errors[1]
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
        
        
# Create offspring, returns tuple of 2 offspring
def mate(indi1, indi2):
    child1 = []
    for gene1, gene2 in zip(indi1.chromosome, indi2.chromosome):
        if random.uniform(0, 1) < 0.5:
            child1.append(gene1)
        else:
            child1.append(gene2)
    
    return Individual(child1)

# population = []

# population.append(Individual(overfit))
# for i in range(POPULATION_SIZE-1):
#     population.append(Individual(gen_chromosome()))


population = []

with open('dump.txt', 'r') as read_file:
    temp = json.load(read_file)
    for indi in temp:
        population.append(Individual(indi[0]))
        population[-1].fitness = indi[1]    
    read_file.close()

while len(population) > POPULATION_SIZE:
    population.pop(-1)


while len(population) != POPULATION_SIZE:
    population.append(Individual(gen_chromosome()))
    population[-1].set_fitness()


for i in range(GENERATIONS):
    
    print(f"Generation: {i}")
    
    
    population = sorted(population, key= lambda indi: indi.fitness)

    table = []
    headers = None    
    for indi in population:
        print(indi.fitness, indi.train, indi.val)
        dic = indi.__dict__
        headers = list(dic.keys())
        table.append(list(dic.values()))
    
    fd.write(f"\n\nGeneration: {i}\n\n")
    fd.write(tabulate(table, headers=headers, tablefmt="github"))
     
    next_gen = []
    
    next_gen.extend(population[:int(ELITE_PERCENTAGE*POPULATION_SIZE)])
    
    for x in range(POPULATION_SIZE - int(ELITE_PERCENTAGE*POPULATION_SIZE)):
        p1 = random.choice(population[:int(BREED_PERCENTAGE*POPULATION_SIZE)])
        p2 = random.choice(population[:int(BREED_PERCENTAGE*POPULATION_SIZE)])
        child = mate(p1, p2)
        child.parents = (p1.id, p2.id)
        next_gen.append(child)
    
    population = next_gen

    table = []
    headers = None
    for indi in population:
        dic = indi.__dict__
        dic.pop("fitness")
        dic.pop("val")
        dic.pop("train")
        headers = list(dic.keys())
        table.append(list(dic.values()))
    
    j = i+1
    fd2.write(f"\n\nGeneration: {j}\n\n")
    fd2.write(tabulate(table, headers=headers, tablefmt="github"))

    for indi in population:
        indi.mutate()
        indi.set_fitness()
    

population = sorted(population, key= lambda indi: indi.fitness)    
for i in range(len(population)):
        population[i].id = i
table = []
headers = None
for indi in population:
    print(indi.fitness, indi.train, indi.val)
    dic = indi.__dict__
    headers = list(dic.keys())
    table.append(list(dic.values()))

fd.write(f"Generation: 100\n")
fd.write(tabulate(table, headers=headers, tablefmt="github"))
    
fd.close()
fd2.close()

dump = []
for indi in population:
    dump.append((indi.chromosome, indi.fitness))

# print(dump)

with open ('dump.txt', 'w') as write_file:
    json.dump(dump , write_file, indent=2)