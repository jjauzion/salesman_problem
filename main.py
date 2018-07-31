# -*-coding:Utf-8 -*

from src.city import City
from src.individual import Individual

city2travel = []
nb_of_city = 3
for i in range(nb_of_city):
    city2travel.append(City(5))

new = Individual(city_list=city2travel)
print(new)
