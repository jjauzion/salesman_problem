# -*-coding:Utf-8 -*

import random

from src.city import City
from src.individual import Individual

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
    for i in population:
        i.adjusted_fitness = (i.fitness - worse_fitness) * -1
        i.breed_proba = i.adjusted_fitness * 100 / best_fitness

def     get_parents(population):
    parent = []
    while len(parent) < 2:
        element = random.choice(population)
        if element.breed_proba >= random.randrange(100):
            parent.append(element)
    return (parent[0], parent[1])

def     next_generation(population, population_size):
    next_gen = []
    i = 0
    while i < population_size:
        father, mother = get_parents(population)
        print("father = ", father)
        print("mother = ", mother)
        next_gen.append(Individual(parent_a=mother, parent_b=father))
        i += 1
    return next_gen

nb_of_city = 10
population_size = 10
nb_iteration = 100

city2travel = []
for i in range(nb_of_city):
    city2travel.append(City(5))
population = []
for i in range(population_size):
    population.append(Individual(city_list=city2travel))
set_individual_breed_probability(population)
for i in population:
    print(i, " ; proba = ", i.breed_proba)
average_fitness = [sum(i.fitness for i in population) / population_size]
'''
average_fitness = [sum(i.fitness for i in population) / population_size]
for i in range(nb_iteration):
    population = next_generation(population, population_size)
    set_individual_breed_probability(population)
    average_fitness.append(sum(i.fitness for i in population) / population_size)
    print("Population num {}: av fitness = {}".format(i, average_fitness[i]))
'''
