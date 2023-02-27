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
        Purpose: Initiates the class and calls the function main_home()
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
        
        # Calls the add_button function() and displays the button
        self.button = self.add_button("Yes, I'm starving!", (0.9, 0.185), 0.1)
        self.add_widget(self.button)
        
        # Calls the function to create and display the logo
        self.logo()
        
        
        
    
    def add_label(self, string):
        '''
        Purpose: Creates and displays the label onto the app.
        '''
        
        self.add_widget(Label(
            text = string,
            font_size = 45,
            color = "#FFFFFF",
            bold = True,
            pos_hint={'x': 0.000000001, 'center_y': 0.4}
        ))
        
    def add_button(self, string, size, y):
        '''
        Purpose: Creates a button and returns it.
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
        
        # Clears all the widgets with Kivy method and calls the logo() function.
        self.clear_widgets()
        self.logo()    
        
# Step 4: Creates the rest of the quiz layouts. Any word before the App for the name of the class will become the title in the tab. So in this example, the title is "Decide_What_To_Eat"
class Decide_What_To_EatApp(App):
    
    def build(self):
        '''
        Initiates and builds the quiz.
        '''
        
        # Creates a variable for the Home() class.
        self.root = root = Home()
        
        # Calls the start() function.
        self.start(root)
    
    def display_result(self, root, result):
        '''
        Purpose: Display the result of the quiz
        '''
        
        # First: Resets the screen if any widget is on there
        self.root.reset()
        
        # Second: Calls the add_label() function to add the result.
        self.root.add_label(result)
        
        # Third: Create, display, and binds "Restart" button
        # 1. Calls the add_button() function to add the restart button.
        self.restart_but = self.root.add_button("Restart", (0.9, 0.1), 0.18)
        
        # 2. Displays the restart button
        self.root.add_widget(self.restart_but)
        
        # 3. Determines what happens when the user presses on the restart button
        self.restart_but.bind(on_press= self.return_home)
        
        
    def option_n(self, root):
        '''
        Purpose: Determines the result for result if user picked "Absolutely Not!"
        '''
        
        # Returns the result after getting a random choice
        self.display_result(root, f"Get {random.choice(['Mikado', 'Edo Japan', 'Pizza Hut', 'Dominos', 'Swan Pizza' , 'Papa Johns Pizza', 'Pizza 73', 'Grain of Rice', 'Rice Bowl Deluxe'])}!")
        
        
    
    def option_y(self, root):
        '''
        Purpose: Determines the result for result if user picked "Sure"
        '''
                
        # Returns the result after getting a random choice
        self.display_result(root, f"Go for {random.choice(['McDonalds', 'Popeyes', 'Burger King', 'Dairy Queen','A&W', 'KFC'])}!")
        
        
    
        
    def start(self, root):
        '''
        Purpose: Determines what the home screen button does. It enables us to make the quiz a loop (see return_home() function)
        '''
        
        self.root.button.bind(on_press= self.beginQ)
        
    def beginQ(self,root):
        '''
        Purpose: Displays the only question page.
        '''
        
        # Clears page except for the logo.
        self.root.reset()
        
        # Adds the label and the buttons by calling functions
        self.root.add_label("Do you feel like driving?")
        self.yes = self.root.add_button("Sure", (0.9, 0.1), 0.21)
        self.no = self.root.add_button("Absolutely not!", (0.9, 0.1), 0.1)
        
        # Uses kivy methods to display the widgets and binds the buttons
        self.root.add_widget(self.yes)
        self.root.add_widget(self.no)
        self.yes.bind(on_press= self.option_y)
        self.no.bind(on_press= self.option_n)
        
        
    def return_home(self, root):
        '''
        Purpose: Go back to the home screen of the quiz app and ensures that the app will run infinitely.
        '''
        
        # Calls the main_home() function from the Home() class.
        self.root.main_home()
        
        # Calls the start() function.
        self.start(root)
        
          
    
        
# Testing the program :)
if __name__ == "__main__":
    Decide_What_To_EatApp().run()





    