
class Range:
    """ A class that mimics the built in range class """
    def __init__(start, stop=None, step =1):
        """
        Initialize a Range instance
        Semantics are similar to built-in range class
        """
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop == None:
            start,stop = 0,start

        # Calculate the effective lenght once
        self._length = max(0, (stop - start  + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        """ Returns number of entries in a range """
        return self._length

    def __getitem__(self, k):
        """ Returns entry at index k (using standard interpretation if negative) """
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step
