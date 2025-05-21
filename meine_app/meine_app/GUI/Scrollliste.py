from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


class Scrollliste(ScrollView):
    def __init__(self, einträge, beiAuswahl = None, farbe_ausgewählt = (0.1, 0.1, 1, 100), farbe_nicht_ausgewählt=(1, 1, 1, 0.5), **kwargs):
        super(Scrollliste, self).__init__(**kwargs)

        self.__beiAuswahl = beiAuswahl
        self.__ausgewählt = None

        self.__farbe_ausgewählt = farbe_ausgewählt
        self.__farbe_nicht_ausgewählt = farbe_nicht_ausgewählt

        boxlayout = BoxLayout(orientation="vertical", size_hint_y=None)
        boxlayout.bind(minimum_height=boxlayout.setter('height'))

        for eintrag in einträge:
            button = Button(text=eintrag, background_color=farbe_nicht_ausgewählt, size_hint_y=None)
            button.bind(on_press=self._neueAuswahl)
            boxlayout.add_widget(button)

        self.add_widget(boxlayout)


    def get_ausgewählt(self):
        return self.__ausgewählt

    def add_eintrag(self, eintrag):
        self.children[0].add_widget(eintrag)

    def _neueAuswahl(self, button):
        self.__ausgewählt = button.text

        for btn in self.children[0].children:
            btn.background_color = self.__farbe_nicht_ausgewählt

        button.background_color = self.__farbe_ausgewählt

        if self.__beiAuswahl:
            self.__beiAuswahl(button.text)