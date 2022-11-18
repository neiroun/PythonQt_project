# -*- coding: utf-8 -*-

from main_defs import *
from main_import import *

# This file represents the main class of this program. It serves to execute the program code and all its main functions.


class Main(QMainWindow):
    """
The execution of all the main functions of the program are enclosed in this class.
That is, it means recording, saving and playing back all records made using this program,
as well as creating your own extension
    """
# The __init__ function is used to initialize all the necessary variables, as well as to load the form
    def __init__(self):
        super().__init__()
        self.ui = MainForm()
        self.ui.setupUi(self)
        self.subscriber, self.on_selected_item, self.playing_scene, self.recording_scene, self.speed = Subscriber(), '', \
                                                                                                       False, False, 1.0
        self.values_for_spec = [True, True, True]
        self.ui.doubleSpinBox.setValue(self.speed)
        self.buttons = [self.ui.hotkeyReader1, self.ui.hotkeyReader2, self.ui.hotkeyReader3,
                        self.ui.button_for_start_record, self.ui.button_for_play, self.ui.button_to_save, self.ui.add_button,
                        self.ui.button_for_delete, self.ui.button_for_select, self.ui.button_for_mouse, self.ui.button_for_repeeat,
                        self.ui.button_for_keyboard]
        for item in self.buttons:
            item.clicked.connect(self.button_click_handler)
        self.load_items()
        self.load_signals()

####################################################################################################################
    # hotkey buttons function
####################################################################################################################

    def save(self):
        """
        This function provides the ability to change and save new hotkeys
        :return:
        """
        list_of_values = [self.buttons[x].text() for x in range(3)]
        for i in range(len(list_of_values)):
            if not list_of_values[i]:
                list_of_values[i] = standart_hotkey_list[i]
        save_button_value(list_of_values)
        """
        self.load_hotkey_button_values():  
        Saving hotkeys for future use, as well as for substituting them as default when restarting the program
        """
        self.load_values()

    def read(self, button):
        """
        A function to read a new hot key for selected button
        :param button:
        :return:
        """
        key = read_hotkey(suppress=False)
        if not key in read_button_value():
            if self.is_selected(button):
                button.setText(key)
        self.remove_selected(button)  # Removes the pattern of the selected button from the button

    def click(self, button):
        """
        A function that processes a keystroke and sets a new hotkey
        :param button:
        :return:
        """
        if self.is_selected(button):
            self.remove_selected(button)
            button.setText('')
        else:
            threading.Thread(target=self.read, args=(button,)).start()
            self.make_selected_pattern(button)

    @staticmethod
    def is_selected(button):
        """
        A function used to determine if a new hotkey has been set. If it returns "background-color: #E0E0E0;"
        then we understand that hotkey editing is completed
        :param button:
        :return:
        """
        return button.styleSheet()

    @staticmethod
    def remove_selected(button):
        """
        Function used to remove selected pattern from button (.QPushButton)
        :param button:
        :return:
        """
        button.setStyleSheet('')

    def make_selected_pattern(self, button):
        """
        Function to mark a button as selected when it is pressed
        :param button:
        :return:
        """
        if self.if_any_selected():
            self.remove_all_selected()
        button.setStyleSheet('background-color: #E0E0E0;')

    def remove_all_selected(self):
        """
        The function removes the pattern of the selected element from all buttons
        :return:
        """
        for item in self.buttons:
            self.remove_selected(item)

    def if_any_selected(self):
        """
        The function checks which of the keys have the pattern of the selected
        :return:
        """
        for item in self.buttons:
            if self.is_selected(item):
                return item
        return False

    def load_values(self):
        """
        Function loads hotkey values
        :return:
        """
        values = read_button_value()
        for x in range(len(values)):
            self.buttons[x].setText(values[x])
        self.activate_a_hotkey(values)

####################################################################################################################
    # scene hotkey functions
####################################################################################################################
    def stop(self):
        """
        This function serves to stop the recording process
        :return:
        """
        if self.playing_scene:
            return
        if self.recording_scene:
            self.stop_process()
        self.recording_scene = False
        self.record_button_load()

    def start(self):
        """
        This function serves to stop the recording process
        :return:
        """
        if self.playing_scene:
            return
        self.recording_scene = not self.recording_scene
        self.record_button_load()
        if self.recording_scene:
            self.subscriber.clear_log()
            threading.Thread(target=self.subscriber.run, args=(self.values_for_spec[0], self.values_for_spec[1])).start()
        else:
            self.stop_process()

    def play(self):
        """
        This function is used to play back a recording
        :return:
        """
        if self.recording_scene:
            return
        self.playing_scene = not self.playing_scene
        self.load_play_button()
        if self.playing_scene:
            self.speed = self.ui.doubleSpinBox.value()
            log = self.subscriber.get_log()
            if log:
                threading.Thread(target=self.playing_thread, args=(log,)).start()
        else:
            self.playing_scene = False

    def activate_a_hotkey(self, hotkeys):
        """
        A function to activate hotkeys for a given scene.
        The add_hotkey method is imported from the keyboard library and is used to create hotkeys
        and set their functions.
        :param hotkeys:
        :return:
        """
        remove_all_hotkeys()
        add_hotkey(hotkeys[0], self.start)
        add_hotkey(hotkeys[1], self.stop)
        add_hotkey(hotkeys[2], self.play)

    def stop_process(self):
        """
        This function is triggered when the recording of a scene is stopped, setting the file name,
        as well as its weight and duration.
        :return:
        """
        threading.Thread(target=self.subscriber.stop).start()
        self.ui.file_name.setText('NO')
        self.ui.file_weight.setText('NO')
        self.ui.file_runtime.setText(f'{to_fixed_value(self.time("", from_file=False), 3)} s')

    def playing_thread(self, log):
        """
        The function is used to play back a recorded scene. The following is an algorithm for this.
        :param log:
        :return:
        """
        control = mouse.Controller()
        while self.playing_scene:
            log_of_time = 0
            for item in log:
                if not self.playing_scene:
                    return
                mouse_list = item.split()
                sleep((float(mouse_list[0])-log_of_time)/self.speed)
                log_of_time = float(mouse_list[0])
                try:
                    if mouse_list[1] == 'mouseOnMove':
                        control.position = (int(mouse_list[2]), int(mouse_list[3]))
                    elif mouse_list[1] == 'mouseOnClick':
                        control.position = (int(mouse_list[2]), int(mouse_list[3]))
                        btn = ''
                        if mouse_list[4] == 'Button.left':
                            btn = mouse.Button.left
                        elif mouse_list[4] == 'Button.right':
                            btn = mouse.Button.right
                        elif mouse_list[4] == 'Button.middle':
                            btn = mouse.Button.middle
                        if mouse_list[5] == 'True':
                            control.press(btn)
                        elif mouse_list[5] == 'False':
                            control.release(btn)
                        else:
                            raise ValueError
                    elif mouse_list[1] == 'mouseOnScroll':
                        mouse.position = (int(mouse_list[2]), int(mouse_list[3]))
                        mouse.scroll(int(mouse_list[4]), int(mouse_list[5]))
                    elif mouse_list[1] == 'keyboard':
                        if mouse_list[3] == 'up':
                            press(mouse_list[2])
                        elif mouse_list[3] == 'down':
                            release(mouse_list[2])
                    else:
                        raise ValueError
                except:
                    pass
            if not self.values_for_spec[2]:
                break
        self.playing_scene = False
        self.load_play_button()

    def time(self, name, from_file=True):
        """
        In this function, the execution time of the scene is calculated, for its further use.
        :param name:
        :param from_file:
        :return:
        """
        if from_file:
            with open(f'{name}.rec', 'r') as inf:
                mouse_list = inf.read()
                if mouse_list:
                    item = re.findall(r'(\d+\.\d+)', str(mouse_list).strip('[]'))
                    if item:
                        return float(item[-1])
                    else:
                        return 0
                else:
                    return 0
        else:
            if self.subscriber.get_log():
                return float(self.subscriber.get_log()[-1].split()[0])
            else:
                return 0

    def save_to_file(self):
        """
        Function to save the recorded scene to a file with .rec extension
        :return:
        """
        name = self.ui.lineEdit.text()
        movement = self.subscriber.get_log()
        if name and movement:
            directory_name, text = f'{name}.rec', ''
            if os.path.exists(directory_name):
                index = 2
                directory_name = f'{name}({index}).rec'
                while os.path.exists(directory_name):
                    index += 1
                    directory_name = f'{name}({index}).rec'
            for item in movement:
                text += f'{item}\n'
            with open(directory_name, 'w') as ouf:
                ouf.write(text[:-1])
            self.view_load_items()
        else:
            if not name:
                threading.Thread(target=self.line_edit_error).start()
            elif not movement:
                threading.Thread(target=self.animate_lineEdit_log).start()

    @staticmethod
    def read_file(name):  # reading scene file data
        """
        The function is used to read data from a file with a recorded scene
        :param name:
        :return:
        """
        if os.path.exists(f'{name}.rec'):
            returned = list()
            with open(f'{name}.rec', 'r') as inf:
                for item in inf:
                    returned.append(item.strip())
            return returned
        return False

###################################################################################################################
    # list view functions
###################################################################################################################

    def view_load_items(self):
        """
        Function to view the list of loaded items
        :return:
        """
        mdl = QtGui.QStandardItemModel()
        self.ui.list_view.setModel(mdl)
        for item in os.listdir():
            rc = os.path.splitext(item)[1]
            if rc == '.rec':
                item = QtGui.QStandardItem(item)
                item.setEditable(False)
                mdl.appendRow(item)

    def selected_item(self, index):
        """
        The function is used to display information about the recorded scene: duration, recording time, scene weight,
        its name.
        :param index:
        :return:
        """
        self.on_selected_item = index
        self.ui.second_name.setText(index.data())
        self.ui.second_weight.setText(f'{to_fixed_value(os.path.getsize(index.data()) / 1024, 2)} Кб')
        dt = str(ctime(os.path.getctime(index.data())))
        self.ui.second_time.setText(f'{to_fixed_value(self.time(index.data()[:index.data().find(".")], from_file=True), 3)} с')
        self.ui.date.setText(dt[dt.find(' ') + 1:dt.rfind(' ')])

    def delete(self):  # Function for delete item from list
        os.remove(self.on_selected_item.data())
        mdl = QtGui.QStandardItemModel()
        self.ui.list_view.setModel(mdl)
        mdl.removeRow(self.on_selected_item.row())
        self.view_load_items()

    def on_select_button(self):
        """
        The function is used to display information about the recorded scene when you click on the "Select" button:
        duration, recording time, scene weight, its name.
        :return:
        """
        if self.on_selected_item:
            self.ui.file_name.setText(self.on_selected_item.data())
            self.ui.file_weight.setText(f'{to_fixed_value(os.path.getsize(self.on_selected_item.data()) / 1024, 2)} Кб')
            self.ui.file_runtime.setText(f'{to_fixed_value(self.time(self.on_selected_item.data()[:self.on_selected_item.data().find(".")], from_file=True), 3)} с')
            self.subscriber.set_log(self.read_file(self.on_selected_item.data()[:self.on_selected_item.data().find('.')]))

    def line_edit_error(self):
        """
        Fires when the "Add" button is clicked, if the user has not entered a name for the file.
        :return:
        """
        txt = self.ui.lineEdit.placeholderText()
        self.ui.lineEdit.setPlaceholderText('Вы не указали название')
        sleep(5)
        self.ui.lineEdit.setPlaceholderText(txt)

    def load_items(self):  # Function for load items
        self.ui.lineEdit.setPlaceholderText('Название сценария')
        check()
        self.load_values()
        self.load_images()
        self.view_load_items()

    def load_signals(self):  # Function for load signals
        self.ui.button_to_save.clicked.connect(self.save)
        self.ui.button_for_start_record.clicked.connect(self.start)
        self.ui.button_for_play.clicked.connect(self.play)
        self.ui.add_button.clicked.connect(self.save_to_file)
        self.ui.list_view.clicked.connect(self.selected_item)
        self.ui.button_for_delete.clicked.connect(self.delete)
        self.ui.button_for_select.clicked.connect(self.selected_item)
        self.ui.link_on_my_github.clicked.connect(lambda: webbrowser.open('https://github.com/neiroun'))
        self.ui.button_for_mouse.clicked.connect(lambda: self.spec_button_onclick(0))
        self.ui.button_for_keyboard.clicked.connect(lambda: self.spec_button_onclick(1))
        self.ui.button_for_repeeat.clicked.connect(lambda: self.spec_button_onclick(2))

    def spec_button_onclick(self, index):  # Function for spec buttons ON/OFF
        self.values_for_spec[index] = not self.values_for_spec[index]
        if self.values_for_spec[index]:
            self.sender().setText('ВКЛ')
        else:
            self.sender().setText('ВЫКЛ')

    def button_click_handler(self):  # Function for button click handling
        button = self.sender()
        if button in self.buttons[:3]:
            self.click(button)
        else:
            threading.Thread(target=self.button_animation, args=(button,)).start()

    @staticmethod
    def button_animation(button):
        button.setStyleSheet('background-color: #E0E0E0;')
        sleep(0.1)
        button.setStyleSheet('')

    def load_play_button(self):  # load play button
        try:
            os.chdir('../img')
            if self.playing_scene:
                icon = QtGui.QIcon('stop_red.png')
            else:
                icon = QtGui.QIcon('start_red.png')
            os.chdir('../data')

        except:
            pass
        else:
            self.ui.button_for_play.setIcon(icon)

    def record_button_load(self):  # load record button
        try:
            os.chdir('../img')
            if self.recording_scene:
                icon = QtGui.QIcon('stop_blue.png')
            else:
                icon = QtGui.QIcon('start_blue.png')
            os.chdir('../data')
        except:
            pass
        else:
            self.ui.button_for_start_record.setIcon(icon)

    def load_other_images(self):  # Function to upload GitHub icon
        try:
            os.chdir('../img')  # change directory to img folder
            github_pixmap = QtGui.QPixmap('github.png')
            os.chdir('../data')  # change directory back to data
        except:
            pass
        else:
            self.ui.githubIcon.setPixmap(github_pixmap)

    def load_images(self):  # load all img
        """
        Function to upload pictures to play record buttons and so on
        """
        self.load_play_button()
        self.load_other_images()
        self.record_button_load()


if __name__ == '__main__':
    app = QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec())
