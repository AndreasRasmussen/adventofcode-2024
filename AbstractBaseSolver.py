from abc import ABCMeta, abstractmethod


class AbstractBaseSolver(metaclass=ABCMeta):

    def __init__(self, day):
        self._day = day
        self._input_data = []
        self.set_input_data(self._day)

    @abstractmethod
    def set_input_data(self, day):
        pass

    @abstractmethod
    def get_input_data(self):
        pass

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass

    @abstractmethod
    def print_solutions(self):
        pass
