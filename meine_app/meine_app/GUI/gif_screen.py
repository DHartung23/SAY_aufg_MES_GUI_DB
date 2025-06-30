
from kivy.uix.screenmanager import Screen


class GifScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_enter(self, *args):

        print("GifScreen betreten.")

        Clock.schedule_once(self.go_back_after_gif, 5)

    def on_leave(self, *args):
        # Diese Methode wird aufgerufen, wenn der Screen verlassen wird
        print("GifScreen verlassen.")
        # Hier könntest du z.B. einen geplanten Clock-Event abbrechen, falls nötig.

    def go_back_after_gif(self, dt):
        # Diese Methode wird durch Clock.schedule_once aufgerufen
        self.manager.current = "gif_screen"