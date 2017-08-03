from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.factory import Factory

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# from kivy.core.window import Window
from kivy.config import Config

# from kivy.uix.widget import Widget
# from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.properties import ObjectProperty, ListProperty, NumericProperty

from kivy.graphics import InstructionGroup, Color, Rectangle, Line

import re

phone_screen_kv = """
#:include phone_screen.kv
"""


class Dialer(Screen):
    pass


class DialPad(FloatLayout):
    phone_number = ObjectProperty(None)
    digitstring = ListProperty()

    def format_(self):
        ds = self.digitstring
        pn = self.phone_number
        ds_str = ''.join(ds[:]) + ' ' * ((11 if ds[0] == '1' else 10) - len(ds))

        if ds[0] == '1':
            mask = '%s (%s%s%s) %s%s%s %s%s%s%s'
            if len(ds) > 6:
                mask = '%s (%s%s%s) %s%s%s-%s%s%s%s'
        elif len(ds) < 3:
            mask = '%s%s%s%s %s%s%s%s%s%s'
        elif len(ds) < 8:
            mask = '%s%s%s-%s%s%s%s %s%s%s'
        else:
            mask = '(%s%s%s) %s%s%s-%s%s%s%s'

        num = mask % tuple(ds_str)
        num = re.sub(r'\s+$', '', num)
        pn.text = num

    def on_digitstring(self, widget, *args):
        self.format_()


class NumberButton(Button):

    def change_number(self, num):
        dp = self.parent.parent.parent
        dp.digitstring.append(num)


class Grid1(InstructionGroup):

    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y


class Favorites(Screen):
    speed_cols = NumericProperty(3)
    sc = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Grid1 = InstructionGroup()
        self.Grid1.add(Color(1, 0, 0, 0.5))
        self.Grid1.add(Line(points=[self.x, self.y + 75, self.x + 225, self.y + 75]))
        self.Grid1.add(Line(points=[self.x, self.y + 75*2, self.x + 225, self.y + 75*2]))
        self.Grid1.add(Line(points=[self.x, self.y, self.x+225, self.y, self.x+225, self.y+225, self.x, self.y+225]))

        self.Grid2 = InstructionGroup()
        self.Grid2.add(Color(1, 0, 0, 0.5))
        self.Grid2.add(Rectangle(pos=(self.x, self.y)))
        self.Grid2.add(Line(points=[self.x + 75, self.y, self.x + 75, self.y+225]))
        self.Grid2.add(Line(points=[self.x + 75*2, self.y, self.x + 75*2, self.y+225]))
        self.Grid2.add(Line(points=[self.x, self.y + 75, self.x+225, self.y + 75]))
        self.Grid2.add(Line(points=[self.x, self.y + 75*2, self.x + 225, self.y + 75*2]))
        self.Grid2.add(Line(points=[self.x, self.y, self.x + 225, self.y, self.x + 225, self.y + 225, self.x,
                                    self.y + 225], close=True))

        # self.sc.canvas.add(self.Grid2)


class Contacts(Screen):

    def __init__(self, **kwargs):
        super(Contacts, self).__init__(**kwargs)
        Config.get('kivy', 'keyboard_mode'),
        Config.get('kivy', 'keyboard_layout')


class PhoneManager(ScreenManager):
    dialer_screen = ObjectProperty()
    favorites_screen = ObjectProperty()
    contacts_screen = ObjectProperty()


class PhoneScreen(Screen):
    pm = ObjectProperty()

    def __init__(self, **kwargs):
        super(PhoneScreen, self).__init__(**kwargs)
        self.pm = PhoneManager()
        self.add_widget(self.pm)

    def get_side_menu(self):
        return Factory.PhoneScreenSideMenu(), self.pm

