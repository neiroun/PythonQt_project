# -*- coding: utf-8 -*-

# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 290)
        MainWindow.setMinimumSize(QtCore.QSize(420, 250))
        MainWindow.setMaximumSize(QtCore.QSize(420, 250))
        MainWindow.setStyleSheet(".QMainWindow{\n"
        "background-color: #000000;\n"
        "}\n"
        "\n"
        "\n"
        ".QPushButton{\n"
        "background-color: #FFFFFF;\n"
        "border: 1px solid #7A7A7A;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#hotkeyReader1, #hotkeyReader2, #hotkeyReader3{\n"
        "padding: 2px 0;\n"
        "}\n"
        "\n"
        "#saveButton{\n"
        "padding: 4px 0;  \n"
        "}\n"
        "\n"
        "#page1, #page2, #page3{\n"
        "background-color: #F0F0F0;\n"
        "}\n"
        "\n"
        "#frameWhite, #frameWhite_2, #frameWhite_3{\n"
        "border: 1px solid #7A7A7A;\n"
        "background-color: #FFF;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#playButton, #startRecordButton, #stopRecordButton{\n"
        "margin-top: 2px;\n"
        "width: 45px;\n"
        "height: 35px;\n"
        "}\n"
        "\n"
        "#greyFrame{\n"
        "border: 1px solid #7A7A7A;\n"
        "border-radius: 2px;\n"
        "background-color: #E3E3E3;\n"
        "}\n"
        "\n"
        "#selectButton, #deleteButton{\n"
        "padding: 7px 12px;\n"
        "margin-top: 2px;\n"
        "}\n"
        "\n"
        "#addButton, #addAllButton{\n"
        "border-radius: 0;\n"
        "}\n"
        "\n"
        "#infoLabel{\n"
        "line-height: 2px;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 471, 255))
        self.tabWidget.setObjectName("tabWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.line = QtWidgets.QFrame(self.page1)
        self.line.setGeometry(QtCore.QRect(0, 150, 431, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.page1)
        self.line_2.setGeometry(QtCore.QRect(170, -20, 20, 177))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 10, 213, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 1, 1, 1)
        self.hotkeyReader1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.hotkeyReader1.setText("")
        self.hotkeyReader1.setObjectName("hotkeyReader1")
        self.gridLayout.addWidget(self.hotkeyReader1, 0, 1, 1, 1)
        self.hotkeyReader2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.hotkeyReader2.setText("")
        self.hotkeyReader2.setObjectName("hotkeyReader2")
        self.gridLayout.addWidget(self.hotkeyReader2, 1, 1, 1, 1)
        self.hotkeyReader3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.hotkeyReader3.setText("")
        self.hotkeyReader3.setObjectName("hotkeyReader3")
        self.gridLayout.addWidget(self.hotkeyReader3, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 121, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startRecordButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startRecordButton.setStyleSheet(".QMainWindow{\n"
        "background-color: #87CEEB;\n"
        "}\n"
        "\n"
        "\n"
        ".QPushButton{\n"
        "background-color: #FFF;\n"
        "border: 1px solid #7A7A7A;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#hotkeyReader1, #hotkeyReader2, #hotkeyReader3{\n"
        "padding: 2px 0;\n"
        "}\n"
        "\n"
        "#saveButton{\n"
        "padding: 4px 0;  \n"
        "}\n"
        "\n"
        "#page1, #page2, #page3{\n"
        "background-color: #F0F0F0;\n"
        "}\n"
        "\n"
        "#frameWhite, #frameWhite_2, #frameWhite_3{\n"
        "border: 1px solid #7A7A7A;\n"
        "background-color: #FFF;\n"
        "}\n"
        "\n"
        "#playButton, #startRecordButton, #stopRecordButton{\n"
        "width: 45px;\n"
        "height: 35px;\n"
        "}")
        self.startRecordButton.setText("")
        self.startRecordButton.setObjectName("startRecordButton")
        self.horizontalLayout.addWidget(self.startRecordButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.playButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 141, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.fileInfoGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.fileInfoGrid.setContentsMargins(0, 0, 0, 0)
        self.fileInfoGrid.setObjectName("fileInfoGrid")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.fileInfoGrid.addWidget(self.label_8, 2, 0, 1, 1)
        self.nameLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.nameLabel.setStyleSheet(".QMainWindow{\n"
        "background-color: #87CEEB;\n"
        "}\n"
        "\n"
        ".QPushButton{\n"
        "background-color: #FFF;\n"
        "border: 1px solid #000\n"
        "}")
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.fileInfoGrid.addWidget(self.nameLabel, 0, 1, 1, 1)
        self.weightLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.weightLabel.setText("")
        self.weightLabel.setObjectName("weightLabel")
        self.fileInfoGrid.addWidget(self.weightLabel, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.fileInfoGrid.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.fileInfoGrid.addWidget(self.label_6, 1, 0, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.timeLabel.setText("")
        self.timeLabel.setObjectName("timeLabel")
        self.fileInfoGrid.addWidget(self.timeLabel, 1, 1, 1, 1)
        self.frameWhite = QtWidgets.QFrame(self.page1)
        self.frameWhite.setGeometry(QtCore.QRect(19, 9, 151, 141))
        self.frameWhite.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWhite.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWhite.setObjectName("frameWhite")
        self.frameWhite_2 = QtWidgets.QFrame(self.page1)
        self.frameWhite_2.setGeometry(QtCore.QRect(189, 10, 234, 141))
        self.frameWhite_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWhite_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWhite_2.setObjectName("frameWhite_2")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.page1)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(170, 170, 251, 51))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_3.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.repeatButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.repeatButton.setObjectName("repeatButton")
        self.gridLayout_3.addWidget(self.repeatButton, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 1, 2, 1, 1)
        self.keyboardButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.keyboardButton.setObjectName("keyboardButton")
        self.gridLayout_3.addWidget(self.keyboardButton, 1, 1, 1, 1)
        self.mouseButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.mouseButton.setObjectName("mouseButton")
        self.gridLayout_3.addWidget(self.mouseButton, 1, 3, 1, 1)
        self.frameWhite_2.raise_()
        self.frameWhite.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_5.raise_()
        self.tabWidget.addTab(self.page1, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.addButton = QtWidgets.QPushButton(self.page2)
        self.addButton.setGeometry(QtCore.QRect(230, 10, 61, 20))
        self.addButton.setObjectName("addButton")
        self.lineEdit = QtWidgets.QLineEdit(self.page2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 211, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.frameWhite_3 = QtWidgets.QFrame(self.page2)
        self.frameWhite_3.setGeometry(QtCore.QRect(239, 50, 181, 161))
        self.frameWhite_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWhite_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWhite_3.setObjectName("frameWhite_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frameWhite_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 171, 161))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.fileInfoGrid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.fileInfoGrid_2.setContentsMargins(0, 0, 0, 0)
        self.fileInfoGrid_2.setObjectName("fileInfoGrid_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.fileInfoGrid_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.nameLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.nameLabel_2.setText("")
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.fileInfoGrid_2.addWidget(self.nameLabel_2, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.fileInfoGrid_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.timeLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.timeLabel_2.setText("")
        self.timeLabel_2.setObjectName("timeLabel_2")
        self.fileInfoGrid_2.addWidget(self.timeLabel_2, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.fileInfoGrid_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.dateLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.fileInfoGrid_2.addWidget(self.dateLabel, 3, 1, 1, 1)
        self.weightLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.weightLabel_2.setText("")
        self.weightLabel_2.setObjectName("weightLabel_2")
        self.fileInfoGrid_2.addWidget(self.weightLabel_2, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.fileInfoGrid_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.page2)
        self.line_3.setGeometry(QtCore.QRect(0, 30, 431, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.page2)
        self.line_4.setGeometry(QtCore.QRect(220, 40, 16, 201))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.listView = QtWidgets.QListView(self.page2)
        self.listView.setGeometry(QtCore.QRect(20, 50, 201, 131))
        self.listView.setObjectName("listView")
        self.greyFrame = QtWidgets.QFrame(self.page2)
        self.greyFrame.setGeometry(QtCore.QRect(20, 180, 201, 31))
        self.greyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.greyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.greyFrame.setObjectName("greyFrame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 174, 201, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.deleteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.selectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout_2.addWidget(self.selectButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.greyFrame.raise_()
        self.addButton.raise_()
        self.lineEdit.raise_()
        self.frameWhite_3.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.listView.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.tabWidget.addTab(self.page2, "")
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label_11 = QtWidgets.QLabel(self.page3)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 361, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page3)
        self.label_12.setGeometry(QtCore.QRect(20, 30, 381, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page3)
        self.label_13.setGeometry(QtCore.QRect(350, 210, 81, 16))
        self.label_13.setObjectName("label_13")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.page3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 70, 199, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.githubIcon = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.githubIcon.setText("")
        self.githubIcon.setObjectName("githubIcon")
        self.gridLayout_2.addWidget(self.githubIcon, 0, 0, 1, 1)
        self.youtubeIcon = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.githubLink = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_4)
        self.githubLink.setObjectName("githubLink")
        self.gridLayout_2.addWidget(self.githubLink, 0, 1, 1, 1)
        self.tabWidget.addTab(self.page3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recorder"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Воспроизвести запись:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Начать запись:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Остановить запись:</span></p></body></html>"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Вес:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Название:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Время:</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Повторение:</span></p></body></html>"))
        self.repeatButton.setText(_translate("MainWindow", "ВКЛ"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Ускорeние:</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Клавиатура:</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Мышь:</span></p></body></html>"))
        self.keyboardButton.setText(_translate("MainWindow", "ВКЛ"))
        self.mouseButton.setText(_translate("MainWindow", "ВКЛ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page1), _translate("MainWindow", "Основная"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Время:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Вес:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Дата создания:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Название:</span></p></body></html>"))
        self.greyFrame.setStyleSheet(_translate("MainWindow", ".QMainWindow{\n"
        "background-color: #6495ED;\n"
        "}\n"
        "\n"
        ".QPushButton{\n"
        "background-color: #FFFFFF;\n"
        "border: 1px solid #828790;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#page1, #page2, #page3{\n"
        "background-color: #F0F0F0;\n"
        "}\n"
        "\n"
        "#addButton, #addAllButton{\n"
        "border-radius: 0;\n"
        "}\n"
        "\n"
        "#startRecordButton, #stopRecordButton, #playButton{\n"
        "height: 35px;\n"
        "width: 50px;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#frameWhite, #frameWhite_2, #frameWhite_3{\n"
        "border: 1px solid #828790;\n"
        "background-color: #FFF;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#blueFrame, #blueFrame_2{\n"
        "background-color: #87CEEB;\n"
        "border: 1px solid #828790;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#selectButton, #deleteButton{\n"
        "padding: 4px 6px;\n"
        "border-radius: 2px;\n"
        "}\n"
        "\n"
        "#hotkeyReader1, #hotkeyReader2, #hotkeyReader3{\n"
        "padding: 2px 0;\n"
        "}\n"
        "\n"
        "#saveButton{\n"
        "padding: 3px 0;\n"
        "}"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.selectButton.setText(_translate("MainWindow", "Выбрать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page2), _translate("MainWindow", "Записи"))
        self.githubLink.setText(_translate("MainWindow", "Github neiroun"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page3), _translate("MainWindow", "Информация"))
