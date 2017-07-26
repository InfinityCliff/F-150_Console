import canbus
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)

from side_menu import SideMenu

climate_screen_kv = """
#
# CLIMATE CONTROL SCREEN
#
<CheckBoxBase@CheckBox>   
    size_hint_x: None
    size_hint_y: None        
    background_color: [0, 0, 0, 0] 
    on_press: self.background_color = [0, 0, 0.8, 0.15]
    on_release: 
        self.background_color = [0, 0, 0, 0]
                                           
<CheckBoxBottom@CheckBoxBase>
    size: 102.5, 87.5
    background_radio_down: 'rsc/buttons/green_horizontal_on.png'
    background_radio_normal: 'rsc/buttons/green_horizontal_off.png'
    canvas:
        Clear
        Rectangle: 
            source: self._radio_image if self.group else self._checkbox_image
            -size: (20, 2) if not self.active else (24, 6)
            -pos: (int(self.center_x-10), int(self.y + 10)) \
                      if not self.active \
                      else (int(self.center_x-12), int(self.y + 10))
                     
<CheckBoxRight@CheckBoxBase> 
    id: cc_secondary
    size: 118.346, 62
    background_radio_down: 'rsc/buttons/green_vertical_on.png'
    background_radio_normal: 'rsc/buttons/green_vertical_off.png'
    background_checkbox_down: self.background_radio_down
    background_checkbox_normal: self.background_radio_normal
    canvas:
        Clear
        Rectangle:
            source: self._radio_image if self.group else self._checkbox_image
            -size: (2, 20) if not self.active else (6, 24)
            -pos: (int(self.right - 15), int(self.center_y - 10)) \
                      if not self.active \
                      else (int(self.right - 15), int(self.center_y - 12))
                      
<CCButtonSeatHeat@CheckBoxRight>
    background_checkbox_down: 'rsc/buttons/green_double_circle_vert_1_on.png'
    background_checkbox_normal: 'rsc/buttons/double_circle_vert_off.png'
    lights: 0
    on_press:
        self.lights += 1
        if self.lights == 3: self.lights = 0
    on_release:
        self.active = True if self.lights > 0 else False 
        self.background_radio_down = 'rsc/buttons/green_double_circle_vert_1_on.png' if self.lights == 1 else self._radio_image
        self.background_radio_down = 'rsc/buttons/green_double_circle_vert_2_on.png' if self.lights == 2 else self._radio_image
    canvas:
        Clear
        Rectangle:
            -source: self._radio_image if self.group else self._checkbox_image
            -size: (6, 19) if not self.active else (11, 21)
            -pos: (int(self.right - 15), int(self.center_y - 10)) \
                      if not self.active \
                      else (int(self.right - 17.635), int(self.center_y - 12))
<StepSlider_ControlButton@Button>
    background_color: [0,0,0,0]
    button_image_normal: self.background_normal
    button_image_down: self.background_down
    _button_image: self.button_image_normal
    image_size: 30,30
    on_press: self._button_image = self.button_image_down
    on_release: self._button_image = self.button_image_normal  
    Image:
        id: btn
        source: self.parent._button_image
        center_x: self.parent.center_x
        center_y: self.parent.center_y
        size: self.parent.image_size
        allow_stretch: True

<StepSlider>:
    size_hint_x: None
    size_hint_y: None
    b_color: [0, 0, 0, 1]
    StepSlider_ControlButton:
        size_hint_x:  0.4
        button_image_normal: 'rsc/buttons/blue_minus_active.png'
        button_image_down: 'rsc/buttons/blue_minus_normal.png'
        on_release: root.decrease()
    Label:
        id: step_view
        text: root.value if root.mode == 'text' else ''
        font_size: 30 
    StepSlider_ControlButton:
        size_hint_x:  0.4
        button_image_normal: 'rsc/buttons/red_plus_normal.png'
        button_image_down: 'rsc/buttons/red_plus_active.png'
        on_release: root.increase()      

<CCButtonPreset@CCButton>        
    size: 210, 48

<ClimateScreen>:
    id: 'climate'
    on_leave: app.frontglass.remove_SideMenuButton()
    FloatLayout:
        Image:
            source: 'rsc/screens/Climate.png'
            allow_stretch: False
        CheckBoxBottom:
            id: vent_feet
            group: 'vent_buttons'
            pos: 297.5, 160
        CheckBoxBottom:
            id: vent_feet_def
            group: 'vent_buttons'
            pos: 400, 160    
        CheckBoxBottom:
            id: vent_face
            group: 'vent_buttons'
            pos: 297.5, 247.5  
        CheckBoxBottom:
            id: vent_face_feet
            group: 'vent_buttons'
            pos: 400, 247.5
        CheckBoxBottom:
            id: power
            pos: 362.5, 345
            -size: 75, 60

        StepSlider:
            id: temperature_control
            pos: 48, 324
            size: 210, 60
            #step: 0
            values: [60, 65, 66, 67, 68, 69, 70, 75, 80, 85, 90]
        StepSlider:
            id: fan_control
            mode: 'bar'
            pos: 48, 226
            size: 210, 60
            #step: 0
            values: [0, 1, 2, 3, 4, 5, 6, 7]
        BoxLayout:
            pos: 48, 82
            size: 708.25, 62
            CCButtonSeatHeat:
                id: driver_seat_heat
            CheckBoxRight:
                id: vent_defrost
                group: 'vent_buttons'
            CheckBoxRight:
                id: rear_defrost
            CheckBoxRight:
                id: air_recirc
                group: 'air_source'
            CheckBoxRight:
                id: fresh_air
                group: 'air_source'
            CCButtonSeatHeat:
                id: passenger_seat_heat

                
        HOMEButton:
            on_release: root.manager.current = 'home'
                
#--------------------------------------------------------------
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
    values = ListProperty(None)
    step = NumericProperty(0)
    value = StringProperty('')
    mode = StringProperty('text') # or 'bar'

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


class ClimateScreen(Screen):
    def __init__(self, **kwargs):
        super(ClimateScreen, self).__init__(**kwargs)
        self.sidemenu = SideMenu()

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

    def send_CANBUS(self, code):
        # TODO will translate buttun presses to appropriate can-bus codes and send
        # TODO controller to tx on CAN-BUS
        canbus.send(code)
