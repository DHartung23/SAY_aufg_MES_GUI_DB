from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from meine_app.meine_app.Util import Util
from kivy.uix.screenmanager import Screen
class ScrollButtonApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # 'name' nicht weitergeben!
        self.root = BoxLayout(orientation='vertical')

        self.scroll_view = ScrollView(size_hint=(1, 1))

        self.button_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.button_container.bind(minimum_height=self.button_container.setter('height'))

        self.button_height = Window.height * 0.2

    def build(self):
        self.showAuftrag(Util.getLinieFromDatenbak())
        self.scroll_view.add_widget(self.button_container)
        self.root.add_widget(self.scroll_view)
        return self.root

    def showAuftrag(self, liste: list):
        for auftrag in liste:
            btn = Button(text=f"Auftrag: {auftrag[liste][1]}",color=(1, 1, 1, 1), size_hint_y=None, height=self.button_height)
            self.button_container.add_widget(btn)
            print(auftrag[liste])

    def showLinie(self, liste : list):

        for linie in liste:
            btn = Button(text=f"Linie: {linie[1]}",color=(0, 0, 0, 1), size_hint_y=None, height=self.button_height)
            self.button_container.add_widget(btn)

if __name__ == '__main__':
    ScrollButtonApp().run()