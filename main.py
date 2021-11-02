#!/usr/bin/python3
from kivy.app import App
from screens import StopWatchScreen


class StopWatchApp(App):

    def build(self):
        self.screen = StopWatchScreen()
        return self.screen

    def on_stop(self):
        self.screen.on_close()


if __name__ == '__main__':
    StopWatchApp().run()