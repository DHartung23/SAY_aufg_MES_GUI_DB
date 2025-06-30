from django.db import connection, transaction
from meine_app.meine_app.objects.Produktionslinie import Produktionslinie
from meine_app.meine_app.objects.Produktionsauftrag import Produktionsauftrag
import os
import django


class Util:


    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meine_app.meine_app.settings')  # <- Anpassen!
    django.setup()

    #--------------------------Aufgaben utils-------------------------------------
    @staticmethod
    def get_order_by_number(aufträge, bestellnr: int):
        for i in aufträge:
            if i.getBestellnr() == bestellnr:
                return i

    @staticmethod
    def calculate_production_efficiency(prodMenge, planMenge):
        return prodMenge / planMenge * 100



    #-----------------------------------datenbank zeug -------------------------------------------------------

    # SQL INSERT für Auftrag
    # diese %s sind platzhalter btw.... idk why aber funktioniert mit sqlite so (inshallah)

    _SQL_INSERT_AUFTRAG_QUERY = """
    INSERT INTO Auftrag (BestellNr, Produktname, Menge, Status, AvisierteMenge, LinienID)
    VALUES (%s, %s, %s, %s, %s, %s);
    """


    # SQL INSERT für Linie
    _SQL_INSERT_LINIE_QUERY = """
    INSERT INTO Linie (LinienID, name)
    VALUES (%s, %s);
    """
    #für add auftRAG
    _SQL_UPDATE_AUFTRAG_LINIENID_QUERY = """
        UPDATE Auftrag
        SET LinienID = %s
        WHERE BestellNr = %s;
        """
    _SQL_GET_ALL_LINIE_DATA_QUERY = """
    SELECT * FROM Linie;
    """

    _SQL_GET_ALL_AUFTRAG_DATA_QUERY = """
    SELECT * FROM Auftrag;
    """
    _SQL_GET_ALL_AUFTRAG_DATA_QUERY_ALT = """
        select * from Auftrag where LinienID = %s;
        """



    #Speichert nh Produktionslinie in der Linie Tabelle.
    @staticmethod
    def _save_produktionslinie(linie_obj):

        #holt sich das Linien zeug
        values_to_insert = (
            linie_obj.getLinienID(),  # Wert für LinienID (PK)
            linie_obj.getLinienName(),  # Wert für name
        )

        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(Util._SQL_INSERT_LINIE_QUERY, values_to_insert)

            print(
                f"Produktionslinie {linie_obj.getLinienName()} (ID: {linie_obj.getLinienID()}) gespeichert OwO.")

        except Exception as e:
            print(f"FEHLER beim Speichern von Produktionslinie {linie_obj.getLinienName()}: {e} QwQ")


    #Speichert nen Produktionsauftrag in der Auftrag Tabelle.
    @staticmethod
    def _save_produktionsauftrag(auftrag_obj):

        #holt sich das auftrag zeug
        values_to_insert = (
            auftrag_obj.getBestellnr(),
            auftrag_obj.getProduktName(),
            auftrag_obj.getMenge(),
            auftrag_obj.getStatus(),
            auftrag_obj.getAvisierteMenge(),
            auftrag_obj.getLinienID()  #-> das is ein FK (kp wie sich das verhalten wird
        )

        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(Util._SQL_INSERT_AUFTRAG_QUERY, values_to_insert)

            print(f"Produktionsauftrag {auftrag_obj.getBestellnr() or 'ohne BestellNr'} gespeichert (in der db.")

        except Exception as e:
            print(f"FEHLER beim Speichern von Produktionsauftrag {auftrag_obj.getBestellnr() or 'ohne BestellNr. QwQ'}: {e}")



    #uzpdated den auftag fpr addauftrag methode
    @staticmethod
    def update_produktionsauftrag_linienid(auftrag_obj):

        # gucken ob auftrag ne bestellnummer hat
        if auftrag_obj.getBestellnr() is None:
            print(f"FEHLER: Kann LinienID für Auftrag ohne BestellNr nicht aktualisieren.")
            return

        #KB das nochmal zu erklären (holt sich parameter für den select
        values_to_update = (
            auftrag_obj.getLinienID(),
            auftrag_obj.getBestellnr(),
        )

        try:
            print("gotcha bitch")
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(Util._SQL_UPDATE_AUFTRAG_LINIENID_QUERY, values_to_update)

            print(f"LinienID für Produktionsauftrag {auftrag_obj.getBestellnr()} erfolgreich aktualisiert (UPDATE).")

        except Exception as e:
            print(
                f"FEHLER beim Aktualisieren (UPDATE LinienID) von Produktionsauftrag {auftrag_obj.getBestellnr()}: {e}")


    #soll entweder ne linie ider nen auftrag in DB speichern
    @staticmethod
    def save_to_db(obj):
        if isinstance(obj, Produktionsauftrag):  # wenn Produktionsauftrag dann mach das
            Util._save_produktionsauftrag(obj)
        elif isinstance(obj, Produktionslinie):  # wenn prdlinie is mach das
            Util._save_produktionslinie(obj)       # warum is das obj gelb chat? - "Type 'Produktionslinie' doesn't have expected attribute 'getLinienID'"
        else:
            print(f"FEHLER: Unbekannter Objekttyp {type(obj)} geht nich QwQ.")

    @staticmethod
    def getAuftragFromDatenbak(linienID = None):
        print(linienID)

        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    if linienID is None:
                        cursor.execute(Util._SQL_GET_ALL_AUFTRAG_DATA_QUERY)
                    else:
                        cursor.execute(Util._SQL_GET_ALL_AUFTRAG_DATA_QUERY_ALT, linienID)
                    result = cursor.fetchall()

                    return result
        except Exception as e:
            print(f"Fehler beim Abrufen der Daten aus der Datenbank: {e}")
            # Gib eine leere Liste zurück, damit die App nicht abstürzt
            return []

    @staticmethod
    def getLinieFromDatenbak():

        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(Util._SQL_GET_ALL_LINIE_DATA_QUERY)
                result = cursor.fetchall()

                return result