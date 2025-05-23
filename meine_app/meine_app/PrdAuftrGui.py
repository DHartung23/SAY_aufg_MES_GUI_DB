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
from Util import Util
from kivy.uix.boxlayout import BoxLayout
from meine_app.meine_app.Util import Util
from kivy.uix.widget import Widget

#BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meine_app.meine_app.Stuff.settings')
django.setup()


class gridLayOut(GridLayout):
    #init infinite keywords
    def __init__(self, **kwargs):
        #call constructer
        super(gridLayOut, self).__init__(**kwargs)

        #cols
        self.cols = 1
        self.padding = 20
        self.spacing = 10

        # überschrift



        self.top_grid = GridLayout(cols=2, spacing = 10)
        self.top_grid.cols = 2


        label = Label(
    text="Produktionsauftrag",
    font_size="24sp",
    bold=True,
    color=(1, 1, 1, 1),
    size_hint=(1, None),
    height=40,
    halign='center',
    valign='middle'
)
        label.bind(size=lambda *args: setattr(label, 'text_size', label.size))

        self.add_widget(label)

        self.top_grid.add_widget(Label(text=""))
        self.dummy = Label()
        self.top_grid.add_widget(self.dummy)

        # def __init__(self, produktName : str, avisierteMenge : int):

        # add widget
        self.top_grid.add_widget(Label(text="produktName",
        font_size = "24sp",
        bold = True,
        color = (1, 1, 1, 1)
        ))
        self.produktName = TextInput(multiline=False)
        self.top_grid.add_widget(self.produktName)

        self.top_grid.add_widget(Label(text="avisierteMenge",
        font_size = "24sp",
        bold = True,
        color = (1, 1, 1, 1)
        ))
        self.avisierteMenge = TextInput(multiline=False)
        self.top_grid.add_widget(self.avisierteMenge)


        # blauch nich mehr
        # self.top_grid.add_widget(Label(text="drittes widget"))
        # self.nameDrei = TextInput(multiline=False)
        # self.top_grid.add_widget(self.nameDrei)


        #add sub grid to thingy
        self.add_widget(self.top_grid)

        #Button
        self.submit = Button(   text="Submit", size_hint=(None, None), size=(100, 40) )# Breite: 100px, Höhe: 40px)
        self.submit.bind(on_press=self.press)


        button_box = BoxLayout(orientation='horizontal')
        button_box.add_widget(Widget())
        button_box.add_widget(self.submit)
        button_box.add_widget(Widget())

        self.add_widget(button_box)


        self.commit_button = Button(text="In Datenbank speichern")
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Auftrag;")
                result = cursor.fetchone()
                self.__bestellnr = result[0]
            print(
                f" BEFORE PRESS DEBUG: {self.__bestellnr}")


    def press(self, instance):
        name = self.produktName.text
        menge = self.avisierteMenge.text

        pa : Produktionsauftrag = Produktionsauftrag(name, menge) #initialiseirt Obj mit parametern ausm dings
        Util.save_to_db(pa) # pakct das in Auftrag Datenbank


        # print to screen -> zum testen maybe noch brauchbar


        #self.top_grid.add_widget(Label(text=f'obj: {pa.__repr__()}'))

        print("Produktionsauftrag ist " + pa.__repr__())
        # with transaction.atomic():
        #     with connection.cursor() as cursor:
        #         #cursor.execute("COMMIT;")
        #         cursor.execute("SELECT COUNT(*) FROM Auftrag;")
        #
        #         result = cursor.fetchone()
        #         self.__bestellnr = result[0]
        #     print(
        #         f"AFTER PRESS DEBUG: {self.__bestellnr}")


        self.produktName.text= ""
        self.avisierteMenge.text= ""
        #self.nameDrei.text =""

class PrdAuftragGui(App):
    def build(self):
        return gridLayOut()


if __name__ == "__main__":
    PrdAuftragGui().run()
