import playground
import random

class Atom(object):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.size = float(size)
        self.speed_x = float(speed_x)
        self.speed_y = float(speed_y)
        self.color = color

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.size, self.color)

    def move(self, width, height):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        if self.pos_x <= self.size or self.pos_x > width - self.size:
            self.speed_x *= -1
            if self.pos_x > width - self.size:
                self.pos_x = width - self.size
        if self.pos_y <= self.size or self.pos_y > height - self.size:
            self.speed_y *= -1
            if self.pos_y > height - self.size:
                self.pos_y = height - self.size
        
class FallDownAtom(Atom):
    g = 1.0
    damping = 0.95

    def move(self, width, height):
        self.speed_y += FallDownAtom.g
        self.speed_y *= FallDownAtom.damping
        self.speed_x *= FallDownAtom.damping

        super(FallDownAtom, self).move(width, height)


class ExampleWorld(object):

    def __init__(self, count, width, height):
        self.size_x = width
        self.size_y = height
        self.atoms = []
        for x in range(count):
            self.atoms.append(self.random_atom())
    
    def random_atom(self):
        color = random.choice(list(playground.Colors)).value
        atom_type = random.choice((Atom, FallDownAtom))
        size = random.randrange(5, 20)
        pos_x = random.randrange(size, self.size_x - size)
        pos_y = random.randrange(size, self.size_y - size)
        speed_x = random.randrange(5, 10)
        speed_y = random.randrange(5, 10)

        return atom_type(pos_x, pos_y, speed_x, speed_y, size, color)
    
    def tick(self, size_x, size_y):
        ret = []
        for atom in self.atoms:
            atom.move(size_x, size_y)
            ret.append(atom.to_tuple())
        return tuple(ret)


if __name__ == '__main__':
    size_x, size_y = 400, 300
    world = ExampleWorld(10, size_x, size_y)
    playground.run((size_x, size_y), world)