from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty

from kivy.clock import Clock

class Box1(BoxLayout):
    lbl = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.startup(), 0) # call after the next frame

    def startup(self):
        app = App.get_running_app()
        self.lbl = app.root.ids.box2.label2

    def change_label2(self, text):
        self.lbl.text = text

class Box2(BoxLayout):
    label2 = ObjectProperty()


class EventRoot(BoxLayout):
    change_label = ObjectProperty()


class EventApp(App):
    pass


if __name__ == '__main__':
    EventApp().run()