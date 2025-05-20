from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager


class ProduktionsLinienScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text='Produktions Linien')
        self.add_widget(label)