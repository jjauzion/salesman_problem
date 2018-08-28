# -*-coding:Utf-8 -*

from src.optimisation import Optimisation
import src.param as param

opti = Optimisation(city_map="random")
population = opti.run(param.nb_of_iteration, show="best")
print("FINAL Population:\n{}".format(population))
for individual in population:
    print(individual)
