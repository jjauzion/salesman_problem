# -*-coding:Utf-8 -*

import random

from src.dna import Dna
from src.mylib import get_distance
import src.param as param

class       Individual():
    """Class Individual

    An Individual is a solution to the salesman problem
    Attribute:
     - dna : Its DNA is the route that go through all the city
     - size : Number of city on the route

    """

    count = 0

    def     __init__(self, city_list=None, father=None, mother=None):
        """Constructor of Individual class
        
        An new Individual can be made either from 2 parents or from a city list

        """
        if city_list:
            random.shuffle(city_list)
            self.dna = Dna(city_list)
            self.father_id = -1
            self.mother_id = -1
        elif father and mother:
            self.father_id = father.id
            self.mother_id = mother.id
            self.dna = self.breed(father, mother)
        else:
            raise ValueError(
                    "Error in Indivdual creation: missing parents or city list")
        self.size = self.dna.size
        self.id = Individual.count
        Individual.count += 1
        self.set_fitness()
        self._str = None
        self.adjusted_fitness = 0
        self.breed_proba = 0

    def     __repr__(self):
        #if not self._str:
        self._str = "id({}) ; f({})/m({}) ; fit({:.1f}) ; ".format(\
                self.id, self.father_id, self.mother_id, self.fitness)
        self._str += str(self.dna)
        return self._str

    def     __eq__(self, other):
        """Compare 2 individuals. Comparisons is based on Individual Id"""
        if not isinstance(other, Individual):
            raise TypeError("Type {} can't be compared to Individual".format(\
                    type(other)))
        return self.id == other.id

    def     mix_parents_dna(self, father, mother):
        dna = [None]*father.size
        i_start = random.randrange(father.size - 1)
        i_end = random.randrange(i_start + 2, father.size + 1)
        dna[i_start : i_end] = father.dna[i_start : i_end]
        dna = Dna(dna)
        for i in range(i_start):
            j = i
            while mother.dna[j] in dna:
                j = j + 1 if (j + 1) < mother.dna.size else 0
            dna[i] = mother.dna[j]
        for i in range(i_end, mother.dna.size):
            j = i
            while mother.dna[j] in dna:
                j = j + 1 if (j + 1) < mother.dna.size else 0
            dna[i] = mother.dna[j]
        return dna

    def     breed(self, father, mother):
        """Breed two Individuals to make a new Individual"""
        if not isinstance(father, Individual) or\
                not isinstance(mother, Individual):
            print("Parents must be instance of Individual to breed")
            return
        if father.size != mother.size:
            print("Parents must have the same DNA length to breed")
            return
        dna = self.mix_parents_dna(father, mother)
        dna.mutation()
        return dna

    def     set_fitness(self):
        """Compute the fitness of the individual. The lower, the better"""
        self.fitness = 0
        for i in range(self.size - 1):
            self.fitness += get_distance(self.dna[i], self.dna[i + 1])

    def     reset_count():
        Individual.count = 0
