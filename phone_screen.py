from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty
import re


dialer_screen_kv_ = """
    
# --- Call Menu-------------------------------------
<CallMenu@BoxLayout>:
    orientation: 'vertical'
    size_hint: None, None
    size: 75, 280
    pos: 165, 120
    Button:
        text: 'dial'
    Button:
        text: 'hang'
# ^-- Call Menu -----------------------------------^

# --- Dial Pad -------------------------------------    
<NumberButton@Button>
    id: btn
    num: '-1'
    on_release: root.change_number(self.num)
    halign: 'center'

<DialPad>:
    id: dial_pad
    phone_number: phonenumber
    orientation: 'vertical'
    size_hint: None, None
    size: 280, 280
    x: self.parent.center_x - self.width/2
    y: 120
    Label:
        id: phonenumber
        size_hint_y: None
        height: 40
        font_size: 30
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
# ^-- Dial Pad ------------------------------------^

<Dialer>:
    id: dialer
    PhoneMenu:
    CallMenu:
    DialPad:
    Button:
        id: contact_photo
        size_hint: None, None
        size: 170, 170
        pos: 600, 230
    Label:
        id: contact_name
        size_hint: None, None
        width: self.parent.ids.contact_photo.width
        height: 30
        x: self.parent.ids.contact_photo.x
        y: self.parent.ids.contact_photo.y - self.height-5
        text: 'default'
"""

class Dialer(Screen):
    pass

class DialPad(BoxLayout):
    phone_number = ObjectProperty(None)
    digitstring = ListProperty([])

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
        dp = self.parent.parent
        dp.digitstring.append(num)

speed_dial_kv_ = """
<SpeedDialButton@Button>:
    size_hint: None, None
    size: 75, 75
<SpeedDial>:
    id: speeddial
    
    PhoneMenu:
    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: 225, 275
        x: self.parent.center_x - self.width/2
        y: 120
        BoxLayout:
            SpeedDialButton: 
                text: 'List'
                size: 50, 50
                on_release: speed_contacts.cols = 1
            SpeedDialButton:
                text: 'Grid'
                size: 50, 50
                on_release: speed_contacts.cols = 3
        GridLayout:
            id: speed_contacts
            cols: 3
            size_hint: None, None
            size: 225, 225
            #x: self.parent.center_x - self.width/2
            #y: 120
            canvas:
                Color:
                    rgba: [1, 0, 0, 0.5]
                Line:
                    points: [self.x+ 75, self.y, self.x + 75, self.y+225]
                Line:
                    points: [self.x+ 75*2, self.y, self.x + 75*2, self.y+225]
                Line:
                    points: [self.x, self.y+75, self.x+225, self.y+75]
                Line:
                    points: [self.x, self.y+75*2, self.x+225, self.y+75*2]
                Line:
                    points: [self.x, self.y, self.x+225, self.y, self.x+225, self.y+225, self.x, self.y+225]
                    close: True
            SpeedDialButton:
            SpeedDialButton:
            SpeedDialButton:
            SpeedDialButton:
                    
"""

class SpeedDial(Screen):
    speed_cols = NumericProperty(3)

contacts_kv_ = """
<Contacts>:
    id: contacts
    PhoneMenu:
    Label:
        text: 'contacts'
"""
class Contacts(Screen):
    pass

settings_kv_ = """
<Settings>
    id: settings
    PhoneMenu:
    Label:
        text: 'settings'
"""
class Settings(Screen):
    pass

phone_screen_kv_ = """
# === Base Screen ==================================       
<PhoneScreen>:
    id: 'phone'
    FloatLayout:
        Image:
            source: 'rsc/screens/Menu_Phone.png'
            allow_stretch: False   
        HOMEButton:
            on_release: root.manager.current = 'home' 
        SETButton:
# === Base Screen ==================================
"""

class PhoneScreen(Screen):
    sm = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PhoneScreen, self).__init__(**kwargs)
        self.sm = ScreenManager()
        self.sm.add_widget(Dialer(name='dialer'))
        self.sm.add_widget(SpeedDial(name='speeddial'))
        self.sm.add_widget(Contacts(name='contacts'))
        self.sm.add_widget(Settings(name='settings'))
        self.sm.transition = NoTransition()
        self.add_widget(self.sm)


phone_screen_kv = """

# --- Phone Menu -----------------------------------
<PhoneMenuButton@Button>:
    text: 'default'
    
<PhoneMenu@BoxLayout>:
    orientation: 'vertical'
    size_hint: None, None
    size: 125, 190
    x: 20
    y: 210
    PhoneMenuButton:
        text: 'Phone'
        on_release: root.parent.manager.current = 'dialer'
    PhoneMenuButton:
        text: 'Speed Dial'
        on_release: root.parent.manager.current = 'speeddial'
    PhoneMenuButton:
        text: 'Contacts'
        on_release: root.parent.manager.current = 'contacts'
    PhoneMenuButton:
        text: 'Settings'
        on_release: root.parent.manager.current = 'settings'

""" + dialer_screen_kv_ + speed_dial_kv_ + contacts_kv_ + settings_kv_ + phone_screen_kv_
