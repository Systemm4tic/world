<<<<<<< HEAD
from random import randint


class Maps():

    def __init__(self):
        self.numberOfGrounds = 2
        self.map = self.generate()

    def generate(self):
        map = []
        for i in range(100):
            row = []
            for j in range(100):
                row.append(randint(1,self.numberOfGrounds))
            map.append(row)
        return map
=======
from random import randint


class Maps():

    def __init__(self):
        self.numberOfGrounds = 2
        self.map = self.generate()

    def generate(self):
        map = []
        for i in range(100):
            row = []
            for j in range(100):
                row.append(randint(1,self.numberOfGrounds))
            map.append(row)
        return map
>>>>>>> c9577c66061b7a0bcf414469536be6821967ec0a
