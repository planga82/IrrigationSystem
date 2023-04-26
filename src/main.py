import _thread
import utime
import gc

execfile("utils.py")
execfile("logger.py")
execfile("led_control.py")
execfile("water_pump_control.py")
execfile("machine_state.py")


try:
    counter2 = 1
    while True:
        counter2 = update_counter(counter2)
        #--------------------------------------
        execute_every(counter2, 100, state_transitions)
        #execute_every(counter2, 100, print_current_status, current_state, current_cycles, button_engine_state, button_mode_state, engine_state, total_irrigation_cicles, total_waiting_cycles)
        execute_every(counter2, 50, engine_button)
        execute_every(counter2, 50, mode_button)
        execute_every(counter2, 5, update_engine_state, engine_state)
        if(led_state == 1):
            execute_every(counter2, 50, turn_internal_led)
        else:
            execute_every(counter2, 200, turn_internal_led)
        #--------------------------------------
        utime.sleep(0.01)        
        gc.collect()
except (OSError, Exception) as error:
    write_log_line([str(error)])

    
