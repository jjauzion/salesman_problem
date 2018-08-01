import math

from src.city import City

def     get_distance(city_a, city_b):
    """Return the distance between 2 cities"""
    if not isinstance(city_a, City) or not isinstance(city_b, City):
        raise TypeError("City a is {} and city b is {}. Both must be City."\
                .format(type(city_a), type(city_b)))
    return (math.sqrt((city_a.x - city_b.x) ** 2 + (city_a.y - city_b.y) ** 2))
