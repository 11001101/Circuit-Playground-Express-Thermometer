# Simple visual thermometer for Circuit Playground Express
# turns off the Circuit Playground Express when light sensor "senses darkness"
# shows red as value of temp and blue as extra pixels

import time
from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx

cp.pixels.auto_write = False
cp.pixels.brightness = 0.01
x = True

# Set these based on your ambient temperature in Celsius
# default is from 20 - 30 Celsius
minimum_temp = 20
maximum_temp = 30
min_light = 10
offset = 3.2 
# degrees C offset drift at steady state circuit playground express, 
# this is hardware specific and will change

def scale_range(value):
# Scales a value from the range of minimum_temp to maximum_temp (temperature range) to 0-10
# (the number of NeoPixels). Allows remapping temperature value to pixel position.
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)

while True:
    peak = scale_range(cp.temperature - offset)
    # optional printing to view the values form the sensors
    print(cp.temperature-offset)
    print(int(peak))
    print(cpx.light)

    if cpx.light > min_light and cp.switch is True:
        x = True
    elif cpx.light < min_light or cp.switch is False:
        x = False

    if x is True:
        for i in range(10):
            if i <= peak - 1:
                cp.pixels[i] = (255, 0, 0)
            else:
                cp.pixels[i] = (0, 0, 255)
    elif x is False:
        for i in range(10):
            if i <= peak - 1:
                cp.pixels[i] = (0, 0, 0)
            else:
                cp.pixels[i] = (0, 0, 0)

    cp.pixels.show()
    time.sleep(0.7)
