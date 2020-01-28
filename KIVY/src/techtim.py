import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class Caja1 (GridLayout):
    def __init__(self,**kwargs):
        super(Caja1, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Name: "))
        self.name =  TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.enviar = Button(text="Enviar")
        self.enviar.bind(on_press=self.pressed)
        self.add_widget(self.enviar)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        mail = self.email.text

        print(name, last, mail)

class MainApp(App):
    title = "Falsito truco"
    def build(self):
        return Caja1()

if __name__ == '__main__':
    MainApp().run()