import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from numberttolettre import numbertolettre


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1



        self.add_widget(Label(text="Entrer le nembre a converte"))
        self.number = TextInput(multiline=False)
        self.add_widget(self.number)



        self.convirt = Button(text="Convirtir", font_size=40)
        self.convirt.bind(on_press=self.pressed)
        self.add_widget(self.convirt)

        self.numberconverted = TextInput(multiline=False)
        self.add_widget(self.numberconverted)

    def pressed(self, instance):
        self.numberconverted.text = numbertolettre(self.number.text)


class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()