# -*-coding:Utf-8 -*

import random

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
    mutation_proba = param.mutation_probability

    def     mutation(self):
        if random.randrange(101) <= Individual.mutation_proba:
            i1, i2 = random.sample(range(self.size), 2)
            self.dna[i1], self.dna[i2] = self.dna[i2], self.dna[i1]
            print("Mutation !!")

    def     get_mom_dna(self, mother, father_index, father_length):
        """Mix current self DNA with mother DNA"""
        print("mother dna : ", mother.dna)
        for i in range(father_index):
            j = i
            print("i:{} ; self.dna[i]:{}".format(i, self.dna[i]))
            print("j:{} ; mother.dna[j]:{}".format(j, mother.dna[j]))
            while self.dna[i] and mother.dna[j].id == self.dna[i].id:
                j += 1
                if j >= mother.size:
                    j = 0
                print("j:{} ; mother.dna[j]:{}".format(j, mother.dna[j]))
            self.dna[i] = mother.dna[j]
        print("self dna : ", self.dna)
        for i in range(father_index + father_length, mother.size):
            j = i
            print("i:{} ; self.dna[i]:{}".format(i, self.dna[i]))
            print("j:{} ; mother.dna[j]:{}".format(j, mother.dna[j]))
            while self.dna[i] and mother.dna[j].id == self.dna[i].id:
                j += 1
                if j >= mother.size:
                    j = 0
            self.dna[i] = mother.dna[j]

    def     breed(self, father, mother):
        """Breed two Individuals to make a new Individual"""
        if not isinstance(father, Individual) or\
                not isinstance(mother, Individual):
            print("Parents must be instance of Individual to breed")
            return
        if father.size != mother.size:
            print("Parents must have the same DNA length to breed")
            return
        self.dna = [None]*father.size
        index = random.randrange(father.size)
        length = random.randrange(father.size - index + 1)
        print("index: {} ; range: {} ; length = {}".format(index, father.size - index + 1, length))
        self.dna[index : index + length] =\
                father.dna[index : index + length]
        print("av : ", self.dna)
        self.get_mom_dna(mother, index, length)
        print("ap : ", self.dna)
        self.mutation()

    def     set_fitness(self):
        """Compute the fitness of the individual. The lower, the better"""
        self.fitness = 0
        for i in range(self.size - 1):
            self.fitness += get_distance(self.dna[i], self.dna[i + 1])

    def     reset_count():
        Individual.count = 0

    def     __init__(self, city_list=None, father=None, mother=None):
        """Constructor of Individual class
        
        An new Individual can be made either from 2 parents or from a city list

        """
        if city_list:
            self.dna = city_list
            random.shuffle(self.dna)
            self.father_id = -1
            self.mother_id = -1
            self.size = len(self.dna)
        elif father and mother:
            self.father_id = father.id
            self.mother_id = mother.id
            self.size = len(father.dna)
            self.breed(father, mother)
        else:
            raise ValueError(
                    "Error in Indivdual creation: missing parents or city list")
        self.id = Individual.count
        Individual.count += 1
        self.set_fitness()
        self._str = None
        self.adjusted_fitness = 0
        self.breed_proba = 0

    def     __repr__(self):
        #if not self._str:
        self._str = "id({}) ; f({})/m({}) ; fit({:.1f}) ;".format(\
                self.id, self.father_id, self.mother_id, self.fitness)
        self._str += "DNA: ["
        for i in range(self.size):
            self._str += " {}".format(self.dna[i].id)
            #self._str += "\nfitness: {}".format(self.fitness)
            #self._str += "\nbreed proba: {}".format(self.breed_proba)
        self._str += "]"
        return self._str
