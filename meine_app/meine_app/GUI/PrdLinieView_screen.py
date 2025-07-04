from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from PrdAuftrView_screen import PrdAuftrViewScreen
from meine_app.meine_app.GUI.PrdAuftr_screen import PrdAuftragScreen
from meine_app.meine_app.Util import Util
from kivy.uix.screenmanager import Screen
class PrdLinieViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # 'name' nicht weitergeben!
        self.irgendwas = BoxLayout(orientation='vertical')
        self.scroll_view = ScrollView(size_hint=(1, 1))


        self.button_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.button_container.bind(minimum_height=self.button_container.setter('height'))

        self.button_height = Window.height * 0.2
        self.showLinie(Util.getLinieFromDatenbak())

        self.irgendwas.add_widget(self.scroll_view)

        self.scroll_view.add_widget(self.button_container)
        self.add_widget(self.irgendwas)

        self.back_button = Button(text="Zurück",
                                  size_hint=(None, None),
                                  size=(120, 40),
                                  background_normal='',
                                  background_color=(0.2, 0.6, 0.8, 1),  # Blue color
                                  color=(1, 1, 1, 1),
                                  bold=True,
                                  background_down='rgba(0.1,0.4,0.6,1)')
        self.back_button.bind(on_press=self.go_back)
        button_box = BoxLayout(orientation='horizontal')
        button_box.add_widget(self.back_button)
        self.irgendwas.add_widget(button_box)

    def go_back(self, instance):
        self.manager.current = "home"
        print("back")

    def switchWindow(self, instance, linie_id):
        # Important: Check if the screen already exists in the manager
        screen_name = f"auftrag_viewlinie{linie_id}"
        if not self.manager.has_screen(screen_name):
            # Create the screen instance only if it doesn't exist
            new_screen = PrdAuftrViewScreen(linienID=linie_id, name=screen_name)
            self.manager.add_widget(new_screen)

        # Now switch to the screen using its name
        self.manager.current = screen_name

        #self.manager.current = PrdAuftrViewScreen(linienID=a, name="irgendwas")
    def showLinie(self, liste: list):
        for linie in liste:

            btn = Button(text=f"LinieNr: {linie[0]} | "
                              f"Liniename: {linie[1]} | ",
                         color=(0, 0, 0, 1),
                         size_hint_y=None,
                         height=self.button_height,
                         on_press=lambda instance, line_id=linie[0]: self.switchWindow(instance, line_id))

            self.button_container.add_widget(btn)



    # def showLinie(self, liste : list):
    #
    #     for linie in liste:
    #         btn = Button(text=f"Linie: {linie[1]}",color=(0, 0, 0, 1), size_hint_y=None, height=self.button_height)
    #         self.button_container.add_widget(btn)