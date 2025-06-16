import kivy
from django.db import transaction, connection
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from meine_app.meine_app.objects.Produktionslinie import Produktionslinie
from meine_app.meine_app.objects.Produktionsauftrag import Produktionsauftrag
import os
import sys
import django
from meine_app.meine_app.Util import Util
from kivy.uix.boxlayout import BoxLayout
from meine_app.meine_app.Util import Util
from kivy.uix.widget import Widget

#BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meine_app.meine_app.Stuff.settings')
django.setup()


from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from meine_app.meine_app.objects.Produktionsauftrag import Produktionsauftrag
from meine_app.meine_app.Util import Util
from django.db import transaction, connection


class PrdLinieScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, padding=20, spacing=10)

        self.top_grid = GridLayout(cols=2, spacing=10)

        label = Label(
            text="Produktionslinie",
            font_size="24sp",
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=40,
            halign='center',
            valign='middle')
        label.bind(size=lambda *args: setattr(label, 'text_size', label.size))

        self.layout.add_widget(label)
        self.top_grid.add_widget(Label(text="linieName", color=(0, 0, 0, 1)))
        self.linieName = TextInput(multiline=False)
        self.top_grid.add_widget(self.linieName)

        self.back_button = Button(text="Zurück",
                                  size_hint=(None, None),
                                  size=(120, 40),
                                  background_normal='',
                                  background_color=(0.2, 0.6, 0.8, 1),  # Blue color
                                  color=(1, 1, 1, 1),
                                  bold=True,
                                  background_down='rgba(0.1,0.4,0.6,1)')
        self.back_button.bind(on_press=self.go_back)

        self.submit = Button(text="Submit", size_hint=(None, None),
                             size=(120, 40),
                             background_normal='',
                             background_color=(0.2, 0.6, 0.8, 1),  # Blue color
                             color=(1, 1, 1, 1),
                             bold=True,
                             background_down='rgba(0.1,0.4,0.6,1)')
        self.submit.bind(on_press=self.press)

        self.layout.add_widget(self.top_grid)

        button_box = BoxLayout(orientation='horizontal')
        button_box.add_widget(self.back_button)
        button_box.add_widget(Widget())
        button_box.add_widget(self.submit)

        self.layout.add_widget(button_box)
        self.add_widget(self.layout)

       # with transaction.atomic():
       #     with connection.cursor() as cursor:
       #         cursor.execute("SELECT COUNT(*) FROM Auftrag;")
       #        result = cursor.fetchone()
       #        self.__bestellnr = result[0]
       #        print(f"BEFORE PRESS DEBUG: {self.__bestellnr}")

    def press(self, instance):
        name = self.linieName.text
        pl = Produktionslinie(name)
        Util.save_to_db(pl)
        print("Produktionsauftrag ist " + pl.__repr__())

        self.linieName.text = ""
    def go_back(self, instance):
        """
        Navigiert zurück zum Homescreen.
        """
        if self.manager:
            self.manager.current = "home"
        else:
            print("ScreenManager nicht verfügbar.")