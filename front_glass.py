from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from functools import partial
# from kivy.uix.label import Label

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty
from kivy.factory import Factory
from side_menu import SideMenu


front_glass_kv = """
#:include front_glass.kv
"""


class FrontGlass(FloatLayout):
    front_glass = ObjectProperty()
    normal_pane = ObjectProperty()
    quit_pane = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            on_touch_down=self.create_clock,
            on_touch_up=self.delete_clock)
        self.quit_pane = Factory.QuitPane()
        self.touch = None

    def show_Normal_Pane(self):
        self.clear_widgets()
        self.add_widget(self.normal_pane)

    def create_clock(self, widget, touch, *args):
        self.touch = touch
        callback = partial(self.quit_pane.open, self.touch)
        Clock.schedule_once(callback, 2)
        self.touch.ud['event'] = callback

    def delete_clock(self, widget, touch, *args):
        if self.touch:
            Clock.unschedule(touch.ud['event'])
            self.touch = None
