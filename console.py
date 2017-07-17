from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics import Color
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
from kivy.graphics.texture import Texture

from kivy.uix.screenmanager import NoTransition

from climate_screen import climate_screen_kv, ClimateScreen
from music_screen import music_screen_kv

Builder.load_string("""
#:import partial functools

<Logo>:
    source: 'rsc/logo/InfinityCliffLogoClear-Red.png'
    size_hint: None, None
    size: root.height, root.height
    center: root.center
    allow_stretch: True
    keep_ratio: False
    opacity: 0.5
    
<FrontGlass>:
    id: frontglass
    FloatLayout:
        id: frontglasslayout 

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
            
<PhoneScreen>:
    id: 'phone'
    FloatLayout:
        Image:
            source: 'rsc/screens/Menu_Phone.png'
            allow_stretch: False   
        Label:
            text: 'Phone Screen'
        HOMEButton:
            on_release: root.manager.current = 'home' 
        SETButton:
        
<NavigationScreen>:
    id: 'nav'
    FloatLayout:
        Image:
            source: 'rsc/screens/Menu_Nav.png'
            allow_stretch: False   
        Label:
            text: 'Navigation Screen'
        HOMEButton:
            on_release: root.manager.current = 'home' 
            
<QuitMenu>:
    BoxLayout:
        id: popup
        size_hint: None, None
        orientation: 'vertical'
        Button:
            id: quit_button
            on_release: quit()
            size_hint: None, None
            size: self.texture_size
            Image:
                size_hint: None, None
                size: self.texture_size
                source: 'rsc/buttons/quit_car_pc.png'
                pos: self.parent.pos
        Button:
            id: cancel
            size_hint: None, None
            size: quit_button.texture_size
            Image:
                size_hint: None, None
                size: self.texture_size
                source: 'rsc/buttons/cancel.png'
                pos: self.parent.pos
                                        
""" + climate_screen_kv + music_screen_kv)


class Gradient(object):
    @staticmethod
    def horizontal(rgba_left, rgba_right):
        texture = Texture.create(size=(2, 1), colorfmt="rgba")
        pixels = rgba_left + rgba_right
        pixels = [chr(int(v * 255)) for v in pixels]
        buf = ''.join(pixels)
        texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
        return texture

    @staticmethod
    def vertical(rgba_top, rgba_bottom):
        texture = Texture.create(size=(1, 2), colorfmt="rgba")
        pixels = rgba_bottom + rgba_top
        pixels = [chr(int(v * 255)) for v in pixels]
        buf = ''.join(pixels)
        texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
        return texture

class CTLButton(Button):
    def __init__(self, **kwargs):
        super(CTLButton, self).__init__(**kwargs)
        texture = Texture.create(size=(64, 64))

        size = 64*64*3
        buf = [int(x*255/size) for x in range(size)]
        buf = b''.join(map(chr, buf))

        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=(64, 64))


class HomeScreen(Screen):
    pass


class HOMEButton(Button):
    pass


class PhoneScreen(Screen):
    pass


class NavigationScreen(Screen):
    pass


class MusicScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class Logo(Image):
    pass


class QuitMenu(BoxLayout):
    pass


class FrontGlass(Label):
    def __init__(self, **kwargs):
        super(FrontGlass, self).__init__(**kwargs)
        self.id = 'frontglass'
        self.bind(
            on_touch_down=self.create_clock,
            on_touch_up=self.delete_clock)
        self.menu_up = False

    def create_clock(self, widget, touch, *args):
        callback = partial(self.menu, touch)
        Clock.schedule_once(callback, 2)
        touch.ud['event'] = callback

    def delete_clock(self, widget, touch, *args):
        Clock.unschedule(touch.ud['event'])

    def menu(self, touch, *args):
        with self.canvas.before:
            Color(0.05, 0.05, 0.05, 0.5)
            Rectangle(size=self.parent.size)
        logo = Logo()
        self.add_widget(logo)
        logo.size = self.parent.height-145, self.parent.height-145
        logo.center = self.parent.center
        quitmenu = QuitMenu(center=touch.pos)
        cancel = quitmenu.ids.cancel
        cancel.bind(on_release=partial(self.cancel_menu, quitmenu, logo))

        self.add_widget(quitmenu)

    def cancel_menu(self, widget, logo, *args):
        self.remove_widget(widget)
        self.remove_widget(logo)
        self.canvas.before.clear()


class Console(FloatLayout):
    def __init__(self, **kwargs):
        super(Console, self).__init__(**kwargs)

# Create the screen manager
sm = ScreenManager()
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

    def build(self):
        self.root = Console()
        self.root.add_widget(FrontGlass(), index=0)
        self.root.add_widget(sm, index=1)
        return self.root

    def set_controller(self, controller):
        self.carputer = controller

    def startup(self, init_state):
        climate = sm.get_screen('climate')
        climate.startup(init_state['climate'])
        self.init_state = init_state

if __name__ == '__main__':
    ConsoleApp().run()