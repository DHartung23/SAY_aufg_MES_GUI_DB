from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from meine_app.meine_app.Util import Util
from kivy.uix.screenmanager import Screen
class PrdAuftrViewScreen(Screen):
    def __init__(self, linienID = None, **kwargs):
        super().__init__(**kwargs) # 'name' nicht weitergeben!
        self.irgendwas = BoxLayout(orientation='vertical')
        self.modus = linienID
        self.scroll_view = ScrollView(size_hint=(1, 1))

        self.button_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.button_container.bind(minimum_height=self.button_container.setter('height'))

        self.button_height = Window.height * 0.2
        if linienID is None:
            self.showAuftrag(Util.getAuftragFromDatenbak())
        else:
            self.showAuftrag(Util.getAuftragFromDatenbak(linienID))
        self.irgendwas.add_widget(self.scroll_view)

        self.scroll_view.add_widget(self.button_container)
        self.add_widget(self.irgendwas)

        self.back_button = Button(text="Zurück",
                                  size_hint=(None, None),
                                  size=(120, 40),
                                  background_normal='',
                                  background_color=(0.2, 0.6, 0.8, 1),  # Blue color
                                  color=(1, 1, 1, 1),
                                  bold=True,
                                  background_down='rgba(0.1,0.4,0.6,1)')
        self.back_button.bind(on_press=self.go_back)
        button_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        button_box.add_widget(self.back_button)
        self.irgendwas.add_widget(button_box)

    def go_back(self, instance):
        if self.manager:
            self.manager.current = "home"
        else:
            print("ScreenManager nicht verfügbar.")





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

    # def showLinie(self, liste : list):
    #
    #     for linie in liste:
    #         btn = Button(text=f"Linie: {linie[1]}",color=(0, 0, 0, 1), size_hint_y=None, height=self.button_height)
    #         self.button_container.add_widget(btn)

if __name__ == '__main__':
    PrdAuftrViewScreen().run()