from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from meine_app.meine_app.GUI.LoginScreen import LoginScreen


class MESApp(App):
    def build(self):
        self.__screenmanager = ScreenManager()
        self.__screenmanager.add_widget(LoginScreen(name='login'))
