# Raspberry Pi 400
## How to use and customize raspi400


```pi@raspi400:~ $  sudo pip3 install adafruit-circuitpython-neopixel

Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple

Collecting adafruit-circuitpython-neopixel
  Downloading https://www.piwheels.org/simple/adafruit-circuitpython-neopixel/adafruit_circuitpython_neopixel-6.0.0-py3-none-any.whl

Collecting Adafruit-Blinka (from adafruit-circuitpython-neopixel)
  Downloading https://www.piwheels.org/simple/adafruit-blinka/Adafruit_Blinka-5.8.1-py3-none-any.whl (137kB)
    100% |████████████████████████████████| 143kB 252kB/s 

...

Installing collected packages: Adafruit-PureIO, rpi-ws281x, pyusb, pyftdi, Adafruit-PlatformDetect, sysv-ipc, Adafruit-Blinka, adafruit-circuitpython-pypixelbuf, adafruit-circuitpython-neopixel

Successfully installed Adafruit-Blinka-5.8.1 Adafruit-PlatformDetect-2.22.2 Adafruit-PureIO-1.1.7 adafruit-circuitpython-neopixel-6.0.0 adafruit-circuitpython-pypixelbuf-2.2.0 pyftdi-0.52.0 pyusb-1.1.0 rpi-ws281x-4.2.5 sysv-ipc-1.0.1
```

Please refer Adafruit site - https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython

```pi@raspi400:~/ $ sudo mkdir Programs
pi@raspi400:~/ $ cd Programs
pi@raspi400:~/Programs $ sudo vi neopixels.py

pi@raspi400:~/Programs $ sudo python3 neopixel_simpletest.py

pi@raspi400:~/Programs $ sudo python3 neopixel_keys.py 
Red!
Green!
Blue!
Zoom!
Rainbow colors!
Program Ended
```

