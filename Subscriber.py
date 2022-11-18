# -*- coding: utf-8 -*-


from main_import import *


class Subscriber:  # Write class
    def __init__(self):
        self.logg, self.StartTime = [], 0
        self.mouse_subscriber = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.key_subscriber = ''
        self.is_start = False
        self.mouseOn, self.keyboardOn = True, True

    def run(self, mouseOn, keyboardOn):  # run process
        if not self.is_start:
            self.mouseOn, self.keyboardOn = mouseOn, keyboardOn
            self.clear_log()
            self.StartTime = time()
            if self.mouseOn:
                self.mouse_subscriber.start()
            if self.keyboardOn:
                self.key_subscriber = hook(self.keyboard_write)
            self.is_start = True

    def set_log(self, new_log):  # set log
        self.logg = new_log

    def stop(self):  # stop process
        if self.is_start:
            if self.mouseOn:
                self.mouse_subscriber.stop()
                self.mouse_subscriber = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
            if self.keyboardOn:
                unhook(self.key_subscriber)
            self.is_start = False
            self.key_subscriber = ''

    def get_log(self):  # get logg
        return self.logg

    def clear_log(self):  # clear log
        self.logg = list()

    def keyboard_write(self, a):  # Function for write keyboard
        self.logg.append(f'{time() - self.StartTime} keyboard {str(a)[str(a).find("(") + 1:str(a).find(")")]}')

    def on_move(self, x, y):
        self.logg.append(f'{time() - self.StartTime} mouseOnMove {x} {y}')

    def on_click(self, x, y, button, pressed):
        self.logg.append(f'{time() - self.StartTime} mouseOnClick {x} {y} {button} {pressed}')

    def on_scroll(self, x, y, dx, dy):
        self.logg.append(f'{time() - self.StartTime} mouseOnScroll {x} {y} {dx} {dy}')
