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
        """

        Create a new class instance with a list of city to visit.
        Number of cities in the list is defined in the param package.
        Options:
        city_map="random" : cities have random coordinates
        city_map="circle" : cities are distributed around a circle.
                            The radius defined by max_x in the param package

        """
        self.city2travel = []
        if city_map == "random":
            for i in range(param.nb_of_city):
                self.city2travel.append(City(param.max_x, param.max_y))
            self.x_min = 0
            self.x_max = param.max_x
            self.y_min = 0
            self.y_max = param.max_y
        elif city_map == "circle":
            a = b = 0
            r = param.max_x
            for theta in range(0, 360, 360 // param.nb_of_city):
                x = a + r * math.cos(theta * math.pi / 180)
                y = b + r * math.sin(theta * math.pi / 180)
                new_city = City(1)
                new_city.setXY(x, y)
                self.city2travel.append(new_city)
            self.x_min = -param.max_x
            self.x_max = param.max_x
            self.y_min = -param.max_y
            self.y_max = param.max_y
        else:
            raise ValueError("Wrong city map option to initialise Optimisation")

    def     run(self, max_iter, show=None):
        """
        
        Run the optimisation loop until ...
        If show="convergence", the convergence curve will be printed at each step.
        If show="best", the best individue of the current population will be shown.

        """
        population = Population()
        population.random_population(self.city2travel, param.population_size)
        self.best_fitness = [population.best_performer.fitness]
        x_convergence = [0]
        if show:
            if show == "best":
                (x, y) = population.best_performer.get_plot_data()
                x_min = self.x_min
                x_max = self.x_max
                y_min = self.y_min
                y_max = self.y_max
            elif show == "convergence":
                (x, y) = (x_convergence, self.best_fitness)
                x_min = 0
                x_max = max_iter
                y_min = 0
                y_max = self.best_fitness[0]
            else:
                raise ValueError("Wrong option for show")
            plt.show()
            plt.axis([x_min, x_max, y_min, y_max])
            axes = plt.gca()
            line, = axes.plot(x, y, 'r-')
        for i in range(1, max_iter):
            population = population.next_generation()
            if Population.final:
                break
            self.best_fitness.append(population.best_performer.fitness)
            if show:
                x_convergence.append(i)
                if show == "best":
                    (x, y) = population.best_performer.get_plot_data()
                elif show == "convergence":
                    (x, y) = (x_convergence, self.best_fitness)
                line.set_xdata(x)
                line.set_ydata(y)
                plt.draw()
                plt.pause(1e-17)
                time.sleep(0.01)
        if show:
            plt.show()
        return population
