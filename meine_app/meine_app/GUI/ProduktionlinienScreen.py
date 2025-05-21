from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from Scrollliste import Scrollliste

class ProduktionsLinienScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical")

        linienliste = Scrollliste([str(i+1) for i in range(15)], self.tmp)
        boxlayout.add_widget(linienliste)
        self.add_widget(boxlayout)

    def tmp(self, auswahl):
        print(auswahl)