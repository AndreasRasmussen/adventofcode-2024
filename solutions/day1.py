import AbstractSolver
from collections import Counter

class Day1Solver(AbstractSolver.AbstractSolver):

    def solve_part1(self):
        list1 = []
        list2 = []
        lines = [[int(y) for y in x.rstrip().split('   ')] for x in self.get_input_data()]
        for line in lines:
            list1.append(line[0])
            list2.append(line[1])

        list1.sort()
        list2.sort()

        dist = 0
        for x in range(len(lines)):
            dist += abs(list1[x] - list2[x])

        return dist

    def solve_part2(self):
        list1 = []
        list2 = []
        lines = [[int(y) for y in x.rstrip().split('   ')] for x in self.get_input_data()]
        for line in lines:
            list1.append(line[0])
            list2.append(line[1])

        counted_list2 = Counter(list2)
        dist = 0
        for elem in list1:
            dist += elem * counted_list2[elem]
        return dist