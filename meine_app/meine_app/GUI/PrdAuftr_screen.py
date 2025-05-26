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


class PrdAuftragScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, padding=20, spacing=10)

        self.top_grid = GridLayout(cols=2, spacing=10)

        label = Label(
            text="Produktionsauftrag",
            font_size="24sp",
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=40,
            halign='center',
            valign='middle')
        label.bind(size=lambda *args: setattr(label, 'text_size', label.size))

        self.layout.add_widget(label)
        self.top_grid.add_widget(Label(text="produktName", color=(0, 0, 0, 1)))
        self.produktName = TextInput(multiline=False)
        self.top_grid.add_widget(self.produktName)

        self.top_grid.add_widget(Label(text="avisierteMenge", color=(0, 0, 0, 1)))
        self.avisierteMenge = TextInput(multiline=False)
        self.top_grid.add_widget(self.avisierteMenge)

        self.layout.add_widget(self.top_grid)

        self.submit = Button(text="Submit", size_hint=(None, None), size=(100, 40))
        self.submit.bind(on_press=self.press)

        button_box = BoxLayout(orientation='horizontal')
        button_box.add_widget(Widget())
        button_box.add_widget(self.submit)
        button_box.add_widget(Widget())

        self.layout.add_widget(button_box)
        self.add_widget(self.layout)

        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Auftrag;")
                result = cursor.fetchone()
                self.__bestellnr = result[0]
                print(f"BEFORE PRESS DEBUG: {self.__bestellnr}")

    def press(self, instance):
        name = self.produktName.text
        menge = self.avisierteMenge.text
        pa = Produktionsauftrag(name, menge)
        Util.save_to_db(pa)
        print("Produktionsauftrag ist " + pa.__repr__())

        self.produktName.text = ""
        self.avisierteMenge.text = ""



    # def press(self, instance):
    #     name = self.produktName.text            # Timo Kleinewächte hat gesagt da muss ".text" hin
    #     menge = self.avisierteMenge.text        # hab aber vergessen warum
    #
    #     pa : Produktionsauftrag = Produktionsauftrag(name, menge) #initialiseirt Obj mit parametern ausm dings
    #     Util.save_to_db(pa) # pakct das in Auftrag Datenbank
    #
    #
    #     # print to screen -> zum testen maybe noch brauchbar
    #
    #
    #     #self.top_grid.add_widget(Label(text=f'obj: {pa.__repr__()}'))
    #
    #     print("Produktionsauftrag ist " + pa.__repr__())



        self.produktName.text= ""
        self.avisierteMenge.text= ""
        #self.nameDrei.text =""

class PrdAuftragGui(App):
    def build(self):
        return PrdAuftragScreen()


if __name__ == "__main__":
    PrdAuftragGui().run()
