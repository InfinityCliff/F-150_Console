from kivy.app import App

from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button
from kivy.uix.widget import Widget

side_menu_kv = """
#:include side_menu.kv
"""


class SideMenuContent(Popup):
    active_manager = ObjectProperty()

    def set_manager(self, manager):
        self.active_manager = manager


class SideMenu(FloatLayout):
    sidemenu = ObjectProperty()
    screen = ObjectProperty()

    def __init__(self, get_screen=None, **kwargs):
        super().__init__(**kwargs)
        self.sidemenu = SideMenuContent()

    def add_content(self, menu_content):
        self.sidemenu.menu_content.add_widget(menu_content)

    def show_side_menu(self):
        self.sidemenu.open()

    def set_manager(self, manager):
        self.active_manager = manager
        self.sidemenu.set_manager(self.active_manager)



