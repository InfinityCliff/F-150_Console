from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

# from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
# from kivy.graphics import Color
# from kivy.graphics.texture import Texture

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

from kivy.properties import ListProperty, NumericProperty, StringProperty, ObjectProperty

from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.image import Image

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView

from climate_screen import climate_screen_kv, ClimateScreen
from music_screen import music_screen_kv, MusicScreen
from phone_screen import phone_screen_kv, PhoneScreen


#from side_menu import SideMenu
from functools import partial

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

<NavigationScreen>:
    id: 'nav'
    on_leave: app.frontglass.remove_side_menu_button()
    FloatLayout:
        Image:
            source: 'rsc/screens/Menu_Nav.png'
            allow_stretch: False   
        Label:
            text: 'Navigation Screen'
        HOMEButton:
            on_release: root.manager.current = 'home' 

     

    
""" + climate_screen_kv + music_screen_kv + phone_screen_kv)


# Front Glass  ------------------------------------------

class NormalPane(FloatLayout):
    pass


class QuitPane(ModalView):
    pass


class FrontGlass(FloatLayout):
    normal_pane = ObjectProperty()
    quit_pane = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            on_touch_down=self.create_clock,
            on_touch_up=self.delete_clock)
        #self.quit_menu = QuitMenu()
        #self.side_menu = SideMenu()
        self.normal_pane = NormalPane()
        self.quit_pane = QuitPane()
        self.show_Normal_Pane()
        self.touch = None

    def show_Normal_Pane(self):
        self.clear_widgets()
        self.add_widget(self.normal_pane)

    def create_clock(self, widget, touch, *args):
        self.touch = touch
        callback = partial(self.quit_pane.open, self.touch)
        Clock.schedule_once(callback, 2)
        self.touch.ud['event'] = callback

    def delete_clock(self, widget, touch, *args):
        if self.touch:
            Clock.unschedule(touch.ud['event'])
            self.touch = None

            #def add_side_menu_button(self):

            #    self.add_widget(self.side_menu_button)

            #def remove_side_menu_button(self):
            #    self.remove_widget(self.side_menu_button)
# ^Front Glass  ----------------------------------------^

class NavigationScreen(Screen):
    sidemenu = ObjectProperty()


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
#sm = ScreenManager()
#sm.id = 'scrman'
#sm.add_widget(HomeScreen(name='home'))
#sm.add_widget(PhoneScreen(name='phone'))
#sm.add_widget(NavigationScreen(name='nav'))
#sm.add_widget(MusicScreen(name='music'))
#sm.add_widget(ClimateScreen(name='climate'))
#sm.add_widget(SettingsScreen(name='settings'))
#sm.transition = NoTransition()
#sm.index = -1

class Manager(ScreenManager):
    home_screen = ObjectProperty()
    phone_screen = ObjectProperty()
    music_screen = ObjectProperty()

class ConsoleRoot(FloatLayout):
    sm = ObjectProperty()
    front_glass = ObjectProperty()
    current = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = Manager()
        #self.sm.add_widget(HomeScreen(name='home'))
        #self.sm.add_widget(PhoneScreen(name='phone'))
        self.sm.transition = NoTransition()
        #self.current = self.sm.current
        self.front_glass = FrontGlass()
        self.add_widget(self.sm)
        self.add_widget(self.front_glass)

    def on_current(self, widget, ev):
        print(widget)
        print(ev)
        print(self.sm.current_screen)


class ConsoleApp(App):
    pass


class TempfromConssoleApp():
    carputer = None
    init_state = {}
    #sm = ObjectProperty(sm)
    # scrcur = ObjectProperty(sm.current)
    frontglass = ObjectProperty(FrontGlass())

    def build(self):
        self.root = Console()
        self.root.add_widget(self.frontglass, index=0)
        self.root.add_widget(self.sm, index=1)
        return self.root

    def set_controller(self, controller):
        self.carputer = controller

    def startup(self, init_state):
        #climate = sm.get_screen('climate')
        #climate.startup(init_state['climate'])
        self.init_state = init_state

if __name__ == '__main__':
    ConsoleApp().run()
