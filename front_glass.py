from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from functools import partial
# from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from side_menu import SideMenuButton


class QuitMenu(ModalView):
    pass


front_glass_kv = """
<FrontGlass>:
    id: frontglass
    FloatLayout:
        id: frontglasslayout

<QuitMenu>:
    id: quit_menu
    #background: 'rsc/logo/InfinityCliffLogoClear-Red.png'
    #border: [72.5, 232.2, 72.5, 232.5]
    FloatLayout:
        pos_hint: None, None
        pos: 10, 10
        size_hint: None, None
        size: 335, 335
        canvas.after:
            Rectangle:
                size: self.size
                pos: self.pos
                source: 'rsc/logo/InfinityCliffLogoClear-Red.png'
        BoxLayout:
            id: popup
            size_hint: None, None
            size: 290, 60
            #pos_hint: None, None
            pos: 10, 370
            orientation: 'vertical'
            Button:
                id: quit_button
                on_release: quit()
                size_hint: None, None
                size: 290, 30
                background_normal: 'rsc/buttons/quit_car_pc.png'
            Button:
                text: 'CAN-BUS Console'
                size_hint: None, None
                size: 290, 30
            Button:
                id: cancel
                on_release: quit_menu.dismiss()
                size_hint: None, None
                size: 80, 30
                pos_hint: {'center_x': 0.5, 'y': 1}
                background_normal: 'rsc/buttons/cancel.png'
"""


class FrontGlass(FloatLayout):
    def __init__(self, **kwargs):
        super(FrontGlass, self).__init__(**kwargs)
        self.bind(
            on_touch_down=self.create_clock,
            on_touch_up=self.delete_clock)
        self.quit_menu = QuitMenu()
        self.side_menu_button = SideMenuButton()
        self.touch = None

    def create_clock(self, widget, touch, *args):
        self.touch = touch
        callback = partial(self.quit_menu.open, self.touch)
        Clock.schedule_once(callback, 2)
        self.touch.ud['event'] = callback

    def delete_clock(self, widget, touch, *args):
        if self.touch:
            Clock.unschedule(touch.ud['event'])
            self.touch = None

    def add_side_menu_button(self):

        self.add_widget(self.side_menu_button)

    def remove_side_menu_button(self):
        self.remove_widget(self.side_menu_button)
