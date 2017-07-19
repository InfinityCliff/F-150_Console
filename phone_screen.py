from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty


phone_screen_kv = """
<NumberButton@Button>
    id: btn
    num: '-1'
    on_release: root.phone_number = root.phone_number + self.num

<DialPad>:
    orientation: 'vertical'
    btn: btn
    Label:
        text: btn.phone_number
    GridLayout:
        cols: 3
        NumberButton:
            num: '1'
            text: "1\\n"
        NumberButton:
            num: '2'
            text: "2\\nABC"
        NumberButton:
            num: '3'
            text: "3\\nDEF"
        NumberButton:
            num: '4'
            text: "4\\nGHI"
        NumberButton:
            num: '5'
            text: "5\\nJKL"
        NumberButton:
            num: '6'
            text: "6\\nMNO"        
        NumberButton:
            num: '7'
            text: "7\\nPQRS"
        NumberButton:
            num: '8'
            text: "8\\nTUV"
        NumberButton:
            num: '9'
            text: "9\\nWXYZ"
        NumberButton:
            num: '*'
            text: "*\\n"
        NumberButton:
            num: '0'
            text: "0\\n+"
        NumberButton:
            num: '#'
            text: "#\\n"

<PhoneScreen>:
    DialPad:
"""

class DialPad(BoxLayout):
    btn = ObjectProperty(None)


class NumberButton(Button):
    phone_number = StringProperty("")

    def __init__(self, **kwargs):
        super(NumberButton, self).__init__(**kwargs)

    def on_phone_number(self, widget, *args):
        print(self.phone_number)


class PhoneScreen(Screen):
    def __init__(self, **kwargs):
        super(PhoneScreen, self).__init__(**kwargs)
