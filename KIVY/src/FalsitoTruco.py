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
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen

Jugadores = []
QCartas = 0
Objetivo = 0

class Uno(Screen):

    def empezar(self):
        self.ids.grid.remove_widget(self.ids.juga)
        for i in Jugadores:
            a = Label(text=i, id="prueba")
            self.ids.grid.add_widget(a)
        self.ids.nombre.text = ""
        self.ids.borrar.disabled = True
        self.ids.reiniciar.disabled = False
        self.ids.empezar.disabled = True
        self.ids.qcartas.disabled = True
        self.ids.objetivo.disabled = True
        self.ids.agregar.disabled = True

    def reiniciar(self):
        Jugadores.clear()
        QCartas = 0
        Objetivo = 0
        self.ids.qcartas.text = ""
        self.ids.objetivo.text = ""
        self.ids.juga.text = ""
        self.ids.nombre.text = ""
        self.ids.agregar.disabled = False
        self.ids.borrar.disabled = True
        self.ids.reiniciar.disabled = True
        self.ids.empezar.disabled = True
        self.ids.qcartas.disabled = False
        self.ids.objetivo.disabled = False
        self.ids.grid.remove_widget(self.ids.juga)
        self.ids.grid.remove_widget(self.ids.prueba)
        print(Jugadores)

    def borrar(self):
        Jugadores.reverse()
        if len(Jugadores) != 0:
            largo = Jugadores.count(self)
            Jugadores.pop(largo)
            Jugadores.reverse()
            print(Jugadores)
            self.ids.juga.text = str(Jugadores)
        else:
            self.ids.juga.text = ""

    def agregar(self):
        Jugadores.append(self.ids.nombre.text)
        print(Jugadores)
        #self.ids.nombre.text = ""
        self.ids.borrar.disabled = False
        self.ids.reiniciar.disabled = False
        self.ids.empezar.disabled = False
        self.ids.juga.text = str(Jugadores)
        QCartas = self.ids.qcartas.text
        Objetivo = self.ids.objetivo.text
        self.ids.qcartas.disabled = True
        self.ids.objetivo.disabled = True

class Manager(ScreenManager):
    pass

class FalsoApp(App):
    title = "Falsito truco"
    def build(self):
        return Uno()

if __name__ == "__main__":
    FalsoApp().run()