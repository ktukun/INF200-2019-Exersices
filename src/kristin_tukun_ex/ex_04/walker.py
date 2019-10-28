import random


class Walker:

    def __init__(self, start_position, home_position):
        self.position = start_position
        self.home = home_position
        self.steps = 0

    def move(self):
        self.steps += 1
        step = random.randint(0, 1)
        if step == 0:
            self.position -= 1
        else:
            self.position += 1
        return self.position

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps

