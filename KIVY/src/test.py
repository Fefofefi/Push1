import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Jugadores = ["Fede","Fede","Fede","Fede","Fede","Fede",]

class Contenedor_01 (BoxLayout):
    def __init__(self,**kwargs):
        super(Contenedor_01,self).__init__(**kwargs)

        for i in Jugadores:
            self.add_widget(Label(text=i))

    def choice(self,guess):
        output="You clicked "+guess+" button!"
        self.ids.result.text=output

class MaineApp(App):
    title = "Falsito truco"
    def build(self):
        return Contenedor_01()

if __name__ == '__main__':
    MaineApp().run()