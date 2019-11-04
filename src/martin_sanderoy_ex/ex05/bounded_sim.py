# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'
import random
from walker_sim import Walker
from walker_sim import Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        super(Walker, self).__init__()
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
        self.start = start
        self.home = home
        self.position = start
        self.steps = 0
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        """Equal chance to move backwards and forwards by 1 step,
        but can not move beyond boundary limits."""
        self.steps += 1
        if random.randint(0, 1) == 0:
            if self.position is not self.left_limit:
                self.position -= 1
        else:
            if self.position is not self.right_limit:
                self.position += 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super(Simulation, self).__init__()
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
        self.start = start
        self.home = home
        self.seed = seed
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


"""
Try to make as much use of the methods of the respective superclass as
possible when implementing the subclasses!

The main section of the script shall simulate

-  20 walks from start 0 to home 20 for each of the following left
   boundaries: 0, -10, -100, -1000, -10000. The right boundary shall be
   20 in all cases.
-  Print results as left boundary followed by a list of the 20 walk
   durations for that left boundary.
"""

if __name__ == '__main__':
    left_boundary = [0, -10, -100, -1000, -10000]
    right_boundary = 20
    right_limit = right_boundary
    start = 0
    home = 20
    seed = 12345
    num_sims = 20
    for left_limit in left_boundary:
        sim = BoundedSimulation(start, home, seed, left_limit, right_limit)
        print('left boundary: {} walk durations: {}'
              .format(left_limit, sim.run_simulation(num_sims)))
