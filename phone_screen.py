from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, ListProperty


phone_screen_kv = """
<NumberButton@Button>
    id: btn
    num: '-1'
    on_release: root.change_number(self.num)

<DialPad>:
    id: dial_pad
    phone_number: phonenumber
    orientation: 'vertical'
    Label:
        id: phonenumber
    GridLayout:
        id: phone_grid
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
    id: phone_screen
    DialPad:
"""


class DialPad(BoxLayout):
    phone_number = ObjectProperty(None)
    digitstring = ListProperty([])

    def format_(self):
        ds = self.digitstring
        pn = self.phone_number
        ds_str = ''.join(ds[:])

        mask = '%s' * len(ds)
        if ds[0] == '1':
            if len(ds) < 4:
                ds_str += ' '*(4-len(ds))
            mask = '%s (' + '%s'*(3  )'
        num = mask % tuple(ds_str)
        print(num)
        pn.text = num

    def on_digitstring(self, widget, *args):
        self.format_()

class NumberButton(Button):

    def change_number(self, num):
        dp = self.parent.parent
        dp.digitstring.append(num)


class PhoneScreen(Screen):
    pass
