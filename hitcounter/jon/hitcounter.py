import time

class hitcounter:
    hit_times = [ ]


    def record(self, timestamp):
        self.hit_times.append(timestamp)

    def total(self):
        return len(self.hit_times)

    def rang(self, lower, upper):
        count = 0
        for hit in self.hit_times:
            if hit > lower and hit < upper:
                count = count + 1
        return count


def main():
    HCo = hitcounter()

    HCo.record(int(time.time()))
    HCo.record(int(time.time())-2)
    HCo.record(int(time.time())-10)
    time.sleep(.2)
    HCo.record(int(time.time()))

    print("HCo.total()", HCo.total())
    print("Range test", HCo.rang(int(time.time())-1,int(time.time())+.1))

if __name__ == '__main__':
    main()