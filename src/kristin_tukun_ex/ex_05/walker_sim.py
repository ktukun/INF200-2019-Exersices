# -*- coding: utf-8 -*-

__author__ = 'Kristin Tukun'
__email__ = 'ktukun@nmbu.no'

class Walker:

    def __init__(self, start_position, home_position):
        """
        :param start_position: initial position of the walker
        :param home_position: position of the walker's home
        """
        self.position = start_position
        self.home = home_position
        self.steps = 0

    def move(self):
        """
        Change coordinate by +1 or -1 with equal probability.
        """

        self.steps += 1
        step = random.randint(0, 1)
        if step == 0:
            self.position -= 1
        else:
            self.position += 1

    def is_at_home(self):
        """Returns True if walker is at home position."""
        return self.position == self.home

    def get_position(self):
        """Returns current position."""
        return self.position

    def get_steps(self):
        """Returns number of steps taken by walker."""
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
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
        """
        self.start = start
        self.home = home
        self.seed =

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """