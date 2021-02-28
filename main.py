from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'Calculator App'

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: 'Calculator App'
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1

        MDTextField:
            id: val1
            input_filter: 'float'
            hint_text: "Enter the first value"
            color_mode: 'custom'
            helper_text_mode: "on_focus"

        MDTextField:
            id: val2
            input_filter: 'float'
            hint_text: "Enter the second value"
            color_mode: 'custom'
            helper_text_mode: "on_focus"

        MDTextField:
            id: val3
            hint_text: "Result"
            readonly : "True"
            color_mode: 'custom'
            icon_right_color: app.theme_cls.primary_color
            icon_right: 'equal-box'
        
        MDRoundFlatIconButton:
            id:add
            text: "Addition"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.addition()

        MDRoundFlatIconButton:
            id:sub
            text: "Substraction"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.sub()

        MDRoundFlatIconButton:
            id:add
            text: "Multification"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.multi()

        MDRoundFlatIconButton:
            id:div
            text: "Division"
            icon:"calculator"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.div()

        MDSpinner:
            id: rc_spin
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': .5, 'center_y': .5}
            active: False

        MDLabel:
            id: result
    '''


class Main(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Main(name='Calculator_App'))


class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        self.title = 'Calculator App'
        return self.help_string

    def addition(self):
        val1 = int(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = int(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 + val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Addition is: " +str(res)

    def sub(self):
        val1 = int(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = int(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 - val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Subtraction is: " +str(res)

    def multi(self):
        val1 = int(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = int(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 * val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Multification is: " +str(res)

    def div(self):
        val1 = int(self.help_string.get_screen('Calculator App').ids.val1.text)
        val2 = int(self.help_string.get_screen('Calculator App').ids.val2.text)
        res = val1 / val2
        self.help_string.get_screen('Calculator App').ids.val3.text = "The Division is: " +str(res)

MainApp().run()