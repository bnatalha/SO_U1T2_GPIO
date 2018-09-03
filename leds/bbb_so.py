"""
" @authors Josivan Medeiros and Natália Azevedo
"""
import subprocess   # for .sh like command call
#import os.system   # for system(cmd) 

def bash_command(cmd):
   subprocess.Popen(['/bin/bash', '-c', cmd])

class GPIO:
    leddir = "/sys/class/gpio/"

    def __init__(self, name, gpiodir):
        self.name = name
        self.gpiodir = gpiodir
        self.dirc_path = self.leddir + gpiodir + "/direction"
        self.val_path = self.leddir + gpiodir + "/value"

    def echo_comm(self, arg1, arg2):
        cmd = ("sudo echo " + arg1 + " > " + arg2)
        bash_command(cmd)
        # test: 
        #print(cmd)
        # se fez import os.system:
            #os.system(cmd)

    def set_val(self, val):
        self.echo_comm(val, self.val_path)

    def get_val(self):
        #self.echo_comm(val, self.val_path)
        f = open(self.val_path)
        val = f.read()
        f.close()
        return val
    
    def set_dirc(self, dirc):
        self.echo_comm(dirc, self.dirc_path)

