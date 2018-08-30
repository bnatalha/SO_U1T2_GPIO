"""
" @authors Josivan Medeiros and Natália Azevedo
"""
import time

GPIO = '/sys/class/gpio/'
RED_LED = 'gpio68/'
GREEN_LED = 'gpio69/'
YELLOW_LED = 'gpio67/'

# Opening the pins files and stat
f_stat = open('/proc/stat', 'r')
GREEN_DIR = open(GPIO+GREEN_LED+'direction', 'w')
GREEN_VL = open(GPIO+GREEN_LED+'value', 'w')
RED_DIR = open(GPIO+RED_LED+'direction', 'w')
RED_VL = open(GPIO+RED_LED+'value', 'w')
YELLOW_DIR = open(GPIO+YELLOW_LED+'direction', 'w')
YELLOW_VL = open(GPIO+YELLOW_LED+'value', 'w')

# Setting pins as output
GREEN_DIR.write('out')
RED_DIR.write('out')
YELLOW_DIR.write('out')
#GREEN_DIR.close()
#RED_DIR.close()
#YELLOW_DIR.close()

# Reading status
while(True):
    stat = f_stat.read().split()
    if (len(stat) > 5):
        system_cpu = int(stat[3])
        user_cpu = int(stat[1]) 
        idle_cpu = int(stat[4])
        total_cpu = user_cpu + system_cpu + idle_cpu
    perc = (user_cpu + system_cpu)/total_cpu
    print(perc)
    if (perc < 0.25):
        GREEN_VL.write('1')
        RED_VL.write('0')
        YELLOW_VL.write('0')
    elif (perc < 0.5):
        GREEN_VL.write('0')
        RED_VL.write('0')
        YELLOW_VL.write('1')
    elif (perc < 0.75):
        GREEN_VL.write('0')
        RED_VL.write('1')
        YELLOW_VL.write('0')
    
    time.sleep(1)



