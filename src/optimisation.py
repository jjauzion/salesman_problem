# -*-coding:Utf-8 -*

import random
import matplotlib.pyplot as plt
import time
import math

from src.city import City
from src.individual import Individual
from src.population import Population
import src.param as param

class       Optimisation():
    """Class Optimisation run the genetic algorithm to solve the TSP"""

    def     __init__(self, city_map="random"):
        self.city2travel = []
        if city_map == "random":
            for i in range(param.nb_of_city):
                self.city2travel.append(City(param.max_x, param.max_y))
        elif city_map == "circle":
            a = b = 0
            r = param.max_x
            for theta in range(0, 360, 360 // param.nb_of_city):
                x = a + r * math.cos(theta * math.pi / 180)
                y = b + r * math.sin(theta * math.pi / 180)
                new_city = City(1)
                new_city.setXY(x, y)
                self.city2travel.append(new_city)
        else:
            raise ValueError("Wrong city map option to initialise Optimisation")

    def     run(self, max_iter, show=None):
        population = Population()
        population.random_population(self.city2travel, param.population_size)
        self.best_fitness = [population.best_performer.fitness]
        gen = [0]
        if show:
            if show == "best":
                (x, y) = population.best_performer.get_plot_data()
            elif show == "convergence":
                (x, y) = (gen, self.best_fitness)
            else:
                raise ValueError("Wrong option for show")
            plt.show()
            plt.axis([0, max_iter, 0, self.best_fitness[0]])
            axes = plt.gca()
            line, = axes.plot(x, y, 'r-')
        for i in range(1, max_iter):
            population = population.next_generation()
            if Population.final:
                break
            self.best_fitness.append(population.best_performer.fitness)
            if show:
                gen.append(i)
                if show == "best":
                    (x, y) = population.best_performer.get_plot_data()
                elif show == "convergence":
                    (x, y) = (gen, self.best_fitness)
                    print("x: ", x[i])
                    print("y: ", y[i])
                line.set_xdata(x)
                line.set_ydata(y)
                plt.draw()
                plt.pause(1e-17)
                time.sleep(0.01)
        if show:
            plt.show()
        return population
