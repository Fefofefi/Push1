import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Contenedor_01 (BoxLayout):
    def choice(self,guess):
        output="You clicked "+guess+" button!"
        self.ids.result.text=output


class MainApp(App):
    title = "Falsito truco"
    def build(self):
        return Contenedor_01()

if __name__ == '__main__':
    MainApp().run()