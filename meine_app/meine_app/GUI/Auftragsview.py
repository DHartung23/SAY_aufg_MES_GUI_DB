from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Auftrgasview:
    def __init__(self, auftrag, **kwargs):
        self.ladeauftrag(auftrag)

    def ladeauftrag(self, auftrag):
        boxlayout = BoxLayout(orientation="vertical")

        bestellnr = Label(text=f"Bestellnummer: {auftrag.getBestellnr()}")
        boxlayout.add_widget(bestellnr)

        produktname = Label(text=f"Produktname: {auftrag.getProduktname()}")
        boxlayout.add_widget(bestellnr)

        status = Label(text=f"Status: {auftrag.getStatus()}")
        boxlayout.add_widget(status)

        produziert = Label(
            text=f"Produzierte Einheiten: {auftrag.getProduziertMenge()} von {auftrag.getAvisierteMenge()}")
        boxlayout.add_widget(produziert)

        linie = Label(text=f"gehört zu Linie: {auftrag.getLinienID()}")
        boxlayout.add_widget(linie)