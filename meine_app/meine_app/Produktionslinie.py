
from Produktionsauftrag import *
import django
import os

class Produktionslinie:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '.meine_app\meine_app\settings.py')  # <- Anpassen!
    django.setup()
    def __init__(self, name : str):
        self.__name = name
        self.__produktionsaufträge = []


    def getLinienName(self):
        return self.__name
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
