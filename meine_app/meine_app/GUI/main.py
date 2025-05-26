from kivymd.app import *
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from login_screen import LoginScreen
from home_screen import HomeScreen
from PrdAuftr_screen import PrdAuftragScreen
#from meine_app.meine_app.test import ScrollButtonApp
from PrdAuftrView_screen import PrdAuftrViewScreen
from PrdLinie_screen import PrdLinieScreen

# Load .kv files
Builder.load_file("../kv/login_screen.kv")
Builder.load_file("../kv/home_screen.kv")

class MainApp(MDApp):
    def build(self):                                                                                                        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(PrdAuftragScreen(name="prdauftrag"))
        sm.add_widget(PrdAuftrViewScreen(a="auftrag",name="prdauftragView"))
        sm.add_widget(PrdLinieScreen(name="prdlinie"))

        return sm

if __name__ == "__main__":
    MainApp().run()