from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from widgets import StopWatchWidget
from widgets import StopWatchMenu
from kivy.lang import Builder

Builder.load_string('''
''')


class StopWatchScreen(FloatLayout):

    def __init__(self):
        super().__init__()
        layout = BoxLayout(orientation='vertical',
                           size_hint=(.8, .7),
                           pos_hint={'center_x': .52, 'center_y': .5})
        #layout.add_widget(StopWatchMenu(self.menu_selection))
        self.stopwatch = StopWatchWidget()
        layout.add_widget(self.stopwatch)
        layout.add_widget(ToggleButton(size_hint_x=(.96),
                                       on_press=self.button_pressed))
        self.add_widget(layout)

    def button_pressed(self, btn):
        if btn.state == 'normal':
            self.stopwatch.stop()
        elif btn.state == 'down':
            self.stopwatch.start()

    def menu_selection(self, *args):
        for arg in args:
            print(arg)
        print('----------')

    def on_close(self):
        self.stopwatch.cancel()
