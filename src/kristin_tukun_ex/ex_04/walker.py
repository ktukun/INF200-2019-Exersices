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

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps

    def walk_home(self):
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
