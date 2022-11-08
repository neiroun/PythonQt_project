# -*- coding: utf-8 -*-

from main_defs import *
from main_import import *


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listener, self.selected_item, self.scene_playing, self.scene_recording, self.speed = Subscriber(), '', \
                                                                                                  False, False, 1.0
        self.spec_values = [True, True, True]
        self.ui.doubleSpinBox.setValue(self.speed)
        self.button_list = [self.ui.hotkeyReader1, self.ui.hotkeyReader2, self.ui.hotkeyReader3,
                            self.ui.startRecordButton, self.ui.playButton, self.ui.saveButton, self.ui.addButton,
                            self.ui.deleteButton, self.ui.selectButton, self.ui.mouseButton, self.ui.repeatButton,
                            self.ui.keyboardButton]
        for button in self.button_list:
            button.clicked.connect(self.button_click_handler)
        self.load_items()
        self.load_signals()

    def save_hotkeys(self):
        global standart_hotkey_list
        value_list = [self.button_list[x].text() for x in range(3)]
        for x in range(len(value_list)):
            if not value_list[x]:
                value_list[x] = standart_hotkey_list[x]
        save_values_of_buttons(value_list)
        self.load_hotkey_button_values()

    def hotkey_button_read(self, button):
        hotkey = read_hotkey(suppress=False)
        if not hotkey in read_values_of_button():
            if self.hotkey_button_is_selected(button):
                button.setText(hotkey)
        self.hotkey_button_remove_selected(button)

    def hotkey_onkey_click(self, button):
        if self.hotkey_button_is_selected(button):
            self.hotkey_button_remove_selected(button)
            button.setText('')
        else:
            threading.Thread(target=self.hotkey_button_read, args=(button,)).start()
            self.hotkey_button_make_selected(button)

    def hotkey_button_is_selected(self, button):
        return button.styleSheet()

    def hotkey_button_make_selected(self, button):
        if self.hotkey_button_is_any_selected():
            self.hotkey_button_remove_all_selected()
        button.setStyleSheet('background-color: #E0E0E0;')

    def hotkey_button_remove_selected(self, button):
        button.setStyleSheet('')

    def hotkey_button_remove_all_selected(self):
        for button in self.button_list:
            self.hotkey_button_remove_selected(button)

    def hotkey_button_is_any_selected(self):
        for button in self.button_list:
            if self.hotkey_button_is_selected(button):
                return button
        return False

    def load_hotkey_button_values(self):
        values = read_values_of_button()
        for x in range(len(values)):
            self.button_list[x].setText(values[x])
        self.scene_hotkey_activate(values)

    def scene_hotkey_activate(self, hotkeys):
        remove_all_hotkeys()
        add_hotkey(hotkeys[0], self.scene_start), add_hotkey(hotkeys[1], self.scene_stop), add_hotkey(hotkeys[2],
                                                                                                      self.scene_play)

    def scene_stop(self):
        if self.scene_playing:
            return
        if self.scene_recording:
            self.scene_stop_process()
        self.scene_recording = False
        self.load_record_button()

    def scene_stop_process(self):
        threading.Thread(target=self.listener.stop).start()
        self.ui.nameLabel.setText('NO')
        self.ui.weightLabel.setText('NO')
        self.ui.timeLabel.setText(f'{toFixed(self.scene_time("", from_file=False), 3)} s')

    def scene_start(self):
        if self.scene_playing:
            return
        self.scene_recording = not self.scene_recording
        self.load_record_button()
        if self.scene_recording:
            self.listener.clear_log()
            threading.Thread(target=self.listener.run, args=(self.spec_values[0], self.spec_values[1])).start()
        else:
            self.scene_stop_process()

    def scene_playing_thread(self, log):
        mcontrol = mouse.Controller()
        while self.scene_playing:
            this_time = 0
            for line in log:
                if not self.scene_playing:
                    return
                mlist = line.split()
                sleep((float(mlist[0])-this_time)/self.speed)
                this_time = float(mlist[0])
                try:
                    if mlist[1] == 'mouseOnMove':
                        mcontrol.position = (int(mlist[2]), int(mlist[3]))
                    elif mlist[1] == 'mouseOnClick':
                        mcontrol.position = (int(mlist[2]), int(mlist[3]))
                        button = ''
                        if mlist[4] == 'Button.left':
                            button = mouse.Button.left
                        elif mlist[4] == 'Button.right':
                            button = mouse.Button.right
                        elif mlist[4] == 'Button.middle':
                            button = mouse.Button.middle
                        if mlist[5] == 'True':
                            mcontrol.press(button)
                        elif mlist[5] == 'False':
                            mcontrol.release(button)
                        else:
                            raise ValueError
                    elif mlist[1] == 'mouseOnScroll':
                        mouse.position = (int(mlist[2]), int(mlist[3]))
                        mouse.scroll(int(mlist[4]), int(mlist[5]))
                    elif mlist[1] == 'keyboard':
                        if mlist[3] == 'up':
                            press(mlist[2])
                        elif mlist[3] == 'down':
                            release(mlist[2])
                    else:
                        raise ValueError
                except:
                    pass
            if not self.spec_values[2]:
                break
        self.scene_playing = False
        self.load_play_button()

    def scene_play(self):
        if self.scene_recording:
            return
        self.scene_playing = not self.scene_playing
        self.load_play_button()
        if self.scene_playing:
            self.speed = self.ui.doubleSpinBox.value()
            log = self.listener.get_log()
            if log:
                threading.Thread(target=self.scene_playing_thread, args=(log,)).start()
        else:
            self.scene_playing = False

    def scene_time(self, name, from_file=True):
        if from_file:
            with open(f'{name}.ckr') as inf:
                mlist = inf.read()
                if mlist:
                    a = re.findall(r'(\d+\.\d+)', str(mlist).strip('[]'))
                    if a:
                        return float(a[-1])
                    else:
                        return 0
                else:
                    return 0
        else:
            if self.listener.get_log():
                return float(self.listener.get_log()[-1].split()[0])
            else:
                return 0

    def save_scene_to_file(self):
        name, log = self.ui.lineEdit.text(), self.listener.get_log()
        if name and log:
            dir_name, text = f'{name}.ckr', ''
            if os.path.exists(dir_name):
                index = 2
                dir_name = f'{name}({index}).ckr'
                while os.path.exists(dir_name):
                    index += 1
                    dir_name = f'{name}({index}).ckr'
            for line in log:
                text += f'{line}\n'
            with open(dir_name, 'w') as ouf:
                ouf.write(text[:-1])
            self.listView_load_items()
        else:
            if not name:
                threading.Thread(target=self.animate_lineEdit_name).start()
            elif not log:
                threading.Thread(target=self.animate_lineEdit_log).start()

    def read_scene_file(self, name):
        if os.path.exists(f'{name}.ckr'):
            returned_list = []
            with open(f'{name}.ckr') as inf:
                for line in inf:
                    returned_list.append(line.strip())
            return returned_list
        return False


    def listView_load_items(self):
        model = QtGui.QStandardItemModel()
        self.ui.listView.setModel(model)
        for item in os.listdir():
            ras = os.path.splitext(item)[1]
            if ras == '.ckr':
                item = QtGui.QStandardItem(item)
                item.setEditable(False)
                model.appendRow(item)

    def on_select_item(self, index):
        self.selected_item = index
        self.ui.nameLabel_2.setText(index.data())
        self.ui.weightLabel_2.setText(f'{toFixed(os.path.getsize(index.data())/1024,2)} Кб')
        date = str(ctime(os.path.getctime(index.data())))
        self.ui.dateLabel.setText(date[date.find(' ')+1:date.rfind(' ')])
        self.ui.timeLabel_2.setText(f'{toFixed(self.scene_time(index.data()[:index.data().find(".")], from_file=True), 3)} мс')

    def delete_item(self):
        os.remove(self.selected_item.data())
        model = QtGui.QStandardItemModel()
        self.ui.listView.setModel(model)
        model.removeRow(self.selected_item.row())
        self.listView_load_items()

    def on_select_button(self):
        if self.selected_item:
            self.ui.nameLabel.setText(self.selected_item.data())
            self.ui.weightLabel.setText(f'{toFixed(os.path.getsize(self.selected_item.data()) / 1024, 2)} Кб')
            self.ui.timeLabel.setText(f'{toFixed(self.scene_time(self.selected_item.data()[:self.selected_item.data().find(".")], from_file=True), 3)} с')
            self.listener.set_log(self.read_scene_file(self.selected_item.data()[:self.selected_item.data().find('.')]))

    def animate_lineEdit_log(self):
        self.ui.lineEdit.setText('')
        text = self.ui.lineEdit.placeholderText()
        self.ui.lineEdit.setPlaceholderText("Вы не записали сценарий")
        sleep(5)
        self.ui.lineEdit.setPlaceholderText(text)

    def animate_lineEdit_name(self):
        text = self.ui.lineEdit.placeholderText()
        self.ui.lineEdit.setPlaceholderText('Вы не указали название')
        sleep(5)
        self.ui.lineEdit.setPlaceholderText(text)

    def load_items(self):
        self.ui.lineEdit.setPlaceholderText('Название сценария')
        check_folder_of_data()
        self.load_hotkey_button_values()
        self.load_images()
        self.listView_load_items()

    def load_signals(self):
        self.ui.saveButton.clicked.connect(self.save_hotkeys)
        self.ui.startRecordButton.clicked.connect(self.scene_start)
        self.ui.playButton.clicked.connect(self.scene_play)
        self.ui.addButton.clicked.connect(self.save_scene_to_file)
        self.ui.listView.clicked.connect(self.on_select_item)
        self.ui.deleteButton.clicked.connect(self.delete_item)
        self.ui.selectButton.clicked.connect(self.on_select_button)
        self.ui.githubLink.clicked.connect(lambda: webbrowser.open('https://github.com/neiroun'))
        self.ui.mouseButton.clicked.connect(lambda: self.specButton_onclick(0))
        self.ui.keyboardButton.clicked.connect(lambda: self.specButton_onclick(1))
        self.ui.repeatButton.clicked.connect(lambda: self.specButton_onclick(2))

    def specButton_onclick(self, index):
        self.spec_values[index] = not self.spec_values[index]
        if self.spec_values[index]:
            self.sender().setText('ВКЛ')
        else:
            self.sender().setText('ВЫКЛ')

    def button_click_handler(self):
        button = self.sender()
        if button in self.button_list[:3]:
            self.hotkey_onkey_click(button)
        else:
            threading.Thread(target=self.button_animation_thread, args=(button,)).start()

    def button_animation_thread(self, button):
        button.setStyleSheet('background-color: #E0E0E0;')
        sleep(0.1)
        button.setStyleSheet('')

    def load_play_button(self):
        try:
            os.chdir('../img')
            icon = ''
            if self.scene_playing:
                icon = QtGui.QIcon('stop_red.png')
            else:
                icon = QtGui.QIcon('start_red.png')
            os.chdir('../data')
        except:
            pass
        else:
            self.ui.playButton.setIcon(icon)


    def load_record_button(self):
        try:
            os.chdir('../img')
            icon = ''
            if self.scene_recording:
                icon = QtGui.QIcon('stop_blue.png')
            else:
                icon = QtGui.QIcon('start_blue.png')
            os.chdir('../data')
        except:
            pass
        else:
            self.ui.startRecordButton.setIcon(icon)

    def load_other_images(self):
        try:
            os.chdir('../img')
            github_pixmap = QtGui.QPixmap('github.png')
            youtube_pixmap = QtGui.QPixmap('youtube.png')
            os.chdir('../data')
        except:
            pass
        else:
            self.ui.youtubeIcon.setPixmap(youtube_pixmap)
            self.ui.githubIcon.setPixmap(github_pixmap)


    def load_images(self):
        self.load_play_button()
        self.load_other_images()
        self.load_record_button()


if __name__ == '__main__':
    app = QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec())