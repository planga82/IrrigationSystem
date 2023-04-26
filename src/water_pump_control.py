import machine
import utime


engine_switch = 0
    
def update_engine_state(engine_state):
    global engine_switch
    engine = machine.Pin(18, machine.Pin.OUT)
    if (engine_state == 1):
        # To reduce pump water power
        if(engine_switch >= 6):
            engine_switch = 0
        else:
            engine_switch = engine_switch + 1
        if(engine_switch == 0):   
            engine.value(0)
        else:
            engine.value(1)
    else:
        engine.value(0)
    
def engine_button():
    global button_engine_state
    button_engine_control = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_engine_state = button_engine_control.value()
    
def mode_button():
    global button_mode_state
    button_mode_control = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_mode_state = button_mode_control.value()
        