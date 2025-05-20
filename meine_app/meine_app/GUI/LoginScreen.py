from tkinter import Button

from kivy.uix.boxlayout import BoxLayout


class LoginScreen(BoxLayout):
    def build(self):
        self.__loginButton = Button(text='Login')
        self.__loginButton.bind(on_press= self.parent.login)

        self.add_widget(self.__loginButton)
        return self