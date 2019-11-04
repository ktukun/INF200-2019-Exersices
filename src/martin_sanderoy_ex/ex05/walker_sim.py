# -*- coding: utf-8 -*-

__author__ = 'Martin Sanderøy'
__email__ = 'martsand@nmbu.no'
import random


class Walker:
    def __init__(self, initial_position, home_position):
        self.position = initial_position
        self.home = home_position
        self.distance = abs(initial_position - home_position)
        self.steps = 0

    def move(self):
        """Equal chance to move backwards and forwards by 1 step"""
        self.steps += 1
        if random.randint(0, 1) == 0:
            self.position -= 1
        else:
            self.position += 1

    def is_at_home(self):
        """Check if walker is at his home"""
        return self.position == self.home

    def get_position(self):
        """returns current position"""
        return self.position

    def get_steps(self):
        """returns number of steps taken"""
        return self.steps

    def walk_home(self):
        """walks until the walker is home"""
        while self.is_at_home() is False:
            self.move()


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
        self.seed = seed

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walk = Walker(self.start, self.home)
        walk.walk_home()
        return walk.get_steps()

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
        random.seed(self.seed)
        walks = []*num_walks
        for _ in range(num_walks):
            walks.append(self.single_walk())
        return walks


if __name__ == '__main__':
    """
    The main section of the script shall simulate
    -  20 walks from start 0 to home 10
    -  20 walks from start 10 to home 0
    -  for each of those cases simulate *twice* with seed value 12345 and
       *once* with seed value 54321
    -  print the resulting lists (six lists in total).
    """
    num_sims = 20
    sim = Simulation(0, 10, 12345)
    print('20 simulation with start:0, home:10, seed:12345. ',
          sim.run_simulation(num_sims))
    sim = Simulation(0, 10, 12345)
    print('20 simulation with start:0, home:10, seed:12345. ',
          sim.run_simulation(num_sims))
    sim = Simulation(0, 10, 54321)
    print('20 simulation with start:0, home:10, seed:54321. ',
          sim.run_simulation(num_sims))

    sim = Simulation(10, 0, 12345)
    print('20 simulation with start:10, home:0, seed:12345. ',
          sim.run_simulation(num_sims))
    sim = Simulation(10, 0, 12345)
    print('20 simulation with start:10, home:0, seed:12345. ',
          sim.run_simulation(num_sims))
    sim = Simulation(10, 0, 54321)
    print('20 simulation with start:10, home:0, seed:54321. ',
          sim.run_simulation(num_sims))
