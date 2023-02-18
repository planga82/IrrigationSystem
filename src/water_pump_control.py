import machine
import utime

def turn_on_water_pump():
    engine = machine.Pin(18, machine.Pin.OUT)
    engine.value(1)
    
def turn_off_water_pump():
    engine = machine.Pin(18, machine.Pin.OUT)
    engine.value(0)
    
def press_button(pin):
    global pump_state
    pump_state = not pump_state
    if (pump_state):
        turn_on_water_pump()
    else:
        turn_off_water_pump()
        
def secure_pulling_control_button_state():
    global pump_state
    global button_pump_control
    if(button_pump_control.value() == 0):
        turn_off_water_pump()
        pump_state = False

pump_state = False
button_pump_control = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pump_control.irq(trigger= machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=press_button)




    



