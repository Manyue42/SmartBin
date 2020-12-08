from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from firebase import firebase

url = "https://smart-bin-7a6bc.firebaseio.com/" # URL to Firebase database
token = "i0MaJXzmWD9HRFDi67bHmMCP4Bf0PEKRLG1ziVCO" # unique token used for authentication
firebase=firebase.FirebaseApplication(url,token)

class B1L3(Screen): # Building 1 Level 3
           
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = FloatLayout()
        
        # Mapping of the Dustbin
        self.label2 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-260,54))
        self.label3 = Label(text='1.3A (1%)', color=(0,0,1,1), font_size=18, pos=(-260,-1))
        self.label4 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-185,70))
        self.label5 = Label(text='1.3B (1%)', color=(0,0,1,1), font_size=18, pos=(-185,15))
        self.label6 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-45,-100))
        self.label7 = Label(text='1.3C (1%)', color=(0,0,1,1), font_size=18, pos=(-45,-155))
       
        # Floor Plan and Slide Detection
        self.image1 = Image(source='Building1.png')
        self.image1.bind(on_touch_move=self.detect)
        
        # Add Widget
        self.layout.add_widget(self.image1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.label4)
        self.layout.add_widget(self.label5)
        self.layout.add_widget(self.label6)
        self.layout.add_widget(self.label7)
        
        self.add_widget(self.layout)
    

    def detect(self, instance, touch): 
        if touch.dy<-20: # Slide down to Building 2 Level 3
            self.manager.transition.direction = 'down'
            self.manager.current= 'B2L3'
            
        if touch.dx<-20: # Slide to left to Building 1 Level 4
            self.manager.transition.direction = 'left'
            self.manager.current= 'B1L4'
            
            

class B1L4(Screen): # Building 1 Level 4
           
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = FloatLayout()
        
        # Mapping of the Dustbin
        self.label2 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-260,54))
        self.label3 = Label(text='1.4A (1%)', color=(0,0,1,1), font_size=18, pos=(-260,-1))
        self.label4 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-185,70))
        self.label5 = Label(text='1.4B (1%)', color=(0,0,1,1), font_size=18, pos=(-185,15))
        self.label6 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-45,-100))
        self.label7 = Label(text='1.4C (1%)', color=(0,0,1,1), font_size=18, pos=(-45,-155))
        
        # Floor Plan and Slide Detection
        self.image1 = Image(source='Building1.png')
        self.image1.bind(on_touch_move=self.detect)
        
        # Add Widget
        self.layout.add_widget(self.image1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.label4)
        self.layout.add_widget(self.label5)
        self.layout.add_widget(self.label6)
        self.layout.add_widget(self.label7)

        self.add_widget(self.layout)
                
    def detect(self, instance, touch):
        if touch.dx>20: # Slide to right to Building 1 Level 3
            self.manager.transition.direction = 'right'
            self.manager.current= 'B1L3'
            
                     
class B2L3(Screen): #Building 2 Level 3
           
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = FloatLayout()
        
        # Mapping of the Dustbin
        self.label2 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-220,30))
        self.label3 = Label(text='2.3A (1%)', color=(0,0,1,1), font_size=18, pos=(-220,-25))
        self.label4 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-60,55))
        self.label5 = Label(text='2.3B (1%)', color=(0,0,1,1), font_size=18, pos=(-60,0))
        self.label6 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(180,95))
        self.label7 = Label(text='2.3C (1%)', color=(0,0,1,1), font_size=18, pos=(180,40))
        self.label8 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-180,-80))
        self.label9 = Label(text='2.3D (1%)', color=(0,0,1,1), font_size=18, pos=(-180,-135))
        self.label10 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(-55,-75))
        self.label11 = Label(text='2.3E (1%)', color=(0,0,1,1), font_size=18, pos=(-55,-130))
        self.label12 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(55,-125))
        self.label13 = Label(text='2.3F (1%)', color=(0,0,1,1), font_size=18, pos=(55,-180))
        self.label14 = Label(text='.', color=(0,0,1,1), font_size=100, pos=(250,-80))
        self.label15 = Label(text='2.3G (1%)', color=(0,0,1,1), font_size=18, pos=(250,-135))
        
        # Floor Plan and Slide Detection
        self.image1 = Image(source='Building2.png')
        self.image1.bind(on_touch_move=self.detect)
        
        # Add Widget
        self.layout.add_widget(self.image1)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.label4)
        self.layout.add_widget(self.label5)
        self.layout.add_widget(self.label6)
        self.layout.add_widget(self.label7)
        self.layout.add_widget(self.label8)
        self.layout.add_widget(self.label9)
        self.layout.add_widget(self.label10)
        self.layout.add_widget(self.label11)
        self.layout.add_widget(self.label12)
        self.layout.add_widget(self.label13)
        self.layout.add_widget(self.label14)
        self.layout.add_widget(self.label15)
        
        self.add_widget(self.layout)
        
        
    def detect(self, instance, touch):
        if touch.dy>20: # Slide up to Building 1 Level 3
            self.manager.transition.direction = 'up'
            self.manager.current= 'B1L3'
            
      
class MyApp(App): # Compiling all the screens into an app
    def build(self):
        self.layout = FloatLayout()
        with self.layout.canvas.before: # Changing the background of the layout
            Color(0.784,0.878,0.984,1)
            self.layout.rect = Rectangle(size = (800,540),post = self.layout.pos)
        
        # Logo
        self.image2 = Image(source = 'logo.png',pos=(-230,270))
        
        # Dropdown List
        self.dropdown = DropDown()
        self.button1 = Button(text = 'Building 1 Level 3',size_hint_x = 0.5,size_hint_y=None,height = 40,on_release=self.change_to_building,font_size = 20)
        self.button2 = Button(text = 'Building 1 Level 4',size_hint_x = 0.5,size_hint_y=None,height = 40,on_release=self.change_to_building,font_size = 20)
        self.button3 = Button(text = 'Building 2 Level 3',size_hint_x = 0.5,size_hint_y=None,height = 40,on_release=self.change_to_building,font_size = 20)

        self.dropdown.add_widget(self.button1)
        self.dropdown.add_widget(self.button2)
        self.dropdown.add_widget(self.button3)
        self.mainbutton = Button(text = 'Building 1 Level 3', size_hint = (0.4,0.1), pos_hint = {'top':1,'right':1},on_release = self.dropdown.open,font_size = 20)
        
        # Pop-up Window
        self.box = BoxLayout(orientation = 'vertical')
        self.content1 = Label(text = 'Bin 1.3A is almost full!', font_size = 20)
        self.content2 = Button(text = 'Noted!',size_hint = (1, 0.3),state = 'normal')
            
        self.box.add_widget(self.content1)
        self.box.add_widget(self.content2)
            
        self.popup = Popup(title = 'Notification',content = self.box, auto_dismiss = True, size_hint = (0.4,0.4),title_size = 25)
        self.content2.bind(on_press = self.close)
        
        # Screen Manager
        self.sm=ScreenManager()
        self.b1l3=B1L3(name='B1L3')
        self.b1l4=B1L4(name='B1L4')
        self.b2l3=B2L3(name='B2L3')
        self.sm.add_widget(self.b1l3)
        self.sm.add_widget(self.b1l4)
        self.sm.add_widget(self.b2l3)
        self.sm.current='B1L3'
        
        # Add widget to the layout
        self.layout.add_widget(self.sm)
        self.layout.add_widget(self.mainbutton)
        self.layout.add_widget(self.image2)
        
        # Update the percentage in the text label
        Clock.schedule_interval(self.callback_B1L3A, 10)
        Clock.schedule_interval(self.callback_B1L3B, 0.2)
        Clock.schedule_interval(self.callback_B1L3C, 0.15)
        
        Clock.schedule_interval(self.callback_B1L4A, 0.2)
        Clock.schedule_interval(self.callback_B1L4B, 0.15)
        Clock.schedule_interval(self.callback_B1L4C, 0.1)
        
        Clock.schedule_interval(self.callback_B2L3A, 0.25)
        Clock.schedule_interval(self.callback_B2L3B, 0.2)
        Clock.schedule_interval(self.callback_B2L3C, 0.1)
        Clock.schedule_interval(self.callback_B2L3D, 0.15)
        Clock.schedule_interval(self.callback_B2L3E, 0.1)
        Clock.schedule_interval(self.callback_B2L3F, 0.15)
        Clock.schedule_interval(self.callback_B2L3G, 0.07)
        
        Clock.schedule_interval(self.blink_B1L3A, 0.5)
        Clock.schedule_interval(self.blink_B1L3B, 0.5)
        Clock.schedule_interval(self.blink_B1L3C, 0.5)
        
        Clock.schedule_interval(self.blink_B1L4A, 0.5)
        Clock.schedule_interval(self.blink_B1L4B, 0.5)
        Clock.schedule_interval(self.blink_B1L4C, 0.5)
        
        Clock.schedule_interval(self.blink_B2L3A, 0.5)
        Clock.schedule_interval(self.blink_B2L3B, 0.5)
        Clock.schedule_interval(self.blink_B2L3C, 0.5)
        Clock.schedule_interval(self.blink_B2L3D, 0.5)
        Clock.schedule_interval(self.blink_B2L3E, 0.5)
        Clock.schedule_interval(self.blink_B2L3F, 0.5)
        Clock.schedule_interval(self.blink_B2L3G, 0.5)
        
        # Update the status of bin 1.3A every 10 second from firebase
        Clock.schedule_interval(self.callback_popup, 10)

        return self.layout
        
    def close(self,instance): # Close Button for Pop-up Window
        if self.content2.state == 'down':
            self.popup.dismiss()
            self.layout.remove_widget(self.popup)
            self.content2.state = 'normal'
            
    def callback_popup(self,instance): # Call the pop-up window and get status of bin 1.3A from firebase
        binlist = firebase.get('/B1L3A')
        if float(binlist) >= 80: # If the bin is 80% full, then notification will pop up to notify the cleaner to clean it
            self.content1.text = "Bin B1L3A is almost full!" 
            self.popup.open()
        elif self.content2.state == 'down':
            self.popup.dismiss()
            self.layout.remove_widget(self.popup)
            self.content2.state = 'normal'


    def change_to_building(self,value): # Floor Selection for Dropdown List
        if value.text == 'Building 1 Level 3':
            self.mainbutton.text = 'Building 1 Level 3'
            self.sm.transition.direction = 'right'
            self.sm.current = 'B1L3'
        elif value.text == 'Building 1 Level 4':
            self.mainbutton.text = 'Building 1 Level 4'
            self.sm.transition.direction = 'left'
            self.sm.current = 'B1L4'
        elif value.text == 'Building 2 Level 3':
            self.mainbutton.text = 'Building 2 Level 3'
            self.sm.transition.direction = 'down'
            self.sm.current = 'B2L3'
        
    def status(self, label1, label2): # Read the percentage in the text label and increase it by one
        number = ''
        state = 0
        prefix = label2.text[0:6]
        for i in label2.text:
            if i == '%':
                state = 0
            if state == 1:
                number += i
            if i == '(':
                state = 1
        number = int(number) + 1
        if number <= 100:
            if number >= 80:
                label1.color = (1,0,0,1)
                label2.color = (1,0,0,1)
            elif number < 80:
                label1.color = (0,0,1,1)
                label2.color = (0,0,1,1)
            label2.text = prefix + str(number) + '%)'
        return number
        
    # Building 1 Level 3, update the status of the bins in this floor
    def callback_B1L3A(self,dt):
        B1L3A = firebase.get('/B1L3A')
        B1L3A = round(B1L3A, 1)
        if B1L3A >= 80:
            self.b1l3.label3.color = (1,0,0,1)
            self.b1l3.label2.color = (1,0,0,1)
        self.b1l3.label3.text = '1.3A (' + str(B1L3A) + '%)'
        
    def callback_B1L3B(self,dt):
        self.status(self.b1l3.label4, self.b1l3.label5)
    def callback_B1L3C(self,dt):
        self.status(self.b1l3.label6, self.b1l3.label7)
        
    # Building 1 Level 4, update the status of the bins in this floor
    def callback_B1L4A(self,dt):
        self.status(self.b1l4.label2, self.b1l4.label3)
    def callback_B1L4B(self,dt):
        self.status(self.b1l4.label4, self.b1l4.label5)
    def callback_B1L4C(self,dt):
        self.status(self.b1l4.label6, self.b1l4.label7)
        
    # Building 2 Level 3, update the status of the bins in this floor
    def callback_B2L3A(self,dt):
        self.status(self.b2l3.label2, self.b2l3.label3)
    def callback_B2L3B(self,dt):
        self.status(self.b2l3.label4, self.b2l3.label5)
    def callback_B2L3C(self,dt):
        self.status(self.b2l3.label6, self.b2l3.label7)
    def callback_B2L3D(self,dt):
        self.status(self.b2l3.label8, self.b2l3.label9)
    def callback_B2L3E(self,dt):
        self.status(self.b2l3.label10, self.b2l3.label11)
    def callback_B2L3F(self,dt):
        self.status(self.b2l3.label12, self.b2l3.label13)
    def callback_B2L3G(self,dt):
        self.status(self.b2l3.label14, self.b2l3.label15)
        
    def blink(self,label1,label2): # Blink when the percentage is 100% 
        number = self.status(label1, label2)
        if number == 101:
            pos_x = label1.pos[0]
            pos_y = label1.pos[1]
            length = len(str(pos_x))
            if length > 4:
                label1.pos = (pos_x+10000,pos_y)
                label2.pos = (pos_x+10000,pos_y-55)
            else:
                label1.pos = (pos_x-10000,pos_y)
                label2.pos = (pos_x-10000,pos_y-55)
    
    # Make dustbin blink when it is 100% full
    def blink_B1L3A(self,dt):
        pass
    def blink_B1L3B(self,dt):
        self.blink(self.b1l3.label4, self.b1l3.label5)
    def blink_B1L3C(self,dt):
        self.blink(self.b1l3.label6, self.b1l3.label7)
        
    def blink_B1L4A(self,dt):
        self.blink(self.b1l4.label2, self.b1l4.label3)
    def blink_B1L4B(self,dt):
        self.blink(self.b1l4.label4, self.b1l4.label5)
    def blink_B1L4C(self,dt):
        self.blink(self.b1l4.label6, self.b1l4.label7)
        
    def blink_B2L3A(self,dt):
        self.blink(self.b2l3.label2, self.b2l3.label3)
    def blink_B2L3B(self,dt):
        self.blink(self.b2l3.label4, self.b2l3.label5)
    def blink_B2L3C(self,dt):
        self.blink(self.b2l3.label6, self.b2l3.label7)
    def blink_B2L3D(self,dt):
        self.blink(self.b2l3.label8, self.b2l3.label9)
    def blink_B2L3E(self,dt):
        self.blink(self.b2l3.label10, self.b2l3.label11)
    def blink_B2L3F(self,dt):
        self.blink(self.b2l3.label12, self.b2l3.label13)
    def blink_B2L3G(self,dt):
        self.blink(self.b2l3.label14, self.b2l3.label15)
        
# Run the app 
if __name__=='__main__':
    MyApp().run()
    
print "Hellow World"