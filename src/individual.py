# -*-coding:Utf-8 -*

import random
from src.mylib import get_distance

class       Individual():
    """Class Individual

    An Individual is a solution to the salesman problem
    Attribute:
     - dna : Its DNA is the route that go through all the city
     - size : Number of city on the route

    """

    def     breed(self, parent_a, parent_b):
        """Breed two Individuals to make a new Individual"""
        if not isinstance(parent_a, Individual) or\
                not isinstance(parent_b, Individual):
            print("Parents must be instance of Individual to breed")
            return
        if parent_a.size != parent_b.size:
            print("Parents must have the same DNA length to breed")
            return
        self.dna = parent_a.dna[:parent_a.size // 2]
        self.dna += parent_b.dna[parent_a.size // 2:]

    def     set_fitness(self):
        self.fitness = 0
        for i in range(self.size - 1):
            print(get_distance(self.dna[i], self.dna[i + 1]))
            self.fitness += get_distance(self.dna[i], self.dna[i + 1])
            print(self.fitness)

    def     __init__(self, city_list=None, parent_a=None, parent_b=None):
        """Constructor of Individual class
        
        An new Individual can be made either from 2 parents or from a city list

        """
        if city_list:
            self.dna = city_list
            random.shuffle(self.dna)
        elif parent_a and parent_b:
            self.dna = self.breed(parent_a, parent_b)
        else:
            raise ValueError("Error in Indivdual creation: missing parents or city list")
        self.size = len(self.dna)
        self.set_fitness()

    def     __repr__(self):
        return "DNA : {}\nfitness = {}".format(self.dna, self.fitness)
