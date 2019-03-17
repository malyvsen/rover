from gpiozero import DigitalOutputDevice, PWMOutputDevice


class Motor:
    def __init__(self, pin_forward, pin_backward, pin_pwm):
        self.forward = DigitalOutputDevice(pin_forward)
        self.backward = DigitalOutputDevice(pin_backward)
        self.pwm = PWMOutputDevice(pin_pwm)


    @property
    def speed(self):
        if self.forward.value == self.backward.value:
            return 0 # soft stop
        if self.forward.value == 1:
            return self.pwm.value # going forward
        return -self.pwm.value # going backward


    @speed.setter
    def speed(self, value):
        if value > 0:
            self.forward.value = 1
            self.backward.value = 0
            self.pwm.value = value
        else:
            self.forward.value = 0
            self.backward.value = 1
            self.pwm.value = -value


    def soft_stop(self):
        self.forward.value = 0
        self.backward.value = 0
        self.pwm.value = 1
