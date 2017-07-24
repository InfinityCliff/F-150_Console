import canbus

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

from kivy.animation import Animation

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty


ipod_screen_kv = """
<iPod>:
    Menu_Button:
"""


class iPod(Screen):
    pass

radio_screen_kv = """
<Radio>:
    Menu_Button:
"""


class Radio(Screen):
    pass


aux_screen_kv = """
<Aux>:
    Menu_Button:
"""


class Aux(Screen):
    pass


music_menu_screen_kv = """
<Music_Menu_Button@Button>:
    size_hint: 1, None
    height: 30
    #pos_hint: 
    
<Music_Menu_Popup@Popup>:
    id: menu
    size_hint: None, 1
    width: 150 
    pos_hint: {'x': 0}
    x: 0
    title: 'Music\\nMenu'
    halign: 'center'
    
    canvas.after:
        Color:
            rgba: [1,0,0,.25]
        Rectangle:
            size: self.size
            pos: self.pos    
    BoxLayout:
        canvas.after:
            Color:
                rgba: [0,1,0,.25]
            Rectangle:
                size: self.size
                pos: self.pos 
        BoxLayout:
            pos_hint: {'center_y': 0.5}
            size_hint_y: None
            height: 90
            size_hint_x: None
            width: 100
            BoxLayout:
                orientation: 'vertical'
                Button:
                    text: 'iPod'
                    on_press: 
                        menu.current_screen.manager.current = 'ipod'
                        menu.dismiss()                    
                Button:
                    text: 'radio'
                    on_press: 
                        menu.current_screen.manager.current = 'radio'
                        menu.dismiss()                  
                Button:
                    text: 'AUX'
                    on_press: 
                        menu.current_screen.manager.current = 'aux'
                        menu.dismiss()                            
        Button:
            text: '<<'
            on_press:
                menu.parent.remove_widget(menu)
                #menu.dismiss()   

"""

class Menu_Button(Button):
    pass

class Music_Menu_Popup(Popup):
    pass
    #def __init__(self, **kwargs):
    #    super(Music_Menu_Popup, self).__init__(**kwargs)

    ##def on_open(self):
     #   print('open')
        #anim = Animation(x=200, y=0)
        #anim.start(self)

    #def on__anim_alpha(self, instance, value):
    #    print('anim_alpha')
        #anim = Animation(x=200, y=0)
        #anim.start(self)
    #    if value == 0 and self._window is not None:
    #        self._window.remove_widget(self)
    #        self._window.unbind(on_resize=self._align_center)
    #        self._window = None

class MusicScreen(Screen):
    sm = ObjectProperty(None)
    menu_button = ObjectProperty(None)
    menu_popup = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)
        self.sm = ScreenManager()
        self.sm.add_widget(iPod(name='ipod'))
        self.sm.add_widget(Radio(name='radio'))
        self.sm.add_widget(Aux(name='aux'))
        self.sm.transition = NoTransition()
        self.add_widget(self.sm)
        self.menu_button = Menu_Button()

    def open_menu(self, widget):
        anim = Animation(x=200, y=0)
        self.menu_popup = Music_Menu_Popup()
        anim.start(widget)
        #self.menu_popup.open()
        self.menu_popup.current_screen = self.sm.current_screen
        self.sm.current_screen.add_widget(self.menu_popup)
        #self.menu_popup._anim_alpha = 100
        #self.menu_popup._anim_duration = 5
        anim.start(self.menu_popup)

        #
        #what if use add widget and then transition, try that and then move on spent too much time on styling
        #

    def send_CANBUS(self, code):
        # TODO will translate buttun presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)

music_screen_kv = """

    
<Menu_Button>:
    size_hint: None, None
    size: 30, 30
    pos: 20, 380
    text: 'menu'
    on_press: self.parent.parent.parent.open_menu(self)
        
        
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
