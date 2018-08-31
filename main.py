# -*-coding:Utf-8 -*

from src.optimisation import Optimisation
import src.param as param
import sys
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-b", "--best", action="store_true",\
        help="Defaut option. Print the best individual of the current population")
group.add_argument("-c", "--convergence", action="store_true", help="Print the convergence curve")
option = parser.parse_args()
if option.convergence:
    show_option = "convergence"
else:
    show_option = "best"
opti = Optimisation(city_map="random")
population = opti.run(param.nb_of_iteration, show=show_option)
print("FINAL Population:\n{}".format(population))
for individual in population:
    print(individual)
