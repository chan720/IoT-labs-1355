# main.py -- put your code here!
# from machine import Pin
# from time import sleep

# btn = Pin(0, Pin.IN, Pin.PULL_UP)

# while True:
#     sleep(0.4)
#     print(btn.value())

from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(48, Pin.OUT)   # Set GPIO48 to output for NeoPixel
neo = NeoPixel(pin, 1)   # Create NeoPixel driver on GPIO48 for 1 pixel

colors = [(255, 0, 0),   # Red
          (0, 255, 0),   # Green
          (0, 0, 255)]   # Blue

while True:
    for color in colors:
        neo[0] = color  # Set the pixel to the current color
        neo.write()      # Write data to the NeoPixel
        time.sleep(0.3)  # Wait for 0.5 seconds before changing color