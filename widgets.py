from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread
from kivy.lang.builder import Builder
from stopwatch import StopWatch

Builder.load_string('''
<StopWatchButton@ButtonBehavior+Image>

<StopWatchMainButton@StopWatchButton>
    source:
        'img/stopwatch_button.png'

<StopWatchTimerButton@StopWatchButton>
    source:
        'img/timer_button.png'

<StopWatchAddLapsButton@StopWatchButton>
    source:
        'img/add_laps_button.png'

<StopWatchMenu>
    StopWatchMainButton
    StopWatchTimerButton
    StopWatchAddLapsButton

<StopwatchWidget>
    hours:
        '00'
    minutes:
        '00'
    seconds:
        '00'
    milliseconds:
        '000'
    Label:
        markup:
            True
        font_size:
            self.width / 4.3
        text_size:
            self.size
        halign:
            'left'
        valign:
            'bottom'
        text:
            root.hours + ':' + root.minutes + ':' + root.seconds + '[size=' + str(int(self.font_size / 4)) + ']' + root.milliseconds + '[/size]'
''')



class StopWatchMenu(BoxLayout):
    """Menu for selecting which stopwatch function to use"""
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback


class StopWatchWidget(RelativeLayout):
    """Widget for loading, running and displaying StopWatch class"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_elapsed = 0
        self.obj = StopWatch(self.update)
        self.obj.start()

    def set_hours(self, h):
        h = str(h)
        if len(h) == 1:
            h = '0' + h
        self.hours = h

    def set_minutes(self, m):
        m = str(m)
        if len(m) == 1:
            m = '0' + m
        self.minutes = m

    def set_seconds(self, s):
        s = str(s)
        if len(s) == 1:
            s = '0' + s
        self.seconds = s

    def set_milliseconds(self, ms):
        m = str(ms)[2:]
        o = '000'
        self.milliseconds = m + o[len(m):]

    def start(self):
        self.__prev_time = None
        self.obj.resume()

    def stop(self):
        self.obj.pause()

    def cancel(self):
        self.obj.stop()

    @mainthread
    def update(self, dt):
        self.time_elapsed += dt
        s = int(self.time_elapsed)
        self.set_milliseconds(round(self.time_elapsed - s, 3))
        h = s // 3600
        self.set_hours(h)
        s -= h * 3600
        m = s // 60
        self.set_minutes(m)
        s -= m * 60
        self.set_seconds(s)
