from kivy.app import App

from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button
from kivy.uix.widget import Widget

side_menu_kv = """
#:include side_menu.kv
"""


class SideMenuContent(Popup):
    pass


class SideMenu(FloatLayout):
    sidemenu = ObjectProperty()
    sidemenucontent = ObjectProperty()
    #manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #app = App.get_running_app()
        #app.root.side_menu_controller = self

    def on_sidemenu(self):
        print('on_sidemenu')

    def show_side_menu(self):
        print('show_side_menu')
        #self.sidemenu = SideMenuContent()
        #self.sidemenu.open()
        #self.sidemenucontent, self.manager = self.parent.parent.parent.sm.current_screen.get_side_menu()
        #app = App.get_running_app()
        #app.root.active_manager = self.manager
        #app.root.side_menu_controller = self
        #self.sidemenu.menu_content.add_widget(self.sidemenucontent)


    def update_menu(self):
        print('update_menu')



