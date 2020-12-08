# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:21:09 2017

@author: Zhang Manyu
"""

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
from RPi import GPIO
from firebase import firebase
from kivy.clock import Clock
from kivy.uix.popup import Popup 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.button import Button 

url = "https://smart-bin-7a6bc.firebaseio.com/" # URL to Firebase database
token = "i0MaJXzmWD9HRFDi67bHmMCP4Bf0PEKRLG1ziVCO" # unique token used for authentication

firebase=firebase.FirebaseApplication(url,token)

TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

class LevelSensor(sm.SM):
    def read_level():
        while True:
            GPIO.output(TRIG, False)                 #Set TRIG as LOW
            print "Waitng For Sensor To Settle"
            time.sleep(2)                            #Delay of 2 seconds
            GPIO.output(TRIG, True)                  #Set TRIG as HIGH
            time.sleep(0.00001)                      #Delay of 0.00001 seconds
            GPIO.output(TRIG, False)                 #Set TRIG as LOW
            while GPIO.input(ECHO)==0:　　　　　　　　　　　#Check whether the ECHO is LOW
                pulse_start = time.time()              #Saves the last known time of LOW pulse
            while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
      　　　　　    pulse_end = time.time()                #Saves the last known time of HIGH pulse 
　　　　　　    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
      
          　distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  　　　　    distance = round(distance, 2)            #Round to two decimal points
  
  
  　　　　    percentage = ((40-distance)/40.0)*100
  　　　　    firebase.put('/','B1L3A',percentage)           
  　　　　
  
  　　　　    if distance > 2 and distance < 400:      #Check whether the distance is within range
      　　 　   print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    　　　    else:
    　　　　    　print "Out Of Range"                   #display out of range
        return percentage
      
      
class SmartBin(App):                                                      
    def build(self):
        self.layout = GridLayout(cols=2)    
        Clock.schedule_interval(self.callback,0.1)                             #for the values to be updated every 0.1min
        #self.st = Label(text='Sensored height of dustbin:',color=(1,0,0,1),font_size=24,halign='left',valign='middle')
        #self.svalue = TextInput(text='enter the height of your dustbin',font_size = 20)
        #self.ch = Label(text='Current level of dustbin', color=(1,0,0,1),font_size=24, halign='left',valign='middle')
        self.clevel = Label(text='0.0',font_size=24)
        self.level = Label(text = 'Level of dustbin',color=(0,1,0,1),font_size=24,halign='left',valign='middle')
        self.levelvalue = Label(text = '0.0' + ' %', font_size = 24)
        #self.button = Button(text='Calculate')
        
        #self.layout.add_widget(self.st)
        #self.layout.add_widget(self.svalue)
        #self.layout.add_widget(self.ch)
        self.layout.add_widget(self.clevel)
        self.layout.add_widget(self.level)
        self.layout.add_widget(self.levelvalue)
        #self.layout.add_widget(self.button)
        #self.button.bind(on_press=self.Calculate)
        
        Clock.schedule_interval(self.popup,10)

        return self.layout 
        
    #def update(self, instance):                                               
     #   st = float(self.svalue.text)
     #   self.svalue.text = str(st)
     ##   ch = float(self.clevel.text)
      #  self.clevel.text = str(ch)
    
    #def Calculate(self,instance):
        #dustbin= float(self.svalue.text)
     #   sensored = float(self.clevel.text)
     #   p = (40-sensored)/dustbin*100.0
     #   self.levelvalue.text = str(p)
     #   return self.levelvalue
         
        
    def popup(self,levelvalue):
        if float(self.levelvalue.text.strip(' %')) > 80.0:
            popup = Popup(title='Warning',content=Label(text='Dustbin is almost full, please drop your rubish to other bins!'),
                          size_hint=(None, None), size=(40, 40))
            popup.open()
        if float(self.levelvalue.tex.strip(' %')t) < 70.0:
            popup = Popup(title='Test popup',content=Label(text='Have a nice day!'),size_hint=(None, None), size=(40, 40))
            popup.open()
            
    def callback(self,value):                                                  #function to callback output values from Controller
        rL=read_level()
        self.levelvalue.text = str(rL.step(float(self.levelvalue.text))) + ' %' 
            
SmartBin().run()