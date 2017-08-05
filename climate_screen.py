import canbus
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import (Line)

from side_menu import SideMenu
from console_screen import ConsoleScreen

climate_screen_kv = """
#:include climate_screen.kv
"""

canbus.code_table = {'temp_up': 0, 'temp_down': 1,
                     'fan_up': 2,  'fan_down': 3,
                     'vent_FA': 4, 'vent_FF': 5, 'vent_FT': 6, 'vent_FD': 7,
                     'vent_DF': 8, 'read_DF': 9,
                     'Air_RE': 10, 'Air_FR': 11,
                     'Heat_DR1': 12, 'Heat_DR2': 13, 'Heat_DRO': 14,
                     'Heat_PS1': 15, 'Heat_PS2': 16, 'Heat_PSO': 17,
                     'AC': 18, 'power': 19}


class StepSlider(BoxLayout):
    values = ListProperty()
    step = NumericProperty(0)
    value = StringProperty('')
    mode = StringProperty('text')  # or 'bar'

    def __init__(self, **kwargs):
        super(StepSlider, self).__init__(**kwargs)

    def decrease(self):
        self.step -= 1 if self.step > 1 else 0
        self.value = str(self.values[self.step])
        if self.mode == 'bar':
            self.drawbar()
            canbus.send('fan_down')
        if self.mode == 'text':
            canbus.send('temp_down')

    def increase(self):
        if self.step < len(self.values) - 1:
            self.step += 1
        else:
            self.step = len(self.values) - 1
        self.value = str(self.values[self.step])
        if self.mode == 'bar':
            self.drawbar()
            canbus.send('fan_up')
        if self.mode == 'text':
            canbus.send('temp_up')

    def drawbar(self):
        canvas = self.ids.step_view.canvas
        canvas.clear()
        for x in range(1, self.step+1):
            with canvas:
                x1 = self.x + 63.1 + ((x-1) * 13.883)
                y1 = self.y + 13.297
                x2 = x1
                y2 = y1 + 35
                Line(points=[x1, y1, x2, y2], width=2)


class ClimateScreen(ConsoleScreen):

    def startup(self, init_state):
        vent_buttons = {1: self.ids.vent_face,
                        2: self.ids.vent_feet_def,
                        3: self.ids.vent_feet,
                        4: self.ids.vent_face_feet,
                        5: self.ids.vent_defrost}

        self.ids.power.active = init_state['power']
        vent_buttons[init_state['vent_buttons']].active = True
        self.ids.temperature_control.step = init_state['temp_step']
        self.ids.fan_control.step = init_state['fan_stop']
        self.ids.fan_control.drawbar()

    def get_side_menu(self):
        return None, None

    @staticmethod
    def send_canbus(code):
        # TODO will translate button presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)
