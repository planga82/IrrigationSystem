import time
import board
import countio
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
            self.last_transition_s = current_time

class MotorControl:
    def __init__(self, motor_pin):
        self.motor = digitalio.DigitalInOut(motor_pin)
        self.motor.direction = digitalio.Direction.OUTPUT

    def turn_on(self):
        self.motor.value = 1

    def turn_off(self):
        self.motor.value = 0

class FlowControl:
    def __init__(self, flow_pin):
        self.counter = countio.Counter(flow_pin, edge=countio.Edge.RISE)
        self.ml_count = 2.3

    def wait_until(self,expected_ml):
        current = 0
        expected_counts = expected_ml / self.ml_count
        self.counter.reset()
        while current < expected_counts:
            current = self.counter.count
            time.sleep(0.1)
        self.counter.reset()



l = LedControl(2)
motor = MotorControl(board.GP2)
flow = FlowControl(board.GP17)
expected_ml = 50
period = 30

last_time = time.monotonic()
try:
    while True:
        print("start")
        l.led_blink()
        if (time.monotonic() - last_time > period):
            print("flow")
            motor.turn_on()
            flow.wait_until(expected_ml)
            motor.turn_off()
            last_time = time.monotonic()
        print("end")
        time.sleep(1)
except:
    print("Process finished")
    motor.turn_off()




