from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.factory import Factory

# from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
# from kivy.graphics import Color
# from kivy.graphics.texture import Texture

from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.screenmanager import NoTransition

from kivy.properties import ListProperty, NumericProperty, StringProperty, ObjectProperty

from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.image import Image

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView

from front_glass import front_glass_kv, FrontGlass
from side_menu import side_menu_kv
from music_screen import music_screen_kv
from phone_screen import phone_screen_kv
from climate_screen import climate_screen_kv

from functools import partial

Builder.load_string("""
""" + front_glass_kv + side_menu_kv + music_screen_kv + phone_screen_kv + climate_screen_kv)





class HomeScreen(Screen):
    def get_side_menu(self):
        return(Factory.HomeScreenSideMenu(), self.manager)


class Console(FloatLayout):
    def __init__(self, **kwargs):
        super(Console, self).__init__(**kwargs)


class Manager(ScreenManager):
    home_screen = ObjectProperty()
    music_screen = ObjectProperty()
    phone_screen = ObjectProperty()
    climate_screen = ObjectProperty()

class ConsoleRoot(FloatLayout):
    sm = ObjectProperty()
    front_glass = ObjectProperty()
    active_screen = ObjectProperty()
    side_menu_controller = ObjectProperty()
    active_manager = ObjectProperty()
    #test = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = Manager()
        self.front_glass = FrontGlass()
        self.add_widget(self.sm)
        self.add_widget(self.front_glass)

    def on_active_screen(self, widget, screen, *args):
        print('on_active_screen')
        print(widget)
        print(screen)
        #self.side_menu_controller.update_menu()

class ConsoleApp(App):
    pass

if __name__ == '__main__':
    ConsoleApp().run()
