"""
" @authors Josivan Medeiros and Natália Azevedo
"""

import subprocess
import time # for sleep
import threading # for paralellism
import bbb_so as bbb # for gpio class

#GPIO_DIR = "/sys/class/gpio/"
UPDATE_DIRECTION = True
USAGE75 = 75

# P9 setup:
# DGND      1|2    DGND
# MMC       3|4    MMC...
# MMC       5|6    MMC...
# GPIO66    7|8    GPIO67
# GPIO69    9|10   GPIO68
# GPIO45    11|12   GPIO44

def switch_leds(leds_l, val):
    for led in leds_l:
        led.set_val(val)

def single_led_on(leds_l, xled):
    for led in leds_l:
        if led == xled:
            led.set_val("1")
        else:
            led.set_val("0")
# -------------------------------

def semaforo(leds_):
    def blink_all(leds_l):
        while PANIC_MODE.is_set() == True:
            time.sleep(1)
            switch_leds(leds_l,"1") #turn on
            time.sleep(seconds)
            switch_leds(leds_l,"0") #turn off
            time.sleep(seconds)
    
    def read_usage():
        p = subprocess.call(['./information'])
        #f = open("percent.out","r")
        #p = int(f.read())
        #f.close()
        return p

    while RUNNING.is_set():
        usage = read_usage()
        if usage < 25: #green
            single_led_on(leds_, leds_[0])
        elif usage < 50: #yellow
            single_led_on(leds_, leds_[1])
        elif usage < 75: #red
            single_led_on(leds_, leds_[2])
        else: #blink_all
            print("panic!!!")
            blink_all(leds_)
            PANIC_MODE.set()

def defuser():
    print("#defusing the forkbomb...")
    subprocess.call(['./antiforkbomb.sh'])
    time.sleep(5)
    print("#done defusing.")

def supervise():
    while RUNNING.is_set():
        time.sleep(1)
        #read measure
        if PANIC_MODE.is_set():
            #call defuser
            defuser()
            PANIC_MODE.clear()
            print("no more panic.")

print("# setting leds")
g = bbb.GPIO("green_led", "gpio67")
y = bbb.GPIO("yellow_led", "gpio68")
r = bbb.GPIO("red_led", "gpio69")
leds = [g, y, r]

print("# setting pb")
pb = bbb.GPIO("push_button", "gpio44") 

seconds = .5 # sleep time

print("# setting directions for leds")
if (UPDATE_DIRECTION):
    for led in leds:
        led.set_dirc("out")

print("# setting events")
PANIC_MODE = threading.Event()
PANIC_MODE.clear()  #dont start at panic mode
RUNNING = threading.Event()
RUNNING.set()   #start running

print("# threads")
blinker = threading.Thread(target=semaforo, name="blinker", args=[leds], daemon=True)
superviser = threading.Thread(target=supervise, name="superviser", daemon=True)

blinker.start()
superviser.start()

print("# starting tests...")
time.sleep(30)
RUNNING.clear()

print("# finished running tests.")
blinker.join()
print("joined {}".format(blinker.name))
superviser.join()
print("joined {}".format(superviser.name))

print("# turn off everything before finishing")
switch_leds(leds,"0")
print("program finished.")
