from django.db import connection, transaction
import os
import sys
import django
import os
import django

# Konfiguriere die Django-Einstellungen
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meine_app.meine_app.Stuff.settings')

# Initialisiere Django
django.setup()



    #brauch ich maybe nochmal
    #_SQL_COUNT_QUERY = """SELECT COUNT(*) from Auftrag;"""

class Produktionsauftrag:
    def __init__(self, produktName: str, avisierteMenge: int):
        self.__produktName = produktName
        self.__menge = 0
        self.__status = "created"
        self.__avisierteMenge = avisierteMenge

        # Existing BestellNr generation logic for *new* objects
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM Auftrag;")
                    result = cursor.fetchone()
                    self.__bestellnr = result[0] + 1  # Increment for new
            print(f"DEBUG: New BestellNr generated: {self.__bestellnr}")
        except Exception as e:
            print(e)
            print(f"Fehler beim Generieren der BestellNr.")
            self.__bestellnr = -1  # Handle error

        self.__linienID = None
        self.__db_id = None  # Initialize for objects created this way


    @classmethod
    def from_db_row(cls, row_data):
        """
        Creates a Produktionsauftrag object from a database row.
        Assumes row_data is a tuple/list matching the SELECT query order.
        """
        # Map row_data indices to constructor arguments or directly to attributes
        # IMPORTANT: Adjust indices based on your SELECT query
        auftrag = cls(
            produktName=row_data[1],  # Assuming produktName is at index 2
            avisierteMenge=row_data[4]  # Assuming avisierteMenge is at index 3
        )
        # Directly set other attributes that are loaded from DB
         # Assuming id is at index 0
        auftrag.__bestellnr = row_data[0]  # Assuming BestellNr is at index 1
        auftrag.__menge = row_data[2]  # Assuming menge is at index 4
        auftrag.__status = row_data[3]  # Assuming status is at index 5
        auftrag.__linienID = row_data[4]  # Assuming linienID is at index 6

        return auftrag

        #self.__sql_insert_query = """INSERT INTO Auftrag (BestellNr, Produktname, Menge, Status, AvisierteMenge, LinienID) VALUES (?, ?, ?, ?, ?, ?);"""




    # hab in Util klasse rein gepackt wenn das geht löschen @nüchternes ich

    # def writeDB(self):
    #
    #     values_to_insert = (
    #         self.getBestellnr(),
    #         self.getProduktName(),
    #         self.getMenge(),
    #         self.getStatus(),
    #         self.getAvisierteMenge(),
    #         self.getLinienID(),
    #     )
    #
    #     try:
    #         with transaction.atomic():
    #             with connection.cursor() as cursor:
    #                 cursor.execute(self._SQL_INSERT_QUERY, values_to_insert)
    #
    #         print(
    #             f"Daten für Auftrag {self.getBestellnr() or 'ohne BestellNr'} erfolgreich über Raw SQL in Datenbank geschrieben.")
    #
    #     except Exception as e:
    #         print(f"FEHLER: Konnte Auftrag ({self.getProduktName()}, {self.getAvisierteMenge()}) nicht in Datenbank schreiben: {e}")




    def start(self):
        self.__status = "in Production"
    def finish(self):
        self.__status = "completed"



    def produce_units(self, menge : int):
        for i in range(menge):
            self.__menge = self.__menge + True

#############################           getter setter               ####################################################



    def getAvisierteMenge(self):
        return self.__avisierteMenge

    def getProduktName(self):
        return self.__produktName

    def getStatus(self):
        return self.__status

    def getLinienID(self):
        return self.__linienID

    def getBestellnr(self):
        return self.__bestellnr

    def getMenge(self):
        return self.__menge
    #-------------------------------        setter          ---------------------------


    def setAvisierteMenge(self, avisierteMenge):
        if avisierteMenge <= 0:
            self.__avisierteMenge = avisierteMenge
        else:
            raise ValueError(f"menge darf nich negativ sein!!!!!!!!!")
    def setLinienID(self, linienID):
        self.__linienID = linienID
    def __eq__(self, other):
        return self.__produktName == other.__produktName

    def __repr__(self):
        return str(f"Produktionsauftrag("
                f"bestellnr={self.__bestellnr}, "
                f"produktName={self.__produktName}, "
                f"menge={self.__menge}, "
                f"status={self.__status}, "
                f"avisierteMenge={self.__avisierteMenge}, "
                f"linienID={self.__linienID})")
