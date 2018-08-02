# -*-coding:Utf-8 -*

from src.optimisation import Optimisation
import src.param as param

opti = Optimisation(city_map="circle")
population = opti.run(param.nb_of_iteration, show="convergence")
print("FINAL Population:\n{}".format(population))
for individual in population:
    print(individual)
