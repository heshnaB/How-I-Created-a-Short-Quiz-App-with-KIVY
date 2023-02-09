#In Progress

'''
Author: Heshna Bhagawan
Project: Building a quiz app that helps you decide what to eat.
Ref: 
Doc for Kivy: https://kivy.org/doc/stable/guide/widgets.html
App Sample in Kivy: https://www.section.io/engineering-education/kivy-python-first-app/
- Color picker: https://htmlcolorcodes.com/
'''

# Please install the library if you dont have it by entering this in the command prompt: pip install kivy

# Now we have to import the libraries for the app
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime, date, time, timedelta


# Now we will open the file with the list of places and convert it into a list.
p = open("Places.txt"); places = []; [places.append(i.strip()) for i in p]
q = open("Questions.txt"); qs = [];  [qs.append(i.strip()) for i in q]

# Split the list into the categories drive thru and deliver.
drive_thru = places[0:6]; deliver = places[6:-1]


class QuizApp(App):
    
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.add_widget(Image(source="logo.png"))
        
        self.ready4Quiz = Label(
            text = "Are you ready to decide what to eat?",
            font_size = 45,
            color = "#FFFFFF",
            bold = True
        )
        
        self.window.add_widget(self.ready4Quiz)
        
        self.button = Button(
            text = "YES, I'M STARVING!!",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        self.window.add_widget(self.button)
        self.button.bind(on_press = self.beginQ)
        
        
        return self.window
    
    def beginQ(self, event):
        
        self.window.remove_widget(self.ready4Quiz)
        self.window.remove_widget(self.button)
        
        self.quest = Label(
            text = "Do you feel like driving?",
            font_size = 45,
            color = "#FFFFFF",
            bold = True
        )
        
        self.window.add_widget(self.quest)
        
        
        
        self.buttonY = Button(
            text = "Sure",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        
        
        self.buttonN = Button(
            text = "Absolutely Not!",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        
        
        self.buttonY.bind(on_press = self.yesoption)
        self.buttonN.bind(on_press = self.nooption)
        self.window.add_widget(self.buttonY)
        self.window.add_widget(self.buttonN)
        
        
        
    
        
        
        
    def yesoption(self, event):
        
        import random
        
        ans = str(random.choice(drive_thru))
        
        self.window.remove_widget(self.quest)
        self.window.remove_widget(self.buttonN)
        self.window.remove_widget(self.buttonY)
        
        self.ans = Label(
            text = f"Go for {ans}!",
            font_size = 45,
            color = "#FFFFFF",
            bold = True
        )
        
        self.window.add_widget(self.ans)
        
        
        
        
    
    def nooption(self, event):
        import random
        
        ans = str(random.choice(deliver))
        
        self.window.remove_widget(self.quest)
        self.window.remove_widget(self.buttonN)
        self.window.remove_widget(self.buttonY)
        
        self.ans = Label(
            text = f"Get {ans}!",
            font_size = 45,
            color = "#FFFFFF",
            bold = True
        )
        
        self.window.add_widget(self.ans)

if __name__ == "__main__":
    QuizApp().run()





    