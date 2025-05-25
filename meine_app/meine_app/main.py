from kivymd.app import *
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen

# Load .kv files
Builder.load_file("../kv/login_screen.kv")
Builder.load_file("../kv/home_screen.kv")

class MainApp(MDApp):
    def build(self):                                                                                                        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    MainApp().run()