from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SideMenuButton(Button):
    pass


common_kv = """
<SideMenuButton>:
    size_hint: None, None
    size: 30, 356
    text: '>>'
    #pos_hint: 1, None
    y: 69
    background_color: [.5,.5,.5,.4]
    on_press: self.background_color = [.5,.5,.8,.6]
    on_release: 
        app.scrman.current_screen.sidemenu.open()
        self.background_color = [.5,.5,.5,.4]
    
<SideMenu>:
    button_content: bc
    id: sidemenu
    size_hint: None, 1
    width: 150
    pos_hint: {'x': 0}
    x: 0
    halign: 'center'
    BoxLayout:
        id: bl
        BoxLayout:
            id: bc
            pos_hint: {'center_y': 0.5}
            size_hint_y: None
            height: 90
            size_hint_x: None
            width: 100
        Button:
            text: '<<'
            on_press:
                sidemenu.dismiss()
"""


class SideMenu(Popup):
    button_content = ObjectProperty()

    def __init__(self, **kwargs):
        super(SideMenu, self).__init__(**kwargs)

    def add_content_(self, widget):
        self.button_content.clear_widgets()
        self.button_content.add_widget(widget)




