from kivy.uix.screenmanager import Screen
from meine_app.meine_app.Util import Util

class LoginScreen(Screen):

    def do_login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        result = Util.getUserdata(username)



        print(result, "result")
        print(f"Username: {username}, Password: {password}")

        if password == None:
            self.manager.current = "gif_screen"
        if result:
            if password == result[1]:
                self.manager.current = "home"


        print(f"Username: {username}, Password: {password}")
        self.manager.current = "gif_screen"
        # Switch to home screen
        self.manager.current = "home"