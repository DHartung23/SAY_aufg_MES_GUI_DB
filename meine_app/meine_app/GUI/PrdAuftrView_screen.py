from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from meine_app.meine_app.Util import Util
from kivy.uix.screenmanager import Screen
class PrdAuftrViewScreen(Screen):
    def __init__(self,a:str, **kwargs):
        super().__init__(**kwargs) # 'name' nicht weitergeben!
        self.root = BoxLayout(orientation='vertical')

        self.scroll_view = ScrollView(size_hint=(1, 1))

        self.button_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.button_container.bind(minimum_height=self.button_container.setter('height'))

        self.button_height = Window.height * 0.2

        self.showAuftrag(Util.getAuftragFromDatenbak())



        self.showAuftrag(Util.getAuftragFromDatenbak())
        self.scroll_view.add_widget(self.button_container)
        self.add_widget(self.scroll_view)





    def showAuftrag(self, liste: list):
        for auftrag in liste:
            btn = Button(text=f"BestellNr: {auftrag[0]} | "
                              f"Produktname: {auftrag[1]} | "
                              f"status: {auftrag[3]} | "
                              f"Avis. Menge: {auftrag[4]}",
                         color=(0, 0, 0, 1),
                         size_hint_y=None,
                         height=self.button_height)

            self.button_container.add_widget(btn)

    def showLinie(self, liste : list):

        for linie in liste:
            btn = Button(text=f"Linie: {linie[1]}",color=(0, 0, 0, 1), size_hint_y=None, height=self.button_height)
            self.button_container.add_widget(btn)

if __name__ == '__main__':
    PrdAuftrViewScreen().run()