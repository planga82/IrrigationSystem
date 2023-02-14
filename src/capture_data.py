import machine
   
    
def capture_temperature():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / 65535
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    return str(round(temperature, 1))

def capture_soil_moisture():
    soil = machine.ADC(machine.Pin(26))
    min_moisture=0
    max_moisture=65535
    moisture = (max_moisture - soil.read_u16()) * 100 / (max_moisture - min_moisture)
    return str(int(moisture))

    