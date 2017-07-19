from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from functools import partial
from kivy.uix.label import Label

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


class FrontGlass(Label):
    def __init__(self, **kwargs):
        super(FrontGlass, self).__init__(**kwargs)
        self.bind(
            on_touch_down=self.create_clock,
            on_touch_up=self.delete_clock)
        self.quit_menu = QuitMenu()

    def create_clock(self, widget, touch, *args):
        callback = partial(self.quit_menu.open, touch)
        Clock.schedule_once(callback, 2)
        touch.ud['event'] = callback

    def delete_clock(self, widget, touch, *args):
        Clock.unschedule(touch.ud['event'])
