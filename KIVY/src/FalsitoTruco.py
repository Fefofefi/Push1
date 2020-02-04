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

Jugadores = []

class Uno(Screen):

    def agregar(self):
        Jugadores.append(self.ids.nombre.text)
        print(Jugadores)
        self.ids.nombre.text = ""
        self.ids.borrar.disabled = False
        self.ids.reiniciar.disabled = False
        self.ids.empezar.disabled = False
        self.ids.juga.text = str(Jugadores)

class Manager(ScreenManager):
    pass

class FalsoApp(App):
    title = "Falsito truco"
    def build(self):
        return Uno()

if __name__ == "__main__":
    FalsoApp().run()