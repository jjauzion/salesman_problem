# -*-coding:Utf-8 -*

import random

from src.city import City
from src.individual import Individual
from src.population import Population
import src.param as param

city2travel = []
for i in range(param.nb_of_city):
    city2travel.append(City(param.max_x, param.max_y))
population = Population()
population.random_population(city2travel, param.population_size)
for i in range(param.nb_of_iteration):
    print(population)
    population = population.next_generation()
    if Population.convergence:
        break
print("FINAL Population:\n{}".format(population))
for individual in population:
    print(individual)
