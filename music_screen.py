import canbus

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

from kivy.animation import Animation

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty

from Common import SideMenu

ipod_screen_kv = """
<iPod>:
    Music_Screen_Menu_Button:
"""


class iPod(Screen):
    pass

radio_screen_kv = """
<Radio>:
    Music_Screen_Menu_Button:
"""


class Radio(Screen):
    pass


aux_screen_kv = """
<Aux>:
    Music_Screen_Menu_Button:
"""


class Aux(Screen):
    pass


music_menu_screen_kv = """
#<Music_Menu_Button@Button>:
#    size_hint: 1, None
#    height: 30
#    #pos_hint: 
    
<Music_Screen_Side_Menu>:    
    id: music_side_menu
    orientation: 'vertical'
    Button:
        text: 'iPod'
        on_press: 
            print(root.parent)
            #sidemenu.current_screen.manager.current = 'ipod'
            #sidemenu.dismiss()                    
    Button:
        text: 'radio'
        on_press: 
            #sidemenu.current_screen.manager.current = 'radio'
            #sidemenu.dismiss()                  
    Button:
        text: 'AUX'
        on_press: 
            #sidemenu.current_screen.manager.current = 'aux'
            #sidemenu.dismiss()                            

"""

class Music_Screen_Menu_Button(Button):
    pass


class Music_Screen_Side_Menu(BoxLayout):
    pass


class MusicScreen(Screen):
    sm = ObjectProperty(None)
    side_menu_content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)
        self.sm = ScreenManager()
        self.sm.add_widget(iPod(name='ipod'))
        self.sm.add_widget(Radio(name='radio'))
        self.sm.add_widget(Aux(name='aux'))
        self.sm.transition = NoTransition()
        self.add_widget(self.sm)
        self.menu_button = Music_Screen_Menu_Button()
        self.sidemenu = SideMenu()

    def open_side_menu(self):
        self.sidemenu.open()
        self.sidemenu.add_content_(Music_Screen_Side_Menu())


    def send_CANBUS(self, code):
        # TODO will translate buttun presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)

music_screen_kv = """

    
<Music_Screen_Menu_Button>:
    size_hint: None, None
    size: 30, 30
    pos: 20, 380
    text: 'menu'
    on_press: self.parent.parent.parent.open_side_menu()
        
        
# === Base Screen ==================================     
<MusicScreen>:
    id: music
    #side_menu_content: music_side_menu
    FloatLayout:
        Image:
            source: 'rsc/screens/Music.png'
            allow_stretch: False   
        HOMEButton:
            on_release: root.manager.current = 'home' 
        SETButton:
        
# === Base Screen ==================================
""" + music_menu_screen_kv + aux_screen_kv + radio_screen_kv + ipod_screen_kv
