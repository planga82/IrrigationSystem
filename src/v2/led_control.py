import time
import board
import digitalio

class LedControl:
    def __init__(self, period):
        self.last_transition_s = time.monotonic()
        self.period = period
        self.led = digitalio.DigitalInOut(board.LED)
        self.led.direction = digitalio.Direction.OUTPUT

    # led blink
    def led_blink(self):
        current_time = time.monotonic()
        if (current_time - self.last_transition_s > self.period):
            self.led.value = not self.led.value
            self.last_transition_s = current_time# Write your code here :-)
