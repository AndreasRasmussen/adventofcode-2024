from abc import abstractmethod
import AbstractBaseSolver


class AbstractSolver(AbstractBaseSolver.AbstractBaseSolver):

    def set_input_data(self, day):
        with open(f'inputs/day{self._day}.txt') as f:
            self._input_data = f.readlines()

    def get_input_data(self):
        return self._input_data

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass

    def print_solutions(self):
        print(f'----- day {self._day:02} -----')
        print(f'Solution to part 1: {self.solve_part1()}')
        print(f'Solution to part 2: {self.solve_part2()}')
        print('')
