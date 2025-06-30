from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class Auftrgasview(Screen):
    def __init__(self, auftrag, vorheriger_screen, **kwargs):
        self.auftrag = auftrag
        self.vorheriger_screen = vorheriger_screen
        self.boxlayout = BoxLayout(orientation="vertical")

        #Statusdaten
        self.bestellnr = Label(text=f"Bestellnummer: {self.auftrag.getBestellnr()}")
        self.boxlayout.add_widget(self.bestellnr)

        self.produktname = Label(text=f"Produktname: {self.auftrag.getProduktname()}")
        self.boxlayout.add_widget(self.produktname)

        self.status = Label(text=f"Status: {self.auftrag.getStatus()}")
        self.boxlayout.add_widget(self.status)

        self.produziert = Label(text=f"Produzierte Einheiten: {self.auftrag.getProduziertMenge()} von {self.auftrag.getAvisierteMenge()}")
        self.boxlayout.add_widget(self.produziert)

        self.linie = Label(text=f"gehört zu Linie: {self.auftrag.getLinienID()}")
        self.boxlayout.add_widget(self.linie)

        #Buttons "Arbeitszone"
        self.arbeitslayout = BoxLayout(orientation="horizontal")

        self.start_button = Button(text="Auftrag starten")
        self.start_button.bind(on_press=self.button_auftrag_start)

        self.produzieren_textinput = TextInput(multiline=False, input_filter="int")
        self.produzieren_button = Button(text="Produzierten")
        self.produzieren_button.bind(on_press=self.button_auftrag_produzieren)

        self.fertig_label = Label(text="Auftrag ist bereits abgeschlossen")

        #Zurückbutten
        self.back_button = Button(text="Zurück")
        self.back_button.bind(on_press=self.button_back)

        self.lade_auftragsdaten()
        self.add_widget(self.boxlayout)

    def lade_auftragsdaten(self):
        #Statusdaten aktualisieren
        self.status.text = f"Status: {self.auftrag.getStatus()}"
        self.produziert.text = f"Produzierte Einheiten: {self.auftrag.getProduziertMenge()} von {self.auftrag.getAvisierteMenge()}"

        #Arbeitszone aktualisieren
        self.arbeitslayout.clear_widgets()
        if self.auftrag.getStatus() == "created":
            self.arbeitslayout.add_widget(self.start_button)
        elif self.auftrag.getStatus() == "in production":
            self.arbeitslayout.add_widget(self.produzieren_textinput)
            self.arbeitslayout.add_widget(self.produzieren_button)
        else:
            self.arbeitslayout.add_widget(self.fertig_label)

    def button_auftrag_start(self):
        self.auftrag.start()
        self.lade_auftragsdaten()

    def button_auftrag_produzieren(self):
        self.auftrag.produce_units(self.produzieren_textinput.text)

        if self.auftrag.getMenge() >= self.auftrag.getAvisierteMenge():
            self.auftrag.finish()

        self.lade_auftragsdaten()

    def button_back(self):
        self.manager.current = self.vorheriger_screen
