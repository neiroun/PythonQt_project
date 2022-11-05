# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clickrecorder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 250)
        MainWindow.setMinimumSize(QtCore.QSize(420, 250))
        MainWindow.setMaximumSize(QtCore.QSize(420, 250))
        MainWindow.setStyleSheet(".QMainWindow{\n"
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

