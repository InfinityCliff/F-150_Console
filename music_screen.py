from kivy.factory import Factory

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty, StringProperty

from kivy.uix.button import Button

from side_menu import SideMenu
from console_screen import ConsoleScreen

import canbus

music_screen_kv = """
#:include music_screen.kv
"""

class SearchBar(BoxLayout):
    def add_AlphaButtons(self, widget):
        for x in '#ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            widget.add_widget(Button(text=x))

class MusicManager(ScreenManager):
    ipod_screen = ObjectProperty()
    radio_screen = ObjectProperty()
    aux_screen = ObjectProperty()

class IpodScreen(Screen):
    album_cover = StringProperty("")
    play_mode = StringProperty("Shuffle Song")

    def PlayAlbum(self):
        print('switch to first song and play ablum')

    def ShuffleSongs(self):
        print('Shuffle all songs on Ipod')

    def DoubleShuffle(self):
        print('Shuffle all songs, with two from each artist')

    def AlbumShuffle(self):
        print('shuffle all albums')

class MusicScreen(ConsoleScreen):
    mm = ObjectProperty()
    screen_side_menu = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mm = MusicManager()
        self.add_widget(self.mm)
        self.screen_side_menu = SideMenu(self.get_screen)
        self.screen_side_menu.add_content(Factory.MusicScreenSideMenu())
        self.screen_side_menu.set_manager(self.mm)
        self.add_widget(self.screen_side_menu)

    def get_screen(Self):
        print(self)

    def Shuffle(self):
        pass

    def Double_Shuffle(self):
        pass

    def Album_Shuffle(self):
        pass

    def Play_Album(self):
        pass

    def send_CANBUS(self, code):
        # TODO will translate button presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)




