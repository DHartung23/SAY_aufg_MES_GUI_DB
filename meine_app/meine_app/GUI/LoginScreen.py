from tkinter import Button

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class LoginScreen(Screen):
    def __init__(self, **kwargs):
            super(LoginScreen, self).__init__(**kwargs)

            button = Button(text='Klick mich!')
            button.bind(on_press=self.login)
            self.add_widget(button)

    def login(self, *args):
        App.get_running_app().login()