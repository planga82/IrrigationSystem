import time
import board
import led_control
import motor_control
import flow_control

l = LedControl(2)
motor = MotorControl(board.GP2)
flow = FlowControl(board.GP17)
expected_ml = 50
period = 30

last_time = time.monotonic()
try:
    while True:
        print("start")
        l.led_blink()
        if (time.monotonic() - last_time > period):
            print("flow")
            motor.turn_on()
            flow.wait_until(expected_ml)
            motor.turn_off()
            last_time = time.monotonic()
        print("end")
        time.sleep(1)
except:
    print("Process finished")
    motor.turn_off()




