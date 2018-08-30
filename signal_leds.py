"""
" @authors Josivan Medeiros and Natália Azevedo
"""
import time

Y_DIR = open('/sys/class/gpio/gpio69/direction', 'w')
Y_DIR.write('out')

Y_VAL = open('/sys/class/gpio/gpio69/value', 'w')

while(True):
    Y_VAL.write('1')
    time.sleep(2)
