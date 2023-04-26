import machine
import utime

internal_led_status = 0

def turn_internal_led():
    global internal_led_status
    onboard_led = machine.Pin(25, machine.Pin.OUT)
    if(internal_led_status == 0):
        onboard_led.value(1)
        internal_led_status = 1
    else:
        onboard_led.value(0)
        internal_led_status = 0

        