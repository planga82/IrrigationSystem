import time
import board
from led_control import *
from motor_control import *
from flow_control import *

l = LedControl(2)
motor = MotorControl(board.GP2)
flow = FlowControl(board.GP17)
expected_ml = 110
period = 60 * 60 * 24 # 1 day in second

last_time = time.monotonic()
try:
    while True:
        l.led_blink()
        if (time.monotonic() - last_time > period):
            motor.turn_on()
            flow.wait_until(expected_ml)
            motor.turn_off()
            last_time = time.monotonic()
        time.sleep(1)
except:
    print("Process finished")
    motor.turn_off()
