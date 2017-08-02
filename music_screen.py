
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

# from kivy.animation import Animation

from kivy.uix.boxlayout import BoxLayout

# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty

from side_menu import SideMenu, common_kv
import canbus

ipod_screen_kv = """

<iPod>:

"""


class iPod(Screen):
    pass

radio_screen_kv = """
<Radio>:

"""


class Radio(Screen):
    pass


aux_screen_kv = """
<Aux>:

"""


class Aux(Screen):
    pass


music_menu_screen_kv = """ 
<MusicScreenSideMenuContent>:    
    id: music_side_menu
    orientation: 'vertical'
    Button:
        text: 'iPod'
        on_press: 
            sidemenu.change_screen('ipod')
            sidemenu.dismiss()                    
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


class MusicScreenSideMenuContent(BoxLayout):
    pass


class MusicScreen(Screen):
    sm = ObjectProperty(ScreenManager())
    sidemenu = ObjectProperty(SideMenu(sm))

    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)
        self.sm.add_widget(iPod(name='ipod'))
        self.sm.add_widget(Radio(name='radio'))
        self.sm.add_widget(Aux(name='aux'))
        self.sm.transition = NoTransition()
        self.add_widget(self.sm)
        #self.sidemenu = SideMenu(self.sm)
        self.sidemenu.add_content_(MusicScreenSideMenuContent())

    def open_side_menu(self):
        self.sidemenu.open()

    def send_CANBUS(self, code):
        # TODO will translate button presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)


music_screen_kv = """
        
# === Base Screen ==================================     
<MusicScreen>:
    id: music
    on_leave: app.frontglass.remove_side_menu_button()
    FloatLayout:
        Image:
            source: 'rsc/screens/Music.png'
            allow_stretch: False   
        HOMEButton:
            on_release: root.manager.current = 'home' 
        SETButton:
        
# === Base Screen ==================================
    
""" + aux_screen_kv + radio_screen_kv + ipod_screen_kv + music_menu_screen_kv + common_kv

