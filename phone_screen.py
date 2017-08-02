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


dialer_screen_kv_ = """
    
# --- Call Menu-------------------------------------
<CallButton@Button>:
    size_hint: None, None
    size: 150, 100
    pos: 50, 80
    text: 'dial'

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
    size_hint: None, None
    size: 280, 280
    x: self.parent.center_x - self.width/2
    y: 120
    Button:
        size_hint: None, None
        size: 40,40
        pos_hint: {'right': 1, 'top': 1}
        text: '<-'
        on_press: phonenumber.text = phonenumber.text[:-1]
    BoxLayout:
        orientation: 'vertical'
        size: self.parent.size
        pos: self.parent.pos
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
    CallButton:
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

speed_dial_kv_ = """

<SpeedDialMenuButton@Button>:

<SpeedDialButton@Button>:

<SpeedDial>:
    id: speeddial
    sc: speed_contacts
    PhoneMenu:
    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: 225, 275
        x: self.parent.center_x - self.width/2
        y: 120
        BoxLayout:
            size_hint: None, 0.25
            pos_hint: {'top': 1}
            SpeedDialMenuButton: 
                text: 'List'
                on_release: 
                    speed_contacts.cols = 1
                    #speed_contacts.canvas.clear()
                    #speed_contacts.canvas.add(root.Grid1)
            SpeedDialMenuButton:
                text: 'Grid'
                on_release: 
                    speed_contacts.cols = 3
                    #speed_contacts.canvas.clear()
                    #speed_contacts.canvas.add(root.Grid2)
        ScrollView:
            viewport_size: 225, 225
            GridLayout:
                id: speed_contacts
                cols: 3
                row_default_height: 75
                row_force_default: True
                size_hint: None, None
                size: 225, 225
                SpeedDialButton:
                SpeedDialButton:
                SpeedDialButton:
                SpeedDialButton:       
"""


class Grid1(InstructionGroup):

    def __init__(self, x, y, **kwargs):
        super(Grid1, self).__init__(**kwargs)
        self.x = x
        self.y = y


class SpeedDial(Screen):
    speed_cols = NumericProperty(3)
    sc = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SpeedDial, self).__init__(**kwargs)

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

contacts_kv_ = """
#:import vkb kivy.uix.vkeyboard.VKeyboard

<Contacts>:
    id: contacts
    PhoneMenu:
    BoxLayout:
        id: contact_base
        orientation: 'vertical'
        size: 635, 340
        pos: 165, 70
        BoxLayout:
            size_hint: None, None
            #pos_hint: None, None
            size: 635, 340
            pos: 165, 70
            orientation: 'vertical'
            BoxLayout:
                size_hint: 1, None
                height: 40
                Button:
                    text: 'Groups'
                    size_hint: None, 1
                TextInput:
                    text: 'Search'
                    size_hint: 0.75, 1
                    halign: 'center'
                    on_focus:
                        self.text = '' if self.focus else 'Search'
            ScrollView:
                BoxLayout:
                    orientation: 'vertical'
                    Button:
                    Button:
                    Button:
                    Button:
                    Button:
                    Button:
                    Button:
                    Button:
                    Button: 
"""


class Contacts(Screen):

    def __init__(self, **kwargs):
        super(Contacts, self).__init__(**kwargs)
        Config.get('kivy', 'keyboard_mode'),
        Config.get('kivy', 'keyboard_layout')

settings_kv_ = """
<Settings>
    id: settings
    PhoneMenu:
    Label:
        text: 'settings'
"""


class Settings(Screen):
    pass


class SideMenuContent(BoxLayout):
    pass


class PhoneScreen(Screen):
    sm = ObjectProperty(ScreenManager())
    side_menu_content = ObjectProperty()

    def __init__(self, **kwargs):
        super(PhoneScreen, self).__init__(**kwargs)
        self.sm.add_widget(Dialer(name='dialer'))
        self.sm.add_widget(SpeedDial(name='speeddial'))
        self.sm.add_widget(Contacts(name='contacts'))
        self.sm.add_widget(Settings(name='settings'))
        self.sm.transition = NoTransition()
        self.add_widget(self.sm)
        #self.sidemenu = SideMenu(self.sm)
        self.side_menu_content = SideMenuContent()

phone_screen_kv = """

# --- Phone Menu -----------------------------------
# Phone Screen  -----------------------------------------
<SideMenuContent>:
    Button:
        text: 'phone SM'
        
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
        
<PhoneScreen>:
    #id: 'phone'
    #on_leave: app.root.front_glass.remove_SideMenuButton()
    FloatLayout:
        Image:
            source: 'rsc/screens/Menu_Phone.png'
            allow_stretch: False   
        HOMEButton:
            on_release: root.manager.current = 'home' 
        SETButton:
        
# ^Phone Screen  ---------------------------------------^ 


""" + dialer_screen_kv_ + speed_dial_kv_ + contacts_kv_ + settings_kv_
