from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu1 = None
        self.menu2 = None
    def on_kv_post(self, base_widget):
        prod_items = [
            {"viewclass": "OneLineListItem", "text": "Add", "on_release": lambda: self.select_prod_option("Add")},
            {"viewclass": "OneLineListItem", "text": "View", "on_release": lambda: self.select_prod_option("View")}         
            ]
        self.prod_menu = MDDropdownMenu(
            caller=self.ids.prod_menu_field,
            items=prod_items,
            width_mult=3,
            max_height=dp(150),
        )

        order_items = [
            {"viewclass": "OneLineListItem", "text": "Add", "on_release": lambda: self.select_order_option("Add")},
            {"viewclass": "OneLineListItem", "text": "View", "on_release": lambda: self.select_order_option("View")},
        ]
        self.order_menu = MDDropdownMenu(
            caller=self.ids.order_menu_field,
            items=order_items,
            width_mult=3,
            max_height=dp(150),
        )

    def open_prod_menu(self):
        self.prod_menu.open()

    def open_order_menu(self):
        self.order_menu.open()

    def select_prod_option(self, option):
        self.ids.prod_menu_field.text = option
        self.prod_menu.dismiss()
        print(f"Production Line Option Selected: {option}")
        if option == "Add":
            return self.add_prod()
        print(option)
        # Add logic here — open new screen, show popup, etc.

    def select_order_option(self, option):
        self.ids.order_menu_field.text = option
        self.order_menu.dismiss()
        print(f"Order Option Selected: {option}")
        # Add logic here too
