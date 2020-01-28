import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class Caja1(Widget):
    pass

class MyApp(App):
    title = "Falsito truco"
    def build(self):
        return Caja1()

if __name__ == "__main__":
    MyApp().run()