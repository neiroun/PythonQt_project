from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from form import Ui_MainWindow
import sys
from time import sleep, time, ctime
from pynput import mouse
import threading
from keyboard import read_hotkey, add_hotkey, remove_all_hotkeys, hook, unhook, press, release, remove_hotkey
import os
import re
import webbrowser
from Subscriber import Subscriber
from const import standart_hotkey_list