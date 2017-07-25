from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty

common_kv = """
<SideMenu>:
    #Button_Content: button_content
    id: sidemenu
    size_hint: None, 1
    width: 150
    pos_hint: {'x': 0}
    x: 0
    halign: 'center'
    BoxLayout:
        id: bl
        BoxLayout:
            id: button_content                         
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
    content_ = ObjectProperty(None)
    Button_Content = ObjectProperty(None)

    def add_content_(self, widget):
        self.content_ = widget
        self.ids.button_content.add_widget(self.content_)


    def dismiss(self, *largs, **kwargs):
        self.ids.button_content.remove_widget(self.content_)
        super().dismiss()



