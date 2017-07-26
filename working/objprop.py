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
<PropTest>:
    test_butt: butt
    test_bl: bl
    orientation: 'vertical'
    Button:
        id: butt
        text: '1'
    Button:
        text: '2'
        on_release: root.update()
    Button:
        text: '3'
        on_press: root.change()
    BoxLayout:
        id: bl
        Button:
        Button:
""")

class PropTest(BoxLayout):
    test_butt = ObjectProperty()
    test_bl = ObjectProperty()

    def change(self):
        self.test_butt.text = 'i did it'

    def update(self):
        self.test_bl.clear_widgets()

    def on_test_butt(self, instance, value):
        print(self.test_butt)


class PropTestApp(App):
    def build(self):
        return PropTest()

if __name__ == '__main__':
    PropTestApp().run()
