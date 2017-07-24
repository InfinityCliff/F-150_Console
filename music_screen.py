import canbus

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.properties import ObjectProperty


ipod_screen_kv = """
<iPod>:
    Menu_Button:
"""


class iPod(Screen):
    pass

radio_screen_kv = """
"""


class Radio(Screen):
    pass


aux_screen_kv = """
"""


class Aux(Screen):
    pass


music_menu_screen_kv = """
<Menu_Button@Button>:
    size_hint: None, None
    #pos_hint: None, None
    size: 50, 30
<Music_Menu>:
    id: 'menu'
    size_hint: None, 1
    height: 400
    
    canvas:
        Color: 
            rgba: [1,0,0,.5]
        Rectangle:
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        Menu_Button:
            text: 'iPod'
            
            
            # FINDING THE RIGHT PATH TO MANAGER
            on_press: root.parent.manager.current = 'ipod'
            
            
            
        Menu_Button:
            text: 'Radio'
            on_press: root.parent.manager.current = 'radio'
        Menu_Button:
            text: 'AUX'
            on_press: root.parent.manager.current = 'aux'
        Menu_Button:
"""


class Music_Menu(Screen):
    pass


class MusicScreen(Screen):
    sm = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)
        self.sm = ScreenManager()
        self.sm.add_widget(iPod(name='ipod'))
        self.sm.add_widget(Radio(name='radio'))
        self.sm.add_widget(Aux(name='aux'))
        self.sm.add_widget(Music_Menu(name='menu'))
        self.sm.transition = NoTransition()
        self.add_widget(self.sm)

    def send_CANBUS(self, code):
        # TODO will translate buttun presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)

music_screen_kv = """
    
<Menu_Button@Button>:
    size_hint: None, None
    #pos_hint: None, None
    size: 30, 30
    pos: 20, 380
    text: 'menu'
    on_press: root.parent.manager.current = 'menu'

        
# === Base Screen ==================================     
<MusicScreen>:
    id: music
    FloatLayout:
        Image:
            source: 'rsc/screens/Music.png'
            allow_stretch: False   
        HOMEButton:
            on_release: root.manager.current = 'home' 
        SETButton:
        
# === Base Screen ==================================
""" + music_menu_screen_kv + aux_screen_kv + radio_screen_kv + ipod_screen_kv
