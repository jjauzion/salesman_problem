import random

import src.param as param
from src.city import City

class       Dna():
    """Class DNA is made of an ordered list of City"""

    def     __init__(self, city_list):
        """Constructor of Dna class. A new Dna is made of a city list"""
        self.sequence = list(city_list)
        self.size = len(self.sequence)

    def     __repr__(self):
        str = "DNA = ["
        for city in self.sequence:
            if city:
                str += " {}".format(city.id)
            else:
                str += " None"
        str += "]"
        return str

    def     __iter__(self):
        for allele in self.sequence:
            yield allele

    def     __getitem__(self, index):
        return self.sequence[index]
    
    def     __setitem__(self, index, value):
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, City):
                   raise TypeError("value contains {} item and should\
                           only contains City elements".format(type(value)))
        elif not isinstance(value, City):
           raise TypeError("value is {} and should be a City element"\
                   .format(type(value)))
        self.sequence[index] = value

    def     mutation(self):
        if random.randrange(101) <= param.mutation_probability:
            i1, i2 = random.sample(range(self.size), 2)
            self.sequence[i1], self.sequence[i2] =\
                    self.sequence[i2], self.sequence[i1]
