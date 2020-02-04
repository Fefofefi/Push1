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
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox

Window.size = (300, 1280)

Jugadores = []
CantidadDeCartas = 0
Objetivo = 0
Manos = 0

class MainWindow(Screen):

    cartas = ObjectProperty(None)
    objetivo = ObjectProperty(None)

    def btn(self):
        CantidadDeCartas = int(self.cartas.text)
        Objetivo = int(self.objetivo.text)
        self.cartas.text = ""
        self.objetivo.text = ""

class SecondWindow(Screen):

    cartas = ObjectProperty(None)
    objetivo = ObjectProperty(None)

class ThirdWindow(Screen):

    def btn3(self):
        Nombre = self.njugador.text
        Jugadores.append(Nombre)
        self.njugador.text = ""
        self.jugador.text = str(Jugadores)
        print(Jugadores)

    def btn4(self):
        self.njugador.text = ""
        Jugadores.clear()
        self.jugador.text = ""

    def btn5(self):
        Jugadores.reverse()
        if len(Jugadores) != 0:
            largo = Jugadores.count(self)
            Jugadores.pop(largo)
            Jugadores.reverse()
            print(Jugadores)
            self.jugador.text = str(Jugadores)
        else:
            self.jugador.text = ""

class FourWindow(Screen):
    def __init__(self, **kwargs):
        super(FourWindow, self).__init__(**kwargs)
        for i in Jugadores:
            self.add_widget(Label(text=i))

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("tim4.kv")

class tim4App(App):
    def build(self):
        return kv

if __name__ == "__main__":
    tim4App().run()