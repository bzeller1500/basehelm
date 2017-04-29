
import Tkinter as tk
from picamera import PiCamera
#camera = PiCamera()
#destination = '/home/pi/FTP/videos'
#import os
#import datetime as dt
#import RPi.GPIO as gpio
#filename = os.path.join(destination, dt,date.now().strftime('%Y_%m_%d.h264'))
#camera.start_recording(filename)
gpio.setmode(gpio.BCM)      #setting up gpio pins in BCM format
gpio.setup(21, gpio.OUT)    #bcm port 21 as output this is the last pin
                            #on the outside of the board closest to the
                            #usb and ethernet ports 

import serial
uni = u'\u2B05'
current_direction = 0       #set this later to equal the direction given
                            #from the rfcomm slot

root = tk.Tk()
root.configure(background = 'black')
#root.overrideredirect(True) # uncomment this line for true fullscreen effect
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
svar = tk.StringVar()
labl=tk.Label(root,textvariable=svar,fg='white',bg='black')

ser = serial.Serial('/dev/rfcomm0',9600) # build up the serial interpreter
def setforward():
    global uni
    uni = u'\u2B05'

def setright():
    global uni
    uni = u'\u2B07'

def setleft():
    global uni
    uni = u'\u2B06

def nodir():
    global uni
    uni = u'\u2974'          #with the orientation of the helm this is
                             #backwards

def pulldir():
    global current_direction #again we need to set this later to
                             # the appropriate string from the
                             # rfcomm slot as well as the conditions
    global root
    cmd = ser.readline();    # read full line of instruction from bt com 
    d1 = cmd.split(',')
    current_direction = d1[1] # set new current direction 
    #if current_direction == :
    #    setforward()
    if current_direction == 'right':
        setright()
    if current_direction == 'left':
        setleft()
    else:                    # default case in the event that there is 
        setforward()         # no direction given
    svar.set(uni)
    root.after(2000,pulldir) # this pulls the directions continuously
                             # and continuously enforces the program to
                             # pull directions from rfcomm (once enabled)
                             # every 2000 units (thought they were seconds)
                             # but apparently not

def pullsettings():
    global labl
    settings = ser.readline();
    individual_settings = settings.split(',')
    if individual_settings[1] == 'true':
        gpio.output(21, gpio.HIGH)      #initiate slave recording
        camera.start_recording(filename)#initiate secondary cam rec
    if individual_settings[2] == 'true':
        tk.Label(root,fg='black')   #not sure if this is going to work
        #root.quit
        #build new root w/ all black
    if individual_settings[3] == 'true':
        root.after(2000,pulldir)
    if individual_settings[4] == 'true':
        #build spedometer
            

def build():
    global root
    global svar
    root.configure(background='black')
    #labl=tk.Label(root,textvariable=svar,fg='white',bg='black')
    root.after(20000,pullsettings) # pulls immediate direction
    svar.set(uni)
    labl.config(font=("Times",500,"bold"))
    labl.pack()
    root.mainloop()          # builds the main screen and brings about
                             # then initial loop
                             

