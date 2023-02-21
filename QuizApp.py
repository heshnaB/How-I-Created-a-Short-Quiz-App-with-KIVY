'''
Author: Heshna Bhagawan
Project: Build a quiz app that helps you decide what to eat. The code is designed to go in an infinite loop and won't close until the user closes the window.

References:
Doc for Kivy: https://kivy.org/doc/stable/guide/widgets.html
Other references:
- https://www.section.io/engineering-education/kivy-python-first-app/
- https://www.simplikivyapp.com/ - better for a longer quiz

- Color picker: https://htmlcolorcodes.com/
'''

# Step 1: Please install the library, if you don't have it, by entering this in the command prompt: pip install kivy

# Step 2: Import the following libraries
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
import random


# Step 3: Create a home screen for the app.
class Home(FloatLayout):

    def __init__(self, **kwargs):
        '''
        Purpose: Initiates the class
        '''
        
        # Sets up the app window
        super(Home, self).__init__(**kwargs)
        
        # Call the main_home function.        
        self.main_home()
        
        
    def logo(self):
        '''
        Purpose: Creates and displays the logo
        '''
        
        self.add_widget(Image(source="logo.png",
            size_hint = (0.3, 0.7),
            pos_hint={'center_x': 0.5, 'y': 0.355}))
    
     
    def main_home(self):
        '''
        Purpose: Creates the layout for the home screen
        '''
        
        # Since the code is a loop, we can use the line "self.clear_widgets" to clear the entire page before we add the home screen widgets.
        self.clear_widgets()
        
        # Creates the first question.
        self.add_label("Are you ready to decide what to eat?")
        
        self.button = self.add_button("Yes, I'm starving!", (0.9, 0.185), 0.1)
        
        
        # Display the logo
        self.logo()
        
        # Display the question and the button.
        self.add_widget(self.button)
        
    
    def add_label(self, string):
        self.add_widget(Label(
            text = string,
            font_size = 45,
            color = "#FFFFFF",
            bold = True,
            pos_hint={'x': 0.000000001, 'center_y': 0.4}
        ))
        
    def add_button(self, string, size, y):
        '''
        Purpose: Create and add the yes and no buttons.
        '''
        
        self.b = Button(
            text = string,
            size_hint = size,
            bold = True,
            font_size = 30,
            pos_hint={'center_x': 0.5, 'y': y},
        )
        
        return self.b

    def reset(self):
        '''
        Purpose: To remove all widgets except the logo.
        '''
        
        # Clears all the widgets and adds the logo.
        self.clear_widgets()
        self.logo()    
        
# Step 4: Creates the rest of the quiz layouts.
class QuizApp(App):
    
    def build(self):
        '''
        Initiates and builds the quiz.
        '''
        
        # Creates a variable for the Home() class.
        self.root = root = Home()
        
        # Calls the start() function.
        self.start(root)
    
    def display_result(self, root, result):
        
        self.root.reset()
        
        # Displays the result & the restart button to restart the quiz.
        self.root.add_label(result)
        self.restart_but = self.root.add_button("Restart", (0.9, 0.1), 0.18)
        self.root.add_widget(self.restart_but)
        
        # When the user presses on the restart button, the program calls the return_home() function.
        self.restart_but.bind(on_press= self.return_home)
        
        
    def option_n(self, root):
        '''
        Purpose: Displays the result if user picked "Absolutely Not!" and the "Restart" button.
        '''
        
        result = f"Get {random.choice(['Mikado', 'Edo Japan', 'Pizza Hut', 'Dominos', 'Swan Pizza' , 'Papa Johns Pizza', 'Pizza 73', 'Grain of Rice', 'Rice Bowl Deluxe'])}!"
        
        
        # Repetitive function
        
        self.display_result(root, result)
        
        
    
    def option_y(self, root):
        '''
        Purpose: Displays the result if user picked "Sure" and the "Restart" button.
        '''
        
        # # List of your local drive-thru places.
        result = f"Go for {random.choice(['McDonalds', 'Popeyes', 'Burger King', 'Dairy Queen','A&W', 'KFC'])}!"
        self.display_result(root, result)
        
        
    
        
    def start(self, root):
        '''
        Purpose: Contains the first button's action and returns the app screen.
        '''
        
        self.root.button.bind(on_press= self.beginQ)
        
    def beginQ(self,root):
        '''
        Purpose: Displays the next page after clicking the button on the home screen.
        '''
        
        # Clears page except for the logo.
        self.root.reset()
        
        # Adds the label and the buttons.
        self.root.add_label("Do you feel like driving?")
        self.yes = self.root.add_button("Sure", (0.9, 0.1), 0.21)
        
        self.no = self.root.add_button("Absolutely not!", (0.9, 0.1), 0.1)
        self.root.add_widget(self.yes)
        
        self.root.add_widget(self.no)
        self.yes.bind(on_press= self.option_y)
        self.no.bind(on_press= self.option_n)
        
        
    def return_home(self, root):
        '''
        Purpose: Go back to the home screen of the quiz app and ensures that the app will continue to run unless the user closes the window.
        '''
        
        # Calls the main_home() function from the Home() class.
        self.root.main_home()
        
        # Calls the start() function.
        self.start(root)
        #self.start(root)
        
          
    
        

if __name__ == "__main__":
    QuizApp().run()





    