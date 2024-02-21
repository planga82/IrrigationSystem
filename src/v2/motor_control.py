import digitalio

class MotorControl:
    def __init__(self, motor_pin):
        self.motor = digitalio.DigitalInOut(motor_pin)
        self.motor.direction = digitalio.Direction.OUTPUT

    def turn_on(self):
        self.motor.value = 1

    def turn_off(self):
        self.motor.value = 0
