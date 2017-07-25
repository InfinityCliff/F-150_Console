from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty

Builder.load_string("""
<Get_People>:
    stuff_p: root_lbl
    orientation: 'vertical'
    Button:
        name: root_btn
        id: root_btn
        text: "I am Root Button"
        on_release: root.rooted()
    Label:
        id: root_lbl
        text: "I am Root Label"
    Get_Boys:
        id: gb
    Get_Girls:
        id: gg

<Get_Boys>:
    stuff_b: label_b
    Button:
        id: button_b
        text: "button 1"
        on_release: root.change_girl()
        on_press: root. change_people()
    Label:
        id: label_b
        text: "Label for boys"

<Get_Girls>:
    stuff_c: label_g
    Button:
        id: button_g
        text: "Button for girls"
    Label:
        id: label_g
        text:"Label for girls"
""")


class Get_People(BoxLayout):
    stuff_p = ObjectProperty(None)

    def rooted(self):
        self.ids.gb.stuff_b.text = "people changed boys!"

class Get_Boys(BoxLayout):
    stuff_b = ObjectProperty(None)

    def change_girl(self):
        self.parent.ids.gg.stuff_c.text = "Boys changed Girls!"

    def change_people(self):
        self.parent.ids.root_lbl.text = "Boys changed people!"

class Get_Girls(BoxLayout):
    stuff_c = ObjectProperty(None)

class TestApp(App):
    def build(self):
        #self.load_kv('dates_test.kv')
        return Get_People()

if __name__ == '__main__':
    TestApp().run()