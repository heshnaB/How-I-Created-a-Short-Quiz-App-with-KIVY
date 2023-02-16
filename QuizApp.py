#In Progress

'''
Author: Heshna Bhagawan
Project: Building a quiz app that helps you decide what to eat. The code is designed to go in an infinite loop and won't close until the user closes the window.

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
from kivy.uix.textinput import TextInput
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
        self.label = Label(
                text="Are you ready to decide what to eat?",
                font_size = 45,
                color = "#FFFFFF",
                bold = True,
                pos_hint={'x': 0.000000001, 'center_y': 0.4}
            )
        
        # Creates the button for the answer to the first question.
        self.button = Button(
            text = "Yes, I'm starving!",
            size_hint = (0.9, 0.185),
            bold = True,
            font_size = 30,
            pos_hint={'center_x': 0.5, 'y': 0.1})
        
        # Display the logo
        self.logo()
        
        # Display the question and the button.
        self.add_widget(self.label)
        self.add_widget(self.button)
        
        
            

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
        
        # Recognizes the size and position changes. See the purpose of the function "_update_rect()" below.
        root.bind(size=self._update_rect, pos=self._update_rect)
        
        # Adds a background image/color/video to the layout of the quiz app. 
        with root.canvas.before:
            
            # See color link in references for more colors.
            Color(0, 0, 0, 0)  
            self.rect = Rectangle(size=root.size, pos=root.pos)
        
        # Calls the start() function.
        self.start(root)
    
    def _update_rect(self, instance, value):
        '''
        Purpose: To ensure that the rectangle is drawn inside the layout of the quiz app.
        '''
        self.rect.pos = instance.pos
        self.rect.size = instance.size   
        
    def start(self, root):
        '''
        Purpose: Contains the first button's action and returns the app screen.
        '''
        
        self.root.button.bind(on_press= self.beginQ)
        self.h = ''
        return root
        
    
    
    
    def beginQ(self,root):
        '''
        Purpose: Displays the next page after clicking the button on the home screen.
        '''
        
        # Clears page except for the logo.
        self.root.reset()
        
        # Adds the label and the buttons.
        self.add_label(root,"Do you feel like driving?")
        self.add_buttons(root)
        
        
        
        
    def add_label(self,root, string):
        '''
        Purpose: Create and add the label onto the app.
        '''
        
        self.root.add_widget(Label(
            text = string,
            font_size = 45,
            color = "#FFFFFF",
            bold = True,
            pos_hint={'x': 0.000000001, 'center_y': 0.4}
        ))
        
        
        
    def add_buttons(self, root):
        '''
        Purpose: Create and add the yes and no buttons.
        '''
        
        self.y = Button(
            text = "Sure",
            size_hint = (0.9,0.1),
            bold = True,
            font_size = 30,
            pos_hint={'center_x': 0.5, 'y': 0.21},
        )
        
        self.buttonN = Button(
            text = "Absolutely not!",
            size_hint = (0.9,0.1),
            bold = True,
            font_size = 30,
            pos_hint={'center_x': 0.5, 'y': 0.1},
            
        )
        
        self.root.add_widget(self.y)
        self.root.add_widget(self.buttonN)
        
        # Binds the yes and no buttons so that they lead the user to their own result.
        self.y.bind(on_press= self.option_y)
        self.buttonN.bind(on_press = self.option_n)
    
    
    def home_button(self, root):
        '''
        Display: Adds a button that takes the user back to the homepage.
        '''
        
        self.restart_but = Button(
            text = "Restart?",
            size_hint = (0.9,0.1),
            bold = True,
            font_size = 30,
            pos_hint={'center_x': 0.5, 'y': 0.18},
            
        )
        
        self.root.add_widget(self.restart_but)
        
        # When the user presses on the restart button, the program calls the return_home() function.
        self.restart_but.bind(on_press= self.return_home)
        
        
        
    def return_home(self, root):
        '''
        Purpose: Go back to the home screen of the quiz app and ensures that the app will continue to run unless the user closes the window.
        '''
        
        # Calls the main_home() function from the Home() class.
        self.root.main_home()
        
        # Calls the start() function.
        self.start(root)
        
          
    def option_n(self, root):
        '''
        Purpose: Displays the result if user picked "Absolutely Not!" and the "Restart" button.
        '''
        
        # List of your local places that has delivery.
        deliver = ['Mikado', 'Edo Japan', 'Pizza Hut', 'Dominos', \
            'Swan Pizza' , 'Papa Johns Pizza', 'Pizza 73', 'Grain of Rice',\
                'Rice Bowl Deluxe']
        
        # Clears the quiz app except for the logo
        self.root.reset()
        
        # Displays the result & the restart button to restart the quiz.
        self.add_label(root,f"Get {random.choice(deliver)}!")
        self.home_button(root)
        
    
    def option_y(self, root):
        '''
        Purpose: Displays the result if user picked "Sure" and the "Restart" button.
        '''
        
        # # List of your local drive-thru places.
        drive_thru = ['McDonald\'s', 'Popeyes', 'Burger King', 'Dairy Queen','A&W', 'KFC']
        
        # Clears the quiz app except for the logo
        self.root.reset()
        
        # Displays the result & the restart button to restart the quiz.
        self.add_label(root,f"Go for {random.choice(drive_thru)}!")
        self.home_button(root)
        

if __name__ == "__main__":
    QuizApp().run()





    