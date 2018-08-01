from random import randrange

class MyTest():

    def __init__(self):
        self.list = [1, 2, 3, 4, 5, 6, 7, 8]

    def __getitem__(self, index):
        if isinstance(index, slice):
            print("slice : ", index)
            return self.list[index]
        else:
            print("index : ", index)
            return self.list[index]

    def __setitem__(self, index, val):
        if isinstance(index, slice):
            print("index slice : ", index)
            self.list[index] = val
        else:
            print("index index : ", index)
            self.list[index] = val
        if isinstance(val, slice):
            print("val slice : ", val)
            self.list[index] = val
        else:
            print("val index : ", val)
            self.list[index] = val
    
elm = MyTest()
elm2 = MyTest()
r1 = elm[3]
r2 = elm[1:5]
print("r1 = {}\nr2 = {}".format(r1, r2))
elm2[6] = elm[0]
elm2[0:3] = elm[2:5]
print("elm2 = {}".format(elm2))
