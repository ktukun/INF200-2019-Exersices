# -*- coding: utf-8 -*-
from kristin_tukun_ex.ex_05.walker_sim import Walker, Simulation
import random

__author__ = 'Kristin Tukun'
__email__ = 'ktukun@nmbu.no'


class BoundedWalker(Walker):

    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """

        super().__init__(start, home)
        self.l_lim = left_limit
        self.r_lim = right_limit

    def move(self):
        """
        Change coordinate by +1 or -1 with equal probability.
        """

        self.steps += 1
        step = random.randint(0, 1)

        if self.get_steps() >= self.l_lim or self.get_steps() <= self.r_lim:
            if step == 0:
                self.position -= 1
            else:
                self.position += 1

        else: pass

    def walk_home(self):
        while self.is_at_home() is False:
            self.move()


class BoundedSimulation(Simulation):

    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """

        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.
        """
        walk = BoundedWalker(self.start, self.home, self.left_limit,
                             self.right_limit)
        walk.walk_home()
        return walk.get_steps()


if __name__ == "__main__":

    num_walks = 20
    right_lim = 20
    left_limits = [0, -10, -100, -1000, -10000]

    walker = BoundedSimulation(0, 20, 12345,  0, right_lim)

    print(walker.run_simulation(num_walks))

    walker = BoundedSimulation(0, 20, 12345,  -10, right_lim)

    print(walker.run_simulation(num_walks))

    walker = BoundedSimulation(0, 20, 12345,  -100, right_lim)

    print(walker.run_simulation(num_walks))

    walker = BoundedSimulation(0, 20, 12345,  -1000, right_lim)

    print(walker.run_simulation(num_walks))

    walker = BoundedSimulation(0, 20, 12345,  -10000, right_lim)

    print(walker.run_simulation(num_walks))
