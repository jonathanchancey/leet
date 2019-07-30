
class PeakableInterface(object):
    nextExists = True
    nextVal = 0
    it = iter([])


    def __init__(self, iterator):
        self.it = iterator
        self.next()

    def peek(self):
        return self.nextVal

    def next(self):
        # Invoking next() method should ensure that the ‘iter’ object is advanced before returning the cached next value in the form of ‘next’

        if not self.nextExists:
            return False
        
        try: 
            self.nextVal = self.it.__next__()
        except StopIteration:
            self.nextExists = False
            self.hasNext()
        
        
        # if tempNext:
        #     self.nextVal = tempNext
            
        return self.nextVal
        
    def hasNext(self):
        return self.nextExists


def main():
    # define a list
    my_list = [4, 7, 0, 3]

    # get an iterator using iter()
    my_iter = iter(my_list)

    # create pi object
    pi = PeakableInterface(my_iter)

    print(pi.peek())
    print(pi.next())
    print(pi.hasNext())
    print(pi.next())
    print(pi.next())
    print(pi.hasNext())
    print(pi.next())
    print(pi.next())
    print(pi.hasNext())


if __name__ == '__main__':
    main()