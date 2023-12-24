""" You’re given an array of positive integers, weights, where \
    weights[i] is the weight of the i th index. \

    Write a function, Pick Index(), which performs weighted random
    selection to return an index from the weights array. The larger
    the value of weights[i], the heavier the weight is, and the higher
    the chances of its index being picked.

    Suppose that the array consists of the weights [12, 84, 35]. In this
    case, the probabilities of picking the indexes will be as follows:

    Index 0:
    12/(12+84+35) = 9.2%

    Index 1:
    84/(12+84+35)=64.1%

    Index 2:
    35/(12+84+35)=26.7%
"""
import random
from typing import List


class RandomPickWithWeight:

    def __init__(self, weights: List[int]):
        self.weights = weights

        self.total_sum = 0
        self.prob_sum = []

        for w in weights:
            self.total_sum += w
            self.prob_sum.append(self.total_sum)

    def pick_index(self):
        rd = random.randint(0, self.total_sum)

        # Search for index corresponding to randomly picked value
        # in the probability line
        # >> First element greater than 'rd'
        low = 0
        high = len(self.prob_sum) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.prob_sum[mid] >= rd:
                if mid > 0 and self.prob_sum[mid - 1] >= rd:
                    high = mid - 1
                else:
                    return mid
            else:
                low = mid + 1

        return 0


# Driver code
def main():
    # rd = RandomPickWithWeight([12, 84, 35])
    # print(rd.weights)
    # print(rd.prob_sum)
    # print(rd.total_sum)

    # return

    counter = 900

    weights = [[1, 2, 3, 4, 5],
                [1, 12, 23, 34, 45, 56, 67, 78, 89, 90],
                [10, 20, 30, 40, 50],
                [1, 10, 23, 32, 41, 56, 62, 75, 87, 90],
                [12, 20, 35, 42, 55],
                [10, 10, 10, 10, 10],
                [10, 10, 20, 20, 20, 30],
                [1, 2, 3],
                [10, 20, 30, 40],
                [5, 10, 15, 20, 25, 30]]

    dict = {}
    for i in range(len(weights)):
        print("\n")
        print(i + 1, ". List of weights: ", weights[i], ", pick_index() called ", counter, " times", sep="")
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        sol = RandomPickWithWeight(weights[i])
        for j in range(counter):
            index = sol.pick_index()
            dict[index] += 1
        print("-"*105)
        print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format( \
            "Indexes", "|", "Weights", "|", "Occurences", "|", "Actual Frequency", "|", "Expected Frequency"))
        print("-"*105)
        for key, value in dict.items():

            print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format(key, "|", weights[i][key], "|", value, "|", \
                str(round((value/counter)*100, 2)) + "%", "|", str(round(weights[i][key]/sum(weights[i])*100, 2))+"%"))
        dict = {}
        print("\n", "-"*105, sep="")


if __name__ == '__main__':
    main()
