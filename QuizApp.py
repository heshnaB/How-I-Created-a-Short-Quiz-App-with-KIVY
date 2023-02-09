#In Progress

'''
Author: Heshna Bhagawan
Project: Building a quiz app that helps you decide what to eat.
Ref: 
- https://levelup.gitconnected.com/create-your-app-with-flutter-in-5-days-412ee41de22a
-If you need help with installing Android IOS Emulator: https://www.geeksforgeeks.org/how-to-set-up-an-emulator-for-vscode/
- https://kivy.org/doc/stable/guide/widgets.html
- https://www.section.io/engineering-education/kivy-python-first-app/
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

# Split the list into the categories drive thru and deliver.
drive_thru = places[0:6]; deliver = places[6:-1]



class QuizApp(App):
    
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.add_widget(Image(source="logo.png"))
        
        self.ageRequest = Label(
            text = "Are you ready to decide what to eat?",
            font_size = 45,
            color = "#FFFFFF",
            bold = True
        )
        
        self.window.add_widget(self.ageRequest)
        
        # self.date = TextInput(
        #     multiline = False,
        #     padding_y = (30,30),
        #     size_hint = (1,0.7),
        #     font_size = 30
        # )
        
        # self.window.add_widget(self.date)
        
        self.button = Button(
            text = "YES, I'M STARVING!!",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        
        self.button.bind(on_press = self.q_1)
        self.window.add_widget(self.button)
        
        return self.window
    
    def q_1(self, event):
        today = datetime.today().year
        dob = self.date.text
        age = int(today) - int(dob)
        self.ageRequest.text = "You are " + str(int(age)) + " years old"
        
    # def getAge(self, event):
    #     today = datetime.today().year
    #     dob = self.date.text
    #     age = int(today) - int(dob)
    #     self.ageRequest.text = "You are " + str(int(age)) + " years old"

if __name__ == "__main__":
    QuizApp().run()





    