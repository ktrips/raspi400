#!/bin/bash --rcfile

export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/RaspberryAi-fe5c92410ba3.json
echo "Applied Vision certificate."

aplay /home/pi/Programs/vision.wav

echo "Run Google Vision!"
cd /home/pi/Programs/
python3 detect_camera.py faces

echo "Completed Google Vision!"
