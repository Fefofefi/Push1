import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder

class MainWindow(Screen):

    cartas = ObjectProperty(None)
    objetivo = ObjectProperty(None)

    def btn(self):
        print("Se juega con", self.cartas.text, "cartas", "y se juega hasta", self.objetivo.text)
        cartas = self.cartas.text
        objetivo = self.objetivo.text
        self.cartas.text = ""
        self.objetivo.text = ""
        print(cartas, objetivo)

class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("tim4.kv")

class tim4App(App):
    def build(self):
        return kv

if __name__ == "__main__":
    tim4App().run()