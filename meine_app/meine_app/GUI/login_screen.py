from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    def do_login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        # Dummy authentication (just printing for now)
        print(f"Username: {username}, Password: {password}")

        # Switch to home screen
        self.manager.current = "home"