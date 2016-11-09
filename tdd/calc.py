class Calculator(object):

    def add(self, x, y):
        return x + y

    def add_plus(self, x, y, z):
        return self.add(self.add(x, y), z)