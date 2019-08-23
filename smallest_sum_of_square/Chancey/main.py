#smallest number of squared integers which sum to n
import math

def snosi(constituents, number):
    # calculates the sum of the constituents because we use the value twice
    calcdsum = sum(i ** 2 for i in constituents)
    
    if calcdsum == number:
        # print("constituents = ", [str(constituent) + "^2" for constituent in constituents])
        return len(constituents) # we're done

    # print("Adding ", int(math.sqrt(number-calcdsum)))
    constituents.append(int(math.sqrt(number-calcdsum)))
    
    # print("Recursion with ", constituents, number)
    return snosi(constituents, number)

def main():
    n = 13
    risto = []
    # risto[0] = n
    count = snosi(risto, n)
    print("The smallest number of squared integers which sum to the number {} is {}".format(n, count))

if __name__ == '__main__':
    main()