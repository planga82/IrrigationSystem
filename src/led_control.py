import machine
from machine import Timer
import utime

def turn_on_internal_led(sleep_period = 1):
    onboard_led = machine.Pin(25, machine.Pin.OUT)
    onboard_led.value(1)
    utime.sleep(sleep_period)
    onboard_led.value(0)
    
# TODO use asyncio
def start_led_control(custom_period = 30):
    while True:
        turn_on_internal_led()
        utime.sleep(custom_period)
    