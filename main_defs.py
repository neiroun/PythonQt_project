# -*- coding: utf-8 -*-

from main_import import *


def to_fixed_value(numberObj, digits=0):  # values to fixed
    return f"{numberObj:.{digits}f}"


def check():  # Function for check data
    if not os.path.exists('data'):
        os.mkdir('data')
    os.chdir('data')


def clear_values():
    global standart_hotkey_list
    with open('buttons.dt', 'w') as ouf:
        txt = ''
        for item in standart_hotkey_list:
            txt += f'{item}\n'
        ouf.write(txt[:-1])


def read_button_value():
    global standart_hotkey_list
    if os.path.exists('buttons.dt'):
        lines, correct = list(), list()
        with open('buttons.dt') as file:
            for item in file:
                lines.append(item)
        if len(lines) < 3:
            clear_values()
            return standart_hotkey_list
        for item in range(len(lines)):
            try:
                add = add_hotkey(lines[item].strip(), lambda: 2)
            except:
                correct.append(standart_hotkey_list[item])
            else:
                correct.append(lines[item])
                remove_hotkey(add)
        save_button_value(correct)
        return list(map(str.strip, correct))
    else:
        clear_values()
        return list(map(str.strip, standart_hotkey_list))


def save_button_value(values):
    if os.path.exists('buttons.dt'):
        txt = ''
        for item in values:
            txt += f'{item.strip()}\n'
        with open('buttons.dt', 'w') as ouf:
            ouf.write(txt[:-1])
    else:
        clear_values()
        save_button_value(values)

