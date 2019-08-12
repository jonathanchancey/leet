import random


def main(nums,per):
    randint = random.uniform(0, 1)

    # based on decimal 
    per_expanded = [int(i * 100) for i in per]
    # per_sum = [sum(per[0:i]) for i in range(per)]
    per_sum = []

    j = 0
    for i in per:
        j = j + i
        per_sum.append(j) 


    for i in per_sum:
        if i > randint:
            return i


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    per = [0.1, 0.5, 0.2, 0.2]
    
    print ("The value is {}".format(main(nums,per)))