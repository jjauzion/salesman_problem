from random import randrange

def init(rx, ry=None):
    x = rx
    if not ry:
        y = rx
    else:
        y = ry
    return (x, y)

x, y = init(10, 5)
print("x = {} ; y = {}".format(x, y))
