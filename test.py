from random import randrange

class MyTest():

    def __init__(self, name, id):
        self.id = id
        self.name = name
    
list = []
list.append(MyTest("elm1", 1))
list.append(MyTest("elm2", 2))
list.append(MyTest("elm3", 3))

elm = MyTest("elm1", 1)

if elm in list:
    print("oui")
else:
    print("non")
