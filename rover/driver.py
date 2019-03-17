from rover.motor import Motor


class Driver:
    def __init__(self, left_motor=None, right_motor=None):
        self.left_motor = left_motor if left_motor is not None else Motor(17, 27, 22)
        self.right_motor = left_motor if left_motor is not None else Motor(3, 2, 4)
