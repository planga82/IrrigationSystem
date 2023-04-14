import machine
import utime

    
def update_engine_state(engine_state):
    engine = machine.Pin(18, machine.Pin.OUT)
    engine.value(engine_state)
    
def engine_button():
    global button_engine_state
    button_engine_control = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_engine_state = button_engine_control.value()
    
def mode_button():
    global button_mode_state
    button_mode_control = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_mode_state = button_mode_control.value()
        