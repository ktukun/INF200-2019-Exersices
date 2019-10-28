# -*- coding: utf-8 -*-

__author__ = 'Kristin Tukun'
__email__ = 'kristin.tukun@nmbu.no'

import random


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

    def walk_home(self):
        """
        Runs the walker simulation as long as the walker is not home.
        Breaks the simulation if the steps becomes to many.
        """
        while Walker.is_at_home(self) is False:
            Walker.move(self)
            if self.steps > 1000000:
                break


if __name__ == "__main__":

    start = 0
    home = [1, 2, 5, 10, 20, 50, 100]

    for distance in home:
        number_of_steps = [] * 5

        for _ in range(5):
            student = Walker(start, distance)
            student.walk_home()
            antall = student.get_steps()
            number_of_steps.append(antall)
        print('Distance: {0}, Path lengths: {1}'.format(distance,
                                                        number_of_steps))
