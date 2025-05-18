from Produktionslinie import *

class MES:
    def __init__(self):
        self.__produktionslinie = []

    def add_production_line(self, linie):
        try:
            for i in self.__produktionslinie:
                if linie.getLinienName() == i.getLinienName():
                    raise ValueError(f"'{linie.getLinienName()}' existiert bereits.")
            self.__produktionslinie.append(linie)
        except ValueError as e:
            print(f"Fehler: {e}")

    def get_production_line(self):
        return self.__produktionslinie


