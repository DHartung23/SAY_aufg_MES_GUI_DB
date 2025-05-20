from tkinter import Button
from turtle import Screen

from kivy.uix.screenmanager import ScreenManager


class LoginScreen(Screen):
    def build(self):
        self.__loginButton = Button(text='Login')
        self.__loginButton.bind(on_press= self.parent.login)
        return self.__loginButton