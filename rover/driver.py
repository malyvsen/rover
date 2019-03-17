import numpy as np
from rover.motor import Motor
from rover import config


class Driver:
    def __init__(self, left_motor=None, right_motor=None):
        if left_motor is not None:
            self.left_motor = left_motor
        else:
            self.left_motor = Motor(config.left_motor_forward, config.left_motor_backward, config.left_motor_pwm)
        if right_motor is not None:
            self.right_motor = right_motor
        else:
            self.right_motor = Motor(config.right_motor_forward, config.right_motor_backward, config.right_motor_pwm)


    @property
    def speed(self):
        return np.array((self.left_motor.speed, self.right_motor.speed), dtype=np.float32)


    @speed.setter
    def speed(self, value):
        self.left_motor.speed = value[0]
        self.right_motor.speed = value[1]


    def soft_stop():
        self.left_motor.soft_stop()
        self.right_motor.soft_stop()
