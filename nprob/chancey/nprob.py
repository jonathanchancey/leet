# returns random value based on declared percentages

import random


def main(nums,per):
    # generates random value between 0 and 1
    randint = random.uniform(0, 1)

    per_sum = []
    # uses a simple loop to sum elements into a new array
    j = 0
    for i in per:
        j = j + i
        per_sum.append(j) 

    # compares the randomly generated value to the sumed percentages for pseudo random selection
    for i in per_sum:
        if i > randint:
            return i


if __name__ == '__main__':
    # given values for testing
    nums = [1, 2, 3, 4]
    per = [0.1, 0.5, 0.2, 0.2]
    
    print ("The value is {}".format(main(nums,per)))