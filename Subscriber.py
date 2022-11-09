# -*- coding: utf-8 -*-


from main_import import *


class Subscriber:
    def __init__(self):
        self.logg, self.StartTime = [], 0
        self.mouseListener = mouse.Listener(on_move=self.OnMove, on_click=self.onclick, on_scroll=self.OnScroll)
        self.keyListener = ''
        self.IsStarted = False
        self.mouseOn, self.keyboardOn = True, True

    def run(self, mouseOn, keyboardOn):
        if not self.IsStarted:
            self.mouseOn, self.keyboardOn = mouseOn, keyboardOn
            self.clear_log()
            self.StartTime = time()
            if self.mouseOn:
                self.mouseListener.start()
            if self.keyboardOn:
                self.keyListener = hook(self.WriteKeyboard)
            self.IsStarted = True

    def set_log(self, new_log):
        self.logg = new_log

    def stop(self):
        if self.IsStarted:
            if self.mouseOn:
                self.mouseListener.stop()
                self.mouseListener = mouse.Listener(on_move=self.OnMove, on_click=self.onclick, on_scroll=self.OnScroll)
            if self.keyboardOn:
                unhook(self.keyListener)
            self.IsStarted = False
            self.keyListener = ''

    def get_log(self):
        return self.logg

    def clear_log(self):
        self.logg = []

    def WriteKeyboard(self, a):
        self.logg.append(f'{time() - self.StartTime} keyboard {str(a)[str(a).find("(") + 1:str(a).find(")")]}')

    def OnMove(self, x, y):
        self.logg.append(f'{time() - self.StartTime} mouseOnMove {x} {y}')

    def onclick(self, x, y, button, pressed):
        self.logg.append(f'{time() - self.StartTime} mouseOnClick {x} {y} {button} {pressed}')

    def OnScroll(self, x, y, dx, dy):
        self.logg.append(f'{time() - self.StartTime} mouseOnScroll {x} {y} {dx} {dy}')
