from kivy.uix.screenmanager import Screen, ScreenManager

from Scrollliste import Scrollliste

class ProduktionsLinienScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        linienliste = Scrollliste(["1", "2", "4"])

        self.add_widget(linienliste)