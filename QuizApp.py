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
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout


# Now we will open the file with the list of places and convert it into a list.
p = open("Places.txt"); places = []; [places.append(i.strip()) for i in p]
q = open("Questions.txt"); qs = [];  [qs.append(i.strip()) for i in q]

# Split the list into the categories drive thru and deliver.
drive_thru = places[0:6]; deliver = places[6:-1]

class Home(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(Home, self).__init__(**kwargs)
        
        #let's add a Widget to this layout
        
    
        self.label = Label(
                text="Are you ready to decide what to eat?",
                font_size = 45,
                color = "#FFFFFF",
                bold = True,
                pos_hint={'x': 0.000000001, 'center_y': 0.4}
            )
        self.button = Button(
            text = "Yes, I'm starving!",
            size_hint = (0.9, 0.185),
            bold = True,
            font_size = 30,
            pos_hint={'center_x': 0.5, 'y': 0.1})
        
        self.add_widget(self.label)
        self.add_widget(self.button)
        
        self.add_widget(
            Image(source="logo.png",
            size_hint = (0.3, 0.7),
            pos_hint={'center_x': 0.5, 'y': 0.355}))
        
        #self.button.bind(on_press= self.reset)
        
        

    def reset(self):
        self.remove_widget(self.button)
        self.remove_widget(self.label)      
        

class QuizApp(App):
    
    def build(self):
        
        
        self.root = root = Home()
        
        
        
        root.bind(size=self._update_rect, pos=self._update_rect)
        

        with root.canvas.before:
            Color(0, 0, 0, 0)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
            
        root.button.bind(on_press= self.beginQ)
        self.h = ''
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    
    def beginQ(self,root):
        import random
        self.root.reset()
        self.add_label(root,"Do you feel like driving?")
        self.add_buttons(root)
        
        #self.answer(self)
        
        # "Sure",0.9,0.1, 0.5, 0.21, random.choice(drive_thru))
        # self.add_button(root, "Absolutely not!", 0.9, 0.1, 0.5, 0.1, random.choice(deliver))
        
        
        
        
    def add_label(self,root, string):
        
        self.new_l = Label(
            text = string,
            font_size = 45,
            color = "#FFFFFF",
            bold = True,
            pos_hint={'x': 0.000000001, 'center_y': 0.4}
        )
        self.root.add_widget(self.new_l)
        
        
    def add_buttons(self, root):
        import random
        # y = ["Sure",0.9,0.1, 0.5, 0.21, random.choice(drive_thru)]
        # n = ["Absolutely not!", 0.9, 0.1, 0.5, 0.1, random.choice(deliver)]
        
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
        # self.y.bind(on_press= )
        # self.buttonN.bind(on_press = print(random.choice(deliver)))
        
        
    
        
        # self.remove_widget(self.y)
        # self.remove_widget(self.buttonN)
        #self.remove_widgets(self.new_l)
        #self.add_label(root,e)
        
        
        
        
        # self.buttonY.bind(on_press= print(f"Go for {random.choice(drive_thru)}"))
        
        # self.buttonN.bind(on_press= print(f"Go for {random.choice(deliver)}"))
            
            
            
            
            
        # self.buttonN = Button(
        #     text = "Absolutely Not!",
        #     size_hint = (0.5, 0.5),
        #     bold = True,
        #     font_size = 30
        # )
        
        
        # self.buttonY.bind(on_press = self.yesoption)
        # self.buttonN.bind(on_press = self.nooption)
        # self.window.add_widget(self.buttonY)
        # self.window.add_widget(self.buttonN)
    
    
    
        # self.window = GridLayout()
        # self.window.cols = 1
        # self.window.size_hint = (0.6, 0.7)
        # self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # self.window.add_widget(Image(source="logo.png"))
        
        # self.ready4Quiz = Label(
        #     text = "Are you ready to decide what to eat?",
        #     font_size = 45,
        #     color = "#FFFFFF",
        #     bold = True
        # )
        
        # self.window.add_widget(self.ready4Quiz)
        
        # self.button = Button(
        #     text = "YES, I'M STARVING!!",
        #     size_hint = (0.5, 0.5),
        #     bold = True,
        #     font_size = 30
        # )
        # self.window.add_widget(self.button)
        # self.button.bind(on_press = self.beginQ)
        
        
        # return self.window
    ##########################################################################
    # def beginQ(self, event):
        
    #     
        
        
        
    
        
        
        
    # def yesoption(self, event):
        
    #     import random
        
    #     ans = str(random.choice(drive_thru))
        
    #     self.window.remove_widget(self.quest)
    #     self.window.remove_widget(self.buttonN)
    #     self.window.remove_widget(self.buttonY)
        
    #     self.ans = Label(
    #         text = f"Go for {ans}!",
    #         font_size = 45,
    #         color = "#FFFFFF",
    #         bold = True
    #     )
        
    #     self.window.add_widget(self.ans)
        
        
        
        
    
    # def nooption(self, event):
    #     import random
        
    #     ans = str(random.choice(deliver))
        
    #     self.window.remove_widget(self.quest)
    #     self.window.remove_widget(self.buttonN)
    #     self.window.remove_widget(self.buttonY)
        
    #     self.ans = Label(
    #         text = f"Get {ans}!",
    #         font_size = 45,
    #         color = "#FFFFFF",
    #         bold = True
    #     )
        
    #     self.window.add_widget(self.ans)

if __name__ == "__main__":
    QuizApp().run()





    