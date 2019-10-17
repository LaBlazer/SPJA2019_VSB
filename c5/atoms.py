import playground
from random import randint

class ExampleWorld(object):
    
    def __init__(self, size_x, size_y, atoms_count):
        self._atom_size_limits = (5, 20)
        self._atom_vel_limits = (1, 10)
        self._width = size_x
        self._height = size_y
        self._atoms = []

        for i in range(atoms_count):
            rad = randint(self._atom_size_limits[0], self._atom_size_limits[1])
            x = randint(rad, self._width - rad)
            y = randint(rad, self._height - rad)
            vx = randint(self._atom_vel_limits[0], self._atom_vel_limits[1])
            vy = randint(self._atom_vel_limits[0], self._atom_vel_limits[1])
            self._atoms.append(Atom(x, y, vx, vy, rad))

    def tick(self):
        for a in self._atoms:
            a.move(self._width, self._height)
            yield a.to_tuple()


class Atom:

    def __init__(self, x, y, vx, vy, radius):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
        self._radius = radius

    def to_tuple(self):
        return (self._x, self._y, self._radius)

    def move(self, size_x, size_y):
        if (self._x + self._radius) >= size_x or (self._x - self._radius) <= 0:
            self._vx *= -1
        if (self._y + self._radius) >= size_y or (self._y - self._radius) <= 0:
            self._vy *= -1

        self._x += self._vx
        self._y += self._vy

if __name__ == '__main__':
    size_x, size_y = 400, 300

    world = ExampleWorld(size_x, size_y, 10)
    playground.run((size_x, size_y), world)
