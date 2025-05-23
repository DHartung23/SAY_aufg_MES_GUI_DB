from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class ScrollButtonApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        scroll_view = ScrollView(size_hint=(1, 1))

        # Container für Buttons
        button_container = BoxLayout(orientation='vertical', size_hint_y=None)
        button_container.bind(minimum_height=button_container.setter('height'))

        # Fensterhöhe zum Berechnen der Buttonhöhe (20% davon)
        button_height = Window.height * 0.2

        # Beispielsweise 10 Buttons
        "TODO:"
        "Noah: die sschleife sachen aus DB holen"


        for i in range(10):
            btn = Button(text=f"Button {i+1}", size_hint_y=None, height=button_height)
            button_container.add_widget(btn)

        scroll_view.add_widget(button_container)
        root.add_widget(scroll_view)

        return root

if __name__ == '__main__':
    ScrollButtonApp().run()