from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.lang import Builder

from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics import Color
from kivy.graphics.texture import Texture

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

from kivy.properties import ListProperty, NumericProperty, StringProperty, ObjectProperty

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from climate_screen import climate_screen_kv, ClimateScreen
from music_screen import music_screen_kv, MusicScreen
from phone_screen import phone_screen_kv, PhoneScreen
from front_glass import front_glass_kv, FrontGlass

from side_menu import SideMenu

Builder.load_string("""
#:import partial functools
#:import SideMenuButton front_glass
<Logo>:
    source: 'rsc/logo/InfinityCliffLogoClear-Red.png'
    size_hint: None, None
    size: root.height, root.height
    center: root.center
    allow_stretch: True
    keep_ratio: False
    #opacity: 0.5
    


<HOMEButton@Button>
    size_hint_x: None
    size_hint_y: None        
    size: 40, 40
    pos: 350,10
    background_color: [1,1,1,0]
    Image:
        source: 'rsc/buttons/home.png'
        size: 40,40
        pos: 350,10

<SETButton@Button>
    size_hint_x: None
    size_hint_y: None        
    size: 40, 40
    pos: 410,10
    background_color: [1,1,1,0]
    Image:
        source: 'rsc/buttons/settings.png'
        size: 40,40
        pos: 410,10   

<MMButton@Button>
    size_hint_x: None
    size_hint_y: None        
    size: 280, 46
    text_size: 280,46
    valign: 'center'
    background_color: [0, 0, 0, 0]


<MENUButtons>
    HOMEButton:
    SETButton:
    
<HomeScreen>:
    id: 'home'
    size: 800, 480
    on_leave: app.frontglass.add_SideMenuButton()
    FloatLayout:
        size: 800, 480
        Image:
            source: 'rsc/screens/Main.png'
            allow_stretch: False 
        MMButton:
            pos: 0, 423
            text: '  Phone'
            on_release: root.manager.current = 'phone'
            halign: 'left'
        MMButton:
            pos: 520,423
            text: 'Navigation  '
            on_release: root.manager.current = 'nav'
            halign: 'right'
        MMButton:
            pos: 0, 9
            text: '  Music'
            on_release: root.manager.current = 'music'
            halign: 'left'
        MMButton:
            pos: 520, 9
            text: 'Climate  '
            on_release: root.manager.current = 'climate'
            halign: 'right'
            

<NavigationScreen>:
    id: 'nav'
    on_leave: app.frontglass.remove_SideMenuButton()
    FloatLayout:
        Image:
            source: 'rsc/screens/Menu_Nav.png'
            allow_stretch: False   
        Label:
            text: 'Navigation Screen'
        HOMEButton:
            on_release: root.manager.current = 'home' 

     

""" + climate_screen_kv + music_screen_kv + phone_screen_kv + front_glass_kv)


class NavigationScreen(Screen):
    sidemenu = ObjectProperty(SideMenu)


class HomeScreen(Screen):
    pass


class HOMEButton(Button):
    pass


class SettingsScreen(Screen):
    pass


class Console(FloatLayout):
    def __init__(self, **kwargs):
        super(Console, self).__init__(**kwargs)

# Create the screen manager
sm = ScreenManager()
sm.id = 'scrman'
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(PhoneScreen(name='phone'))
sm.add_widget(NavigationScreen(name='nav'))
sm.add_widget(MusicScreen(name='music'))
sm.add_widget(ClimateScreen(name='climate'))
sm.add_widget(SettingsScreen(name='settings'))
sm.transition = NoTransition()
sm.index = -1


class ConsoleApp(App):
    carputer = None
    init_state = {}
    scrman = ObjectProperty(sm)
    scrcur = ObjectProperty(sm.current)
    frontglass = ObjectProperty()

    def build(self):
        self.root = Console()
        self.frontglass = FrontGlass()
        self.root.add_widget(self.frontglass, index=0)
        self.root.add_widget(sm, index=1)
        return self.root

    def set_controller(self, controller):
        self.carputer = controller

    def startup(self, init_state):
        climate = sm.get_screen('climate')
        climate.startup(init_state['climate'])
        self.init_state = init_state

    def on_enter(self):
        print('sadfsd')
if __name__ == '__main__':
    ConsoleApp().run()
