
execfile("logger.py")

# Posible states
I_OFF = "IRRIGATION-ACTIVE-WATER-OFF"
I_A_ON = "IRRIGATION-ACTIVE-AUTOMATIC-WATER-ON"
I_M_ON = "IRRIGATION-ACTIVE-MANUAL-WATER-ON"
C_OFF = "CONFIGURATION-ACTIVE-WATER-OFF"
C_ON = "CONFIGURATION-ACTIVE-WATER-ON"

#Global constants
total_irrigation_cicles = 3
total_waiting_cycles = 1440 #24h

#Global variables
current_cycles = 0
current_state = I_OFF

# Input variables
button_engine_state = 0
button_mode_state = 0

# Output variables
engine_state = 0
led_state = 0

def set_I_OFF():
    global current_cycles
    global current_state
    global engine_state
    global led_state
    current_state = I_OFF
    current_cycles = 0
    engine_state = 0
    led_state = 0
    write_log_line([current_state])
    
def set_I_A_ON():
    global current_cycles
    global current_state
    global engine_state
    global led_state
    current_state = I_A_ON
    current_cycles = 0
    engine_state = 1
    led_state = 0
    write_log_line([current_state])
    
def set_I_M_ON():
    global current_cycles
    global current_state
    global engine_state
    global led_state
    current_state = I_M_ON
    current_cycles = 0
    engine_state = 1
    led_state = 0
    write_log_line([current_state])
    
def set_C_OFF(update_total_irrigation_cyles):
    global current_cycles
    global current_state
    global engine_state
    global total_irrigation_cicles
    global led_state
    current_state = C_OFF
    if(update_total_irrigation_cyles):
        total_irrigation_cicles = current_cycles
    current_cycles = 0
    engine_state = 0
    led_state = 1
    write_log_line([current_state])
    
def set_C_ON():
    global current_cycles
    global current_state
    global engine_state
    global led_state
    current_state = C_ON
    current_cycles = 0
    engine_state = 1
    led_state = 1
    write_log_line([current_state])

def state_transitions():
    global current_state
    global current_cycles
    global button_engine_state
    global button_mode_state
    global engine_state
    global total_irrigation_cicles
    global total_waiting_cycles
    
    current_cycles = current_cycles + 1
    if(current_state == I_OFF):
        if(button_mode_state == 1):
            set_C_OFF(False)
            return
        if(button_engine_state == 1):
            set_I_M_ON()
            return
        if(current_cycles >= total_waiting_cycles):
            set_I_A_ON()
            return
            
    if(current_state == I_A_ON):
        if(current_cycles >= total_irrigation_cicles):
            set_I_OFF()
            return
        
    if(current_state == I_M_ON):
        if(button_engine_state == 1):
            set_I_OFF()
            return
        
    if(current_state == C_OFF):
        if(button_mode_state == 1):
            set_I_OFF()
            return
        if(button_engine_state == 1):
            set_C_ON()
            return
        
    if(current_state == C_ON):
        if(button_engine_state == 1):
            set_C_OFF(True)
      
def print_current_status(current_state, current_cycles, button_engine_state, button_mode_state, engine_state, total_irrigation_cicles, total_waiting_cycles):
    print("current_state:" + str(current_state) + " current_cycles:" + str(current_cycles) + " button_engine_state:" + str(button_engine_state) + " button_mode_state:" + str(button_mode_state) + " engine_state:" + str(engine_state) + " total_irrigation_cicles:" + str(total_irrigation_cicles) + " total_waiting_cycles:" + str(total_waiting_cycles))



