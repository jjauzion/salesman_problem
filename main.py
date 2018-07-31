# -*-coding:Utf-8 -*

import random

from src.city import City
from src.individual import Individual
import src.param as param

def     normalize_fitness(population):
    worse_fitness = population[0].fitness
    best_fitness = population[0].fitness
    for i in population:
        if i.fitness < best_fitness:
            best_fitness = i.fitness
        elif i.fitness > worse_fitness:
            worse_fitness = i.fitness


def     set_individual_breed_probability(population):
    worse_fitness = population[0].fitness
    best_fitness = population[0].fitness
    for i in population:
        if i.fitness < best_fitness:
            best_fitness = i.fitness
        elif i.fitness > worse_fitness:
            worse_fitness = i.fitness
    best_fitness = (best_fitness - worse_fitness) * -1
    if best_fitness == 0:
        print("Convergence reach")
        return 1
    for i in population:
        i.adjusted_fitness = (i.fitness - worse_fitness) * -1
        i.breed_proba = i.adjusted_fitness * 100 / best_fitness
    return 0

def     get_parents(population):
    parent = []
    while len(parent) < 2:
        element = random.choice(population)
        if element.breed_proba >= random.randrange(100):
            if len(parent) >= 1 and element.id != parent[0].id:
                parent.append(element)
            elif len(parent) < 1:
                parent.append(element)
    return (parent[0], parent[1])

def     next_generation(population, population_size):
    next_gen = []
    i = 0
    while i < population_size:
        father, mother = get_parents(population)
        next_gen.append(Individual(father=father, mother=mother))
        i += 1
    return next_gen

city2travel = []
for i in range(param.nb_of_city):
    city2travel.append(City(5))
population = []
for i in range(param.population_size):
    population.append(Individual(city_list=list(city2travel)))
set_individual_breed_probability(population)
average_fitness = [sum(i.fitness for i in population) / param.population_size]
for i in range(param.nb_of_iteration):
    population = next_generation(population, param.population_size)
    if (set_individual_breed_probability(population)):
        break
    average_fitness.append(sum(i.fitness for i in population) / param.population_size)
    print("Population num {}: av fitness = {}".format(i + 1, average_fitness[i]))
    for individual in population:
        print(individual)
    input("")
