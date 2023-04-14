import _thread
import utime

execfile("utils.py")
execfile("led_control.py")
execfile("water_pump_control.py")
execfile("machine_state.py")



def thread1():
    counter1 = 1
    while True:
        counter1 = update_counter(counter1)
        #--------------------------------------
        if(led_state == 1):
            execute_every(counter1, 1, turn_on_internal_led, 0.3)
        else:
            execute_every(counter1, 5, turn_on_internal_led, 1)
        #--------------------------------------
        utime.sleep(0.3)
    
def thread2():
    counter2 = 1
    while True:
        counter2 = update_counter(counter2)
        #--------------------------------------
        execute_every(counter2, 2, state_transitions)
        execute_every(counter2, 2, print_current_status, current_state, current_cycles, button_engine_state, button_mode_state, engine_state, total_irrigation_cicles, total_waiting_cycles)
        execute_every(counter2, 1, engine_button)
        execute_every(counter2, 1, mode_button)
        execute_every(counter2, 2, update_engine_state, engine_state)
        #--------------------------------------
        utime.sleep(0.5)
    
_thread.start_new_thread(thread1, [])
thread2()

    
