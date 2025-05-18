import kivy
from django.db import transaction, connection
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Produktionslinie import Produktionslinie
from Produktionsauftrag import Produktionsauftrag
import os
import sys
import django
from Util import Util

from meine_app.meine_app.Util import Util


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meine_app.meine_app.settings')
django.setup()


class gridLayOut(GridLayout):
    #init infinite keywords
    def __init__(self, **kwargs):
        #call constructer
        super(gridLayOut, self).__init__(**kwargs)

        #cols
        self.cols = 1
        # überschrift



        self.top_grid = GridLayout()
        self.top_grid.cols = 2


        self.top_grid.add_widget(Label(text="überschrift"))
        self.ueberschrift = Label()
        self.top_grid.add_widget(self.ueberschrift)

        self.top_grid.add_widget(Label(text=""))
        self.dummy = Label()
        self.top_grid.add_widget(self.dummy)

        # def __init__(self, produktName : str, avisierteMenge : int):

        # add widget
        self.top_grid.add_widget(Label(text="produktName --> string"))
        self.produktName = TextInput(multiline=False)
        self.top_grid.add_widget(self.produktName)

        self.top_grid.add_widget(Label(text="avisierteMenge  ---> Integer"))
        self.avisierteMenge = TextInput(multiline=False)
        self.top_grid.add_widget(self.avisierteMenge)


        # blauch nich mehr
        # self.top_grid.add_widget(Label(text="drittes widget"))
        # self.nameDrei = TextInput(multiline=False)
        # self.top_grid.add_widget(self.nameDrei)


        #add sub grid to thingy
        self.add_widget(self.top_grid)

        #Button
        self.submit = Button(text="submit")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

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

        pa : Produktionsauftrag = Produktionsauftrag(name, menge)
        Util.save_to_db(pa)


        # print to screen -> zum testen maybe noch brauchbar


        self.top_grid.add_widget(Label(text=f'obj: {pa.__repr__()}'))

        print("Produktionsauftrag ist " + pa.__repr__())
        with transaction.atomic():
            with connection.cursor() as cursor:
                #cursor.execute("COMMIT;")
                cursor.execute("SELECT COUNT(*) FROM Auftrag;")

                result = cursor.fetchone()
                self.__bestellnr = result[0]
            print(
                f"AFTER PRESS DEBUG: {self.__bestellnr}")


        self.produktName.text= ""
        self.avisierteMenge.text= ""
        #self.nameDrei.text =""

class MyApp(App):
    def build(self):
        return gridLayOut()


if __name__ == "__main__":
    MyApp().run()
