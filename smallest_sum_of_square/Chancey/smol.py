import math
def s(c, n):
    u = sum(i**2 for i in c)
    if u == n:
        return len(c)
    c.append(int(math.sqrt(n-u)))
    return s(c, n)
def main():
    n = 13
    risto = []
    count = s(risto, n)
    print("#{}={}".format(n, count))
if __name__ == '__main__':
    main()