import _thread
import utime

execfile("utils.py")
execfile("logger.py")
execfile("led_control.py")
execfile("capture_data.py")
execfile("water_pump_control.py")


def sensor_monitoring():
    t = capture_temperature()
    m = capture_soil_moisture()
    write_log_line([t,m])

def thread1():
    counter1 = 1
    while True:
        counter1 = update_counter(counter1)
        #--------------------------------------
        execute_every(counter1, 5, turn_on_internal_led)
        execute_every(counter1, 900, sensor_monitoring)
        #--------------------------------------
        utime.sleep(1)
    
def thread2():
    counter2 = 1
    while True:
        counter2 = update_counter(counter2)
        #--------------------------------------
        execute_every(counter2, 1, secure_pulling_control_button_state)
        #--------------------------------------
        utime.sleep(1)
    
_thread.start_new_thread(thread1, [])
thread2()

    
