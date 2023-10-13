import configparser
import kivy
import socket
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (1280, 100)

cl.soc

config = configparser.ConfigParser()
config.read('config.ini')

color1 = config['Appearance']['base']
color2 = config['Appearance']['second']

class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)

        self.cols = 2
        self.msg = TextInput(multiline=False)
        self.add_widget(self.msg)

        self.submit = Button(text='Send!')
        self.submit.bind(on_press=self.send)
        self.add_widget(self.submit)
    def send(self, instance):
        msg = self.msg.text
        self.msg.text = ''
        if msg != '':
            print(msg)
        
class Erbi(App):
    def build(self):
        return Layout()
Erbi().run()
