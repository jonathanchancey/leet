class PeekableInterface(object):
    iterator = iter([])
    nextVal = []
    nextExists = True

    def __init__(self, iterator):
        self.iterator = iterator
        self.nextVal = self.iterator.__next__()

    def peek(self):
        try:
            self.nextVal = self.iterator.__next__()
        except:
            self.nextExists = False

        return (self.nextExists, self.nextVal)[self.nextExists]

    def next(self):
        tempNext = self.nextVal
        self.peek()
        return tempNext

    def hasNext(self):
        return self.nextExists