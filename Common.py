from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty

common_kv = """

"""


class SideMenu(Popup):
    Button_Content = ObjectProperty()

    def __init__(self, content_, **kwargs):
        super(SideMenu, self).__init__(**kwargs)
        self.content_ = content_
        self.add_content_(self.content_)

    def add_content_(self, widget):
        self.Button_Content.clear_widgets()
        self.Button_Content.add_widget(widget)

    def dismiss(self, *largs, **kwargs):
        self.ids.button_content.remove_widget(self.content_)
        super().dismiss()



