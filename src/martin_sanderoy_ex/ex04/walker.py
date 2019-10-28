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
        while Walker.is_at_home(self) is False:
            Walker.move(self)


if __name__ == '__main__':
    start = 0
    home = [1, 2, 5, 10, 20, 50, 100]
    for home in home:
        students = []*5
        distance = abs(home-start)
        for _ in range(5):
            student = Walker(start, home)
            student.walk_home()
            students.append(student.get_steps())
        print('Distance: {0} -> Path lengths: {1}'.format(distance, students))
