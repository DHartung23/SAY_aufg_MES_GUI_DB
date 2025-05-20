from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from meine_app.meine_app.GUI.LoginScreen import LoginScreen
from meine_app.meine_app.GUI.ProduktionlinienScreen import ProduktionsLinienScreen


class MESApp(App):
    def build(self):
        self.__screenmanager = ScreenManager()
        self.__screenmanager.add_widget(LoginScreen(name='login'))
        self.__screenmanager.add_widget(ProduktionsLinienScreen(name='produktionslinienwahl'))

        return self.__screenmanager

    def login(self, *args):
        self.__screenmanager.current = "produktionslinienwahl"

if __name__ == '__main__':
    MESApp().run()