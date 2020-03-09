
class SequenceIterator:
    """ An iterator for any of Python's sequence type """

    def __init__(self,sequence):
        """ creates an iterator for the given sequence """
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """ Return next element or raise StopIteration Error """
        self_k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__():
        """ By convention, an iterator must return itself as an iterator """
        return self
