import sys,tty,termios
import os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

import time
import board
import neopixel

# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
# pixel_pin = board.NEOPIXEL

# On a Raspberry pi, use this instead, not all pins are supported
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 12

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    char = getch()
    
    if char in ("V"):
        print("Red!")
        pixels.fill((255, 0, 0))
        pixels.show()
        os.system('bash /home/pi/Programs/rp400vision.sh')

    if char in ("g","green"):
        print("Green!")
        pixels.fill((0, 255, 0))
        pixels.show()
        
    if char in ("H"):
        print("Blue!")
        pixels.fill((0, 0, 255))
        pixels.show()
        os.system('bash /home/pi/Programs/rp400ptt.sh')

    if char in ("z","zoom"):
        print("Zoom!")
        pixels.fill((255, 255, 255))
        pixels.show()

    if char in ("t","tired","rainbow"):
        print("Rainbow colors!")
        rainbow_cycle(0.001)

    if char in ("s","stop"):
        print("Stop Neopixel")
        pixels.fill((0, 0, 0))
        pixels.show()

    if char in ("x","q","quit"):
        print("Program Ended")
        pixels.fill((0, 0, 0))
        pixels.show()
        break
        
