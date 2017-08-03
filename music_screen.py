from kivy.factory import Factory

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import ObjectProperty

import canbus

music_screen_kv = """
#:include music_screen.kv
"""


class MusicManager(ScreenManager):
    ipod_screen = ObjectProperty()
    radio_screen = ObjectProperty()
    aux_screen = ObjectProperty()


class MusicScreen(Screen):
    mm = ObjectProperty()
    #sidemenu = ObjectProperty()

    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)
        self.mm = MusicManager()
        self.add_widget(self.mm)

    def get_side_menu(self):
        return Factory.MusicScreenSideMenu(), self.mm

    def send_CANBUS(self, code):
        # TODO will translate button presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)




