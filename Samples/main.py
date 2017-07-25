from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# BEGIN ADDLOCATIONFORM
from kivy.properties import ObjectProperty  # <1>
from kivy.lang import Builder

Builder.load_string("""

<AddLocationForm>:
    orientation: "vertical"
    search_input: search_box
    BoxLayout:
        height: "40dp"
        size_hint_y: None
        TextInput:
            id: search_box
            size_hint_x: 50
        Button:
            text: "Search"
            size_hint_x: 25
            on_press: root.search_location()
        Button:
            text: "Current Location"
            size_hint_x: 25
    ListView:
        item_strings: ["Palo Alto, MX", "Palo Alto, US"]

#AddLocationForm:

""")



class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()  # <2>

    def search_location(self):
        print("Explicit is better than Implicit")
# END ADDLOCATIONFORM


class WeatherApp(App):
    def build(self):
        return AddLocationForm()

if __name__ == '__main__':
	WeatherApp().run()
