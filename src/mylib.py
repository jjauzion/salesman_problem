import math

from src.city import City

def     get_distance(city_a, city_b):
    """Return the distance between 2 cities"""
    if not isinstance(city_a, City) or not isinstance(city_b, City):
        raise TypeError("Parameters must be City")
    return (math.sqrt((city_a.x - city_b.x) ** 2 + (city_a.y - city_b.y) ** 2))
