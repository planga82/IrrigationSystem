import machine
import utime

def turn_on_water_pump():
    engine = machine.Pin(18, machine.Pin.OUT)
    engine.value(1)
    
def turn_off_water_pump():
    engine = machine.Pin(18, machine.Pin.OUT)
    engine.value(0)
    
def control_button():
    button_pump_control = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
    if (button_pump_control.value() == 1):
        turn_on_water_pump()
    else:
        turn_off_water_pump()
        