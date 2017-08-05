from kivy.factory import Factory

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import ObjectProperty

from side_menu import SideMenu
from console_screen import ConsoleScreen

import canbus

music_screen_kv = """
#:include music_screen.kv
"""


class MusicManager(ScreenManager):
    ipod_screen = ObjectProperty()
    radio_screen = ObjectProperty()
    aux_screen = ObjectProperty()


class MusicScreen(ConsoleScreen):
    mm = ObjectProperty()
    screen_side_menu = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mm = MusicManager()
        self.add_widget(self.mm)
        self.screen_side_menu = SideMenu()
        self.screen_side_menu.add_content(Factory.MusicScreenSideMenu())
        self.screen_side_menu.set_manager(self.mm)
        self.add_widget(self.screen_side_menu)


    def send_CANBUS(self, code):
        # TODO will translate button presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)




