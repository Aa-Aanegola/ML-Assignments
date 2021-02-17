import random 
import numpy as np
import time

POPULATION_SIZE = 10
MUTATION_PROBABILITY = 0.02

GENES = ''' qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!,.?'''

TARGET = "I have a bad feeling about this..."

def gen_chromosome():
    ret = ""
    for i in range(len(TARGET)):
        ret += random.choice(GENES)
    return ret

# Class to store each individual with their chromosome
class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.ret_fitness(TARGET)
        
    # Calculate the fitness of the individual (lexicographic distance)
    def ret_fitness(self, target):
        fitness = 0
        for (c1, c2) in zip(self.chromosome, target):
            if c1 != c2:
                fitness += 1
        return fitness

    # Mutate to change some genes
    def mutate(self):
        new = ""
        for i in self.chromosome:
            if random.uniform(0, 1) < MUTATION_PROBABILITY:
                new += random.choice(GENES)
            else:
                new += i
        self.chromosome = new
        self.fitness = self.ret_fitness(TARGET)
        
# Create offspring, returns tuple of 2 offspring
def mate(indi1, indi2):
    child1 = ""
    child2 = ""
    for gene1, gene2 in zip(indi1.chromosome, indi2.chromosome):
        if random.uniform(0, 1) < 0.5:
            child1 += gene1
            child2 += gene2
        else:
            child1 += gene2
            child2 += gene1
    
    return (Individual(child1), Individual(child2))


# Create initial population
found = False
population = []
gen = 0

for i in range(POPULATION_SIZE):
    population.append(Individual(gen_chromosome()))


while found == False:
    # sort the population 
    population = sorted(population, key= lambda indi: indi.fitness)
    
    print(f"Generation: {gen}\t Chromosome: {population[0].chromosome}\t Fitness: {population[0].fitness}")
    
    if population[0].fitness == 0:
        found = True
        break

    next_gen = []

    # Take the top 40% of the current generation
    selected = int(0.1*POPULATION_SIZE)
    next_gen.extend(population[:selected])
    
    for i in range(POPULATION_SIZE - selected):
        p1 = random.choice(population[:POPULATION_SIZE//2])
        p2 = random.choice(population[:POPULATION_SIZE//2])
        c1, c2 =  mate(p1, p2)
        if random.uniform(0, 1) < 0.5:
            next_gen.append(c1)
        else:
            next_gen.append(c2)
     
    population = next_gen
    
    gen += 1
    
    for i in population:
        i.mutate()