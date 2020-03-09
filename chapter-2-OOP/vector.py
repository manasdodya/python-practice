
class Vector:
    """ Represent a vector in multidiemnsional space """

    def __init__(self,d):
        """ Creates d dimensional vector of zeros """
        self._coords = [0]*d

    def __len__(self):
        """ Returns the dimension of vector """
        return len(self._coords)

    def __getitem__(self, j):
        """ Returns the jth coordinate of the vector """
        return self._coords[j]

    def __setitem__(self, j, val):
        """ Set the jth coordinate of the vector to given value """
        self._coords[j] = val

    def __add__(self, other):
        """ Returns sum of two vectors """
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """ Retun true if vector has same coordinates as other """
        return self._coords == other.__coords

    def __ne__(self, other):
        """ Return true if vector differ from other """
        return not self == other

    def __str__(self):
        """ Produce string representation of a vector """
        return '<' + str(self._coords)[1:-1] + '>'


v = Vector(5)
v[1] = 23
v[-1] = 45
print(v[4])
u = v + v
print(u)
total = 0
for entry in v:
    total += entry

print(total)
