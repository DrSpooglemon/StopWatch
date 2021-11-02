from threading import Thread, Event
from time import time, sleep


class StopWatch(Thread):

    def __init__(self, callback):
        super().__init__()
        self.__go = Event()
        self.__running = True
        self.callback = callback

    def __emit(self):
        t = time()
        self.callback(t - self.__prev_time)
        self.__prev_time = t

    def pause(self):
        self.__emit()
        self.__go.clear()

    def resume(self):
        self.__prev_time = time()
        self.__go.set()

    def stop(self):
        print('stopping stopwatch thread...')
        self.__go.set()
        self.__running = False

    def run(self):
        self.__prev_time = None
        while self.__running:
            self.__go.wait()
            sleep(.001)
            self.__emit()
        print('stopwatch thread stopped')