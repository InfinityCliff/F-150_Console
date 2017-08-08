# https://stackoverflow.com/questions/30202801/how-to-access-id-widget-of-different-class-from-a-kivy-file-kv

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty


class Get_People(BoxLayout):
    stuff_p = ObjectProperty

    def rooted(self):
        self.ids.gb.stuff_b.text = "people changed boys!"

class Get_Boys(BoxLayout):
    stuff_b = ObjectProperty

    def change_girl(self):
        self.parent.ids.gg.stuff_c.text = "Boys changed Girls!"
        #self.stuff_b.text = "i changed myself!"

    def change_people(self):
        self.parent.ids.root_lbl.text = "Boys changed people!"

class Get_Girls(BoxLayout):
    stuff_c = ObjectProperty


class gpApp(App):
    def build(self):
        self.load_kv('dates_test.kv')
        return Get_People()

if __name__ == "__main__":
    gpApp().run()