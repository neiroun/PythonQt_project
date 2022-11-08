# -*- coding: utf-8 -*-

from main_import import *


def toFixed(numberObj, digits=0):
    return f"{numberObj:.{digits}f}"


def check_folder_of_data():
    if not os.path.exists('data'):
        os.mkdir('data')
    os.chdir('data')

def clear_values_of_button():
    global standart_hotkey_list
    with open('buttons.dt', 'w') as ouf:
        text = ''
        for hotkey in standart_hotkey_list:
            text += f'{hotkey}\n'
        ouf.write(text[:-1])

def read_values_of_button():
    global standart_hotkey_list
    if os.path.exists('buttons.dt'):
        lines, correct_list = [], []
        with open('buttons.dt') as inf:
            for line in inf:
                lines.append(line)
        if len(lines) < 3:
            clear_values_of_button()
            return standart_hotkey_list
        for x in range(len(lines)):
            try:
                a = add_hotkey(lines[x].strip(), lambda: 2)
            except:
                correct_list.append(standart_hotkey_list[x])
            else:
                correct_list.append(lines[x])
                remove_hotkey(a)
        save_values_of_buttons(correct_list)
        return list(map(str.strip, correct_list))
    else:
        clear_values_of_button()
        return list(map(str.strip, standart_hotkey_list))


def save_values_of_buttons(values):
    if os.path.exists('buttons.dt'):
        text = ''
        for item in values:
            text += f'{item.strip()}\n'
        with open('buttons.dt', 'w') as ouf:
            ouf.write(text[:-1])
    else:
        clear_values_of_button()
        save_values_of_buttons(values)

