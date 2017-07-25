from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from functools import partial
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy import require



Builder.load_string("""
<Insert1>:
    orientation: 'vertical'
    Button:
        text: '1'
    Button:
        text: '2'        
    Button:
        text: '3'

<Insert2>:
    orientation: 'vertical'
    Button:
        text: '4'
    Button:
        text: '5'        
    Button:
        text: '6'

""")

class Insert1(BoxLayout):
    pass

class Insert2(BoxLayout):
    pass

class InterfaceManager(BoxLayout):

    def __init__(self, **kwargs):
        super(InterfaceManager, self).__init__(**kwargs)

        self.b_one = Button(text='show 2')
        self.one = Insert1()
        self.b_one.bind(on_release=self.show_two)

        self.b_two = Button(text='show 1')
        self.two = Insert2()
        self.b_two.bind(on_release=self.show_one)

        self.add_widget(self.one)
        self.add_widget(self.b_one)

    def show_one(self, button):
        self.clear_widgets()
        self.add_widget(self.one)
        self.add_widget(self.b_one)

    def show_two(self, button):
        self.clear_widgets()
        self.add_widget(self.two)
        self.add_widget(self.b_two)


class InsertApp(App):
    def build(self):
        return InterfaceManager()

if __name__ == '__main__':
    InsertApp().run()
