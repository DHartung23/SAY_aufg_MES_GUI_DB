from django.db import connection, transaction
import django
import os
from meine_app.meine_app.objects.Produktionsauftrag import Produktionsauftrag


class Produktionslinie:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meine_app.meine_app.Stuff.settings')  # <- Anpassen!
    django.setup()
    def __init__(self, name : str):
        self.__name = name
        self.__produktionsaufträge = []

        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM Linie;")
                    result = cursor.fetchone()
                    self.__linieid = result[0] + 1  # Increment for new
            print(f"DEBUG: New linieid generated: {self.__linieid}")
        except Exception as e:
            print(e)
            print(f"Fehler beim Generieren der linieid.")
            self.__linieid = -1  # Handle error


    def getLinienName(self):
        return self.__name

    def getLinienID(self):
        return self.__linieid

    def add_auftrag(self,auftrag : Produktionsauftrag):

        if auftrag in self.__produktionsaufträge:
            raise ValueError(f"'{auftrag.getProduktName()}' existiert bereits.")

        if auftrag.getAvisierteMenge() <= 0:
            raise Exception('menge darf nicht negativ sein')
        self.__produktionsaufträge.append(auftrag)


    def get_auftrag(self)->str:
        return self.__produktionsaufträge


    def getAufträge(self):
        return self.__produktionsaufträge








    def __eq__(self, other):
        return self.__name == other.__name
