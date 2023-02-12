import _thread
import utime

execfile("logger.py")
execfile("led_control.py")
execfile("capture_data.py")

# TODO use asyncio

_thread.start_new_thread(start_led_control, [])

while True:
    t = capture_temperature()
    m = capture_soil_moisture()
    write_log_line([t,m])
    utime.sleep(900)
    
