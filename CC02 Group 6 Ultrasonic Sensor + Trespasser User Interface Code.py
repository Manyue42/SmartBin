# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:21:09 2017

@author: Zhang Manyu
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from firebase import firebase
import RPi.GPIO as GPIO                    # Import GPIO library
import time                                # Import time library
GPIO.setmode(GPIO.BCM)                     # Set GPIO pin numbering 
from RPi import GPIO

url = "https://smart-bin-7a6bc.firebaseio.com/" # URL to Firebase database
token = "i0MaJXzmWD9HRFDi67bHmMCP4Bf0PEKRLG1ziVCO" # unique token used for authentication
firebase=firebase.FirebaseApplication(url,token)

TRIG = 23                                  # Associate pin 23 to TRIG
ECHO = 24                                  # Associate pin 24 to ECHO

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                  # Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   # Set pin as GPIO in

def read_level(): 
    while True:
        GPIO.output(TRIG, False)                   # Set TRIG as LOW
        print "Waitng For Sensor To Settle"
        time.sleep(2)                              # Delay of 2 seconds
        GPIO.output(TRIG, True)                    # Set TRIG as HIGH
        time.sleep(2)                              # Delay of 2 seconds
        GPIO.output(TRIG, False)                   # Set TRIG as LOW
        while GPIO.input(ECHO)==0:                 # Check whether the ECHO is LOW
            pulse_start = time.time()              # Saves the last known time of LOW pulse 
        while GPIO.input(ECHO)==1:                 # Check whether the ECHO is HIGH    
            pulse_end = time.time()                # Saves the last known time of HIGH pulse
        pulse_duration = pulse_end - pulse_start   # Get pulse duration to a variable
        distance = pulse_duration * 17150          # Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)              # Round to two decimal points\
        percentage = ((23.5-(distance-3.5))/23.5)*100.0 # Convert the distance to percentage
        firebase.put('/B1L3A')                     # Update the current status of the bin to firebase
        if percentage > 100:                       # When the bin is more than 100% full, display the percentage as 100% instead of greater than 100
            percentage = 100
        if distance >= 26:                         # Initialize the dustbin level when it is empty
            percentage = 0
        if distance > 2 and distance < 400:        # Check whether the distance is within range
             print "Distance:",distance - 0.5,"cm" # Print distance with 0.5 cm calibration
        else:
            print "Out Of Range"
        return percentage


class MenuScreen(App):
    
    def build(self):
        self.layout = FloatLayout()
        with self.layout.canvas.before:        # Adding background to the layout
            Color(0.784,0.878,0.984,1)
            self.layout.rect = Rectangle(size = (800,540),post = self.layout.pos)
        
        # Logo
        self.image0 = Image(source = 'logo.png',pos=(-230,270))
        
        # Adding labels and images
        self.label1 = Label(text = "[b]Bin NO:[/b]"+"\n"+"1.3A", markup=True, color = (0,0,0,1), font_size =32, pos = (-240,0))
        self.label2 = Label(text = "[b]Building 1 Level 3[/b]",markup=True, color = (0,0,0,1), font_size = 36,pos = (230,200))
        self.label3 = Label(text = '0 %', color = (0,1,0,1), font_size = 40, pos = (20,-220))
        self.image1 = Image(source = 'happydust bin.png')
        self.image2 = Image(source = 'saddustbin.png')
        self.image3 = Image(source = 'filleddustbin1.png')
        self.image4 = Image(source = 'shocking-bubble1.png', pos = (250,-100))
        self.image5 = Image(source = 'happy-bubble1.png', pos = (240,0))
        self.image6 = Image(source = 'sad-bubble1.png', pos = (240,0))
        
        # Adding a quit button so that app can be closed
        self.quitbutton = Button(text = 'Quit', size_hint = (0.1,0.1), font_size = 24, pos = (100,120),on_press = self.quit_app)
        
        # Add widget to the layout
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.image1)
        self.layout.add_widget(self.image5)
        self.layout.add_widget(self.image0)
        self.layout.add_widget(self.quitbutton)

        # for the values to be updated every 0.1min
        Clock.schedule_interval(self.update, 2)      
                             
        return self.layout
        
    def update(self,instance):
        binstatus = read_level()                            # Update the current bin status to the app
        self.label3.text = str(round(binstatus,1)) + " %"   # Update the label3
        
        # Display different image for different bin status
        if float(binstatus) < 50:
            # Remove all the widget(images) before adding new images
            self.layout.remove_widget(self.image1)
            self.layout.remove_widget(self.image2)
            self.layout.remove_widget(self.image3)
            self.layout.remove_widget(self.image4)
            self.layout.remove_widget(self.image5)
            self.layout.remove_widget(self.image6)
            # Change the label color
            self.label3.color=(0,1,0,1)
            # Add new widget(images)
            self.layout.add_widget(self.image1)
            self.layout.add_widget(self.image5)
            
        elif 50 <= float(binstatus) < 80:
            # Remove all the widget(images) before adding new images
            self.layout.remove_widget(self.image1)
            self.layout.remove_widget(self.image2)
            self.layout.remove_widget(self.image3)
            self.layout.remove_widget(self.image4)
            self.layout.remove_widget(self.image5)
            self.layout.remove_widget(self.image6)
            # Change the label color
            self.label3.color = (1,0.549,0,1)
            # Add new widget(images)
            self.layout.add_widget(self.image2)
            self.layout.add_widget(self.image6)
            
        elif float(binstatus) >= 80:
            # Remove all the widget(images) before adding new images
            self.layout.remove_widget(self.image1)
            self.layout.remove_widget(self.image2)
            self.layout.remove_widget(self.image3)
            self.layout.remove_widget(self.image4)
            self.layout.remove_widget(self.image5)
            self.layout.remove_widget(self.image6)
            # Change the label color
            self.label3.color = (1,0,0,1)
            # Add new widget(images)
            self.layout.add_widget(self.image3)
            self.layout.add_widget(self.image4)
                
    def quit_app(self, value):  # Quit app function
        App.get_running_app().stop()

# Running the app
myapp=MenuScreen()
myapp.run()
