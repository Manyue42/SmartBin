# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 17:42:01 2017

@author: LeeSei
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

url = "https://smart-bin-7a6bc.firebaseio.com/" # URL to Firebase database
token = "i0MaJXzmWD9HRFDi67bHmMCP4Bf0PEKRLG1ziVCO" # unique token used for authentication
firebase=firebase.FirebaseApplication(url,token)

class MenuScreen(App):
    
    def build(self):
        self.layout = FloatLayout()
        with self.layout.canvas.before:
            Color(0.784,0.878,0.984,1)
            self.layout.rect = Rectangle(size = (800,540),post = self.layout.pos)
        
        self.image0 = Image(source = 'logo.png',pos=(-230,270))
        
        self.label1 = Label(text = "[b]Bin NO:[/b]"+"\n"+"1.3A", markup=True, color = (0,0,0,1), font_size =32, pos = (-240,0))
        self.label2 = Label(text = "[b]Building 1 Level 3[/b]",markup=True, color = (0,0,0,1), font_size = 36,pos = (230,200))
        self.label3 = Label(text = '0 %', color = (0,1,0,1), font_size = 40, pos = (20,-220))
        self.image1 = Image(source = 'happydust bin.png')
        self.image2 = Image(source = 'saddustbin.png')
        self.image3 = Image(source = 'filleddustbin1.png')
        self.image4 = Image(source = 'shocking-bubble1.png', pos = (250,-100))
        self.image5 = Image(source = 'happy-bubble1.png', pos = (240,0))
        self.image6 = Image(source = 'sad-bubble1.png', pos = (240,0))
        
        self.quitbutton = Button(text = 'Quit', size_hint = (0.1,0.1), font_size = 24, pos = (100,120),on_press = self.quit_app)
        
        self.state = 0
        
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.image1)
        self.layout.add_widget(self.image5)
        self.layout.add_widget(self.image0)
        self.layout.add_widget(self.quitbutton)

       
        Clock.schedule_interval(self.update, 2)
       
        
        return self.layout
        
    def update(self,instance):
        binstatus = firebase.get('/B1L3A')
        self.label3.text = str(round(binstatus,1)) + " %"
        if float(binstatus) < 50:
            self.layout.remove_widget(self.image1)
            self.layout.remove_widget(self.image2)
            self.layout.remove_widget(self.image3)
            self.layout.remove_widget(self.image4)
            self.layout.remove_widget(self.image5)
            self.layout.remove_widget(self.image6)
            self.layout.add_widget(self.image1)
            self.layout.add_widget(self.image5)
            
        elif 50<= float(binstatus) < 80:
            self.layout.remove_widget(self.image1)
            self.layout.remove_widget(self.image2)
            self.layout.remove_widget(self.image3)
            self.layout.remove_widget(self.image4)
            self.layout.remove_widget(self.image5)
            self.layout.remove_widget(self.image6)
            self.label3.color = (1,0.549,0,1)
            self.layout.add_widget(self.image2)
            self.layout.add_widget(self.image6)
        
        elif float(binstatus) >= 80:
            self.layout.remove_widget(self.image1)
            self.layout.remove_widget(self.image2)
            self.layout.remove_widget(self.image3)
            self.layout.remove_widget(self.image4)
            self.layout.remove_widget(self.image5)
            self.layout.remove_widget(self.image6)
            self.label3.color = (1,0,0,1)
            self.layout.add_widget(self.image3)
            self.layout.add_widget(self.image4)
     
    def quit_app(self, value):
        App.get_running_app().stop()

myapp=MenuScreen()
myapp.run()