# -*-coding:Utf-8 -*

import random
import matplotlib.pyplot as plt
import time
import math

from src.city import City
from src.individual import Individual
from src.population import Population
import src.param as param

city2travel = []
a = b = 0
r = param.max_x
for theta in range(0, 360, 360 // param.nb_of_city):
    x = a + r * math.cos(theta * math.pi / 180)
    y = b + r * math.sin(theta * math.pi / 180)
    new_city = City(1)
    new_city.setXY(x, y)
    city2travel.append(new_city)
#for i in range(param.nb_of_city):
#    city2travel.append(City(param.max_x, param.max_y))
population = Population()
population.random_population(city2travel, param.population_size)
(x, y) = population.best_performer.plot_route()
plt.show()
axes = plt.gca()
line, = axes.plot(x, y, 'r-')
for i in range(param.nb_of_iteration):
    #print(population)
    (x, y) = population.best_performer.plot_route()
    line.set_xdata(x)
    line.set_ydata(y)
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.01)
    population.best_performer.plot_route()
    population = population.next_generation()
    if Population.convergence:
        break
plt.show()
print("FINAL Population:\n{}".format(population))
for individual in population:
    print(individual)
