from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

common_kv = """
#: import Factory kivy.factory.Factory

<SideMenuContent@Popup>
   #button_content: bc
    menu_content: menu_content
    id: sidemenu
    size_hint: None, 1
    width: 150
    pos_hint: {'x': 0}
    x: 0
    halign: 'center'
    #on_start: print('starting menu')
    BoxLayout:
        id: bl
        BoxLayout:
            id: menu_content
            pos_hint: {'center_y': 0.5}
            size_hint_y: None
            height: 90
            size_hint_x: None
            width: 100
        Button:
            text: '<<'
            on_press:
                print('dismiss')
                root.dismiss() 
                
<SideMenuButton@Button>:
    size_hint: None, None
    size: 30, 356
    text: '>>'
    #pos_hint: 1, None
    y: 69
    background_color: [.5,.5,.5,.4]
    on_press: self.background_color = [.5,.5,.8,.6]
    on_release:
        root.add_widget(Factory.SideMenuContent())
        #app.sm.current_screen.sidemenu.open()
        #root.menu_content.add_widget(app.root.sm.current_screen.menu_content)
        self.background_color = [.5,.5,.5,.4]


<SideMenu>:
    SideMenuButton:
"""


class SideMenu(Widget):
    button_content = ObjectProperty()
    menu_content = ObjectProperty()

    #def __init__(self, screen_manager, **kwargs):
    #    super(SideMenu, self).__init__(**kwargs)
    #    self.sm = screen_manager
