# -*-coding:Utf-8 -*

import random

from src.city import City
from src.individual import Individual
import src.param as param

class       Population():
    """Class population is a set of Individual"""

    count = 0
    convergence = 0

    def     __init__(self, city2travel=None, population_size=None):
        """Constructor of Population. Requires list of cities and pop size"""
        self.list = []
        self.size = 0
        self.generation = Population.count
        Population.count += 1

    def     __getitem__(self, index):
        return self.list[index]

    def     __setitem__(self, index, value):
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, Individual):
                   raise TypeError("value contains {} item and should only\
                           contains Individual elements".format(type(value)))
        elif not isinstance(value, Individual):
           raise TypeError("value is {} and should be a Individual element"\
                   .format(type(value)))
        self.list[index] = value

    def     __add__(self, new):
        """Add a new individual to the population"""
        if not isinstance(new, Individual):
           raise TypeError("Type {} can't be added to the population,\
                   must be an Individual".format(type(new)))
        self.list.append(new)
        self.size += 1
        return self

    def     __iter__(self):
        for i in self.list:
            yield i

    def     __repr__(self):
        return "Generation {}: av fitness = {:.1f} ; best fitness = {:.1f} ; nb individual = {}"\
                .format(self.generation, self.av_fitness, self.best_performer.fitness, self.size)

    def     random_population(self, city2travel, population_size):
        """Generate a random population"""
        self.size = population_size
        for i in range(self.size):
            self.list.append(Individual(city_list=city2travel))
        self.compute_stats()
        self.compute_breed_probability()

    def     compute_stats(self):
        """Compute statistics of the population:

        self.worse_performer : worse individual performer
        self.best_performer : best individual performer
        self.av_fitness : average fitness of the entire population

        """
        self.worse_performer = self.list[0]
        self.best_performer = self.list[0]
        self.av_fitness = 0
        for i in self.list:
            self.av_fitness += i.fitness
            if i.fitness < self.best_performer.fitness:
                self.best_performer = i
            elif i.fitness > self.worse_performer.fitness:
                self.worse_performer = i
        self.av_fitness = self.av_fitness / self.size

    def     compute_breed_probability(self):
        """Compute the breed probability of every individual.

        The probability is higher for individual with high performance
        
        """
        self.best_performer.adjusted_fitness = (self.best_performer.fitness -\
                self.worse_performer.fitness) * -1
        if self.best_performer.adjusted_fitness == 0:
            Population.convergence = 1
        for i in self.list:
            i.adjusted_fitness =\
                    (i.fitness - self.worse_performer.fitness) * -1
            if Population.convergence:
                i.breed_proba = 100
            else:
                i.breed_proba =\
                        i.adjusted_fitness * 100 / self.best_performer.fitness

    def     pick_parents(self):
        """Pick randomly two parents from the indivduals pool.
        
        Indivdual with high breed propability have higher chances to be picked.
        Return a tuple of two Individuals.

        """
        parent = []
        while len(parent) < 2:
            element = random.choice(self.list)
            if element.breed_proba >= random.randrange(101):
                if len(parent) >= 1 and element != parent[0]:
                    parent.append(element)
                elif len(parent) < 1:
                    parent.append(element)
        return (parent[0], parent[1])

    def     next_generation(self):
        """Generate the next generation based on the current population

        The next generation's individuals are sons of the current population.
        The function return a new instance of a Population class.

        """
        next_gen = Population()
        i = 0
        while i < self.size:
            father, mother = self.pick_parents()
            next_gen = next_gen + Individual(father=father, mother=mother)
            i += 1
        next_gen.compute_stats()
        next_gen.compute_breed_probability()
        return next_gen
