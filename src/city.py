# -*-coding:Utf-8 -*

import random

class       City():
    """Class city
    
    A city is defined by:
      -> x and y coordinates
      -> Its name
      -> Its id
    x and y are randonly initialized at the creation of a new city.
    name is by default empty
    id is given at creation of a new city

    Method:
    setXY(x, y) : define x and y values
    randomXY(rangeX, rangeY) : set random value for x and Y
    
    """
    count = 0

    def     randomXY(self, rangeX, rangeY=None):
        """Set x and y attribute of self to random value"""
        self.x = random.randrange(rangeX);
        if not rangeY:
            rangeY = rangeX
        self.y = random.randrange(rangeY);

    def     setXY(self, x, y):
        self.x = x
        self.y = y

    def     _get_id(self):
        return (self._id)

    def     _set_id(self, id):
        self._id = id

    id = property(_get_id, _set_id)

    def     __init__(self, rangeX, rangeY=None, name=""):
        """Constructor of City class, randomly init x and y value"""
        self.randomXY(rangeX, rangeY)
        self.name = name
        self._id = City.count
        City.count += 1

    def     __repr__(self):
        return "City {}: x = {} ; y = {}".format(self.name, self.x, self.y)
