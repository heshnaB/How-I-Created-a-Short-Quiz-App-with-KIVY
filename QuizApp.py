#In Progress

'''
Author: Heshna Bhagawan
Project: Building a quiz app that helps you decide what to eat.
Ref: 
- https://levelup.gitconnected.com/create-your-app-with-flutter-in-5-days-412ee41de22a
-If you need help with installing Android IOS Emulator: https://www.geeksforgeeks.org/how-to-set-up-an-emulator-for-vscode/
- https://kivy.org/doc/stable/guide/widgets.html
- https://www.section.io/engineering-education/kivy-python-first-app/
'''

# Please install the library if you dont have it by entering this in the command prompt: pip install kivy

# Now we have to import the libraries for the app
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Now we will open the file with the list of places and convert it into a list.
p = open("Places.txt"); places = []; [places.append(i.strip()) for i in p]

# Split the list into the categories drive thru and deliver.
drive_thru = places[0:6]; deliver = places[6:-1]

class QuizApp(App):
    
    def build(self):
        self.window = GridLayout()
        # self.window.cols = 1
        # self.window.add_widget(Image(source("logo.png")))
        
    #return self.window

if __name__ == "__main__":
    QuizApp().run()
    

    
#     def build(self):
#         return Label(text="Are you too lazy to cook but you want to eat?")

# QuizApp().run()





    