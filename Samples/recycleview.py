from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior



items = [
    {"text": "white",    "selected": 'normal', "input_data": ["some","random","data"]},
    {"text": "lightblue","selected": 'normal', "input_data": [1,6,3]},
    {"text": "blue",     "selected": 'normal', "input_data": [64,16,9]},
    {"text": "gray",     "selected": 'normal', "input_data": [8766,13,6]},
    {"text": "orange",   "selected": 'normal', "input_data": [9,4,6]},
    {"text": "yellow",   "selected": 'normal', "input_data": [852,958,123]},
    {"text": "white",    "selected": 'normal', "input_data": ["some","random","data"]},
    {"text": "lightblue","selected": 'normal', "input_data": [1,6,3]},
    {"text": "blue",     "selected": 'normal', "input_data": [64,16,9]},
    {"text": "gray",     "selected": 'normal', "input_data": [8766,13,6]},
    {"text": "orange",   "selected": 'normal', "input_data": [9,4,6]},
    {"text": "yellow",   "selected": 'normal', "input_data": [852,958,123]}
]



class MyViewClass(RecycleDataViewBehavior, BoxLayout):

    text = StringProperty("")
    index = None

    def set_state(self,state,app):
        app.root.ids.rv.data[self.index]['selected'] = state

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(MyViewClass, self).refresh_view_attrs(rv, index, data)



class MyRecycleView(RecycleView):

    data = items

    def print_data(self,data):
        print([item['input_data'] for item in data if item['selected'] == 'down'])



KV = '''

<MyViewClass>:
    orientation: 'horizontal'
    CheckBox:
        on_state: root.set_state(self.state,app)
    Label:
        text: root.text

BoxLayout:
    orientation: 'vertical'
    MyRecycleView:
        id: rv
        viewclass: 'MyViewClass'
        RecycleBoxLayout:
            orientation: 'vertical'
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
    Button:
        size_hint_y: 0.1
        text: "Print data"
        on_release: rv.print_data(rv.data)

'''



class RV(App):
    def build(self):
        root = Builder.load_string(KV)
        return root


RV().run()