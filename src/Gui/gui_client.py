# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from NetworkConnection.client import Client
from Crypto.PublicKey import RSA
import os
import os.path


class Ui_MainWindow(object):
    def __init__(self):
        self.fio = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fioEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fioEdit.setGeometry(QtCore.QRect(100, 20, 351, 20))
        self.fioEdit.setObjectName("fioEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.approveButton = QtWidgets.QPushButton(self.centralwidget)
        self.approveButton.setGeometry(QtCore.QRect(480, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.approveButton.setFont(font)
        self.approveButton.setObjectName("approveButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.createDESButton = QtWidgets.QPushButton(self.centralwidget)
        self.createDESButton.setGeometry(QtCore.QRect(480, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createDESButton.setFont(font)
        self.createDESButton.setObjectName("createDESButton")
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setGeometry(QtCore.QRect(434, 170, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.questionLabel.setFont(font)
        self.questionLabel.setObjectName("questionLabel")
        self.yesBox = QtWidgets.QCheckBox(self.centralwidget)
        self.yesBox.setGeometry(QtCore.QRect(430, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.yesBox.setFont(font)
        self.yesBox.setObjectName("yesBox")
        self.noBox = QtWidgets.QCheckBox(self.centralwidget)
        self.noBox.setGeometry(QtCore.QRect(430, 240, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.noBox.setFont(font)
        self.noBox.setObjectName("noBox")
        self.voteButton = QtWidgets.QPushButton(self.centralwidget)
        self.voteButton.setGeometry(QtCore.QRect(430, 270, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.voteButton.setFont(font)
        self.voteButton.setObjectName("voteButton")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(40, 370, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(430, 320, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName("resultLabel")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(70, 110, 256, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ####################################
        #           user code
        ####################################

        self.fio = ""
        self.client = Client()
        self.passphrase = "NiktoNeUgadaet"
        self.public_key = ""

        self.approveButton.clicked.connect(self.get_fio)
        self.updateButton.clicked.connect(self.update_info)
        self.createDESButton.clicked.connect(self.create_des)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client_blyat"))
        self.label.setText(_translate("MainWindow", "Твое ФИО"))
        self.approveButton.setText(_translate("MainWindow", "Подтвердить"))
        self.label_2.setText(_translate("MainWindow", "Участники голосования"))
        self.createDESButton.setText(_translate("MainWindow", "Создать Ключи ЭЦП"))
        self.questionLabel.setText(_translate("MainWindow", "Вопрос голосования"))
        self.yesBox.setText(_translate("MainWindow", " Да (манда)"))
        self.noBox.setText(_translate("MainWindow", " Нет (пидора ответ)"))
        self.voteButton.setText(_translate("MainWindow", "Press F to Vote"))
        self.updateButton.setText(_translate("MainWindow", "Обновить информацию"))
        self.resultLabel.setText(_translate("MainWindow", "Победил ответ...."))

    def get_fio(self):
        self.fio = self.fioEdit.text().lower()

    def update_info(self):
        self.client.update_info()


    def create_des(self):
        if os.path.exists("./private_key"):
            return
        key = RSA.generate(1024, os.urandom)
        with open("./private_key", "wb") as f:
            f.write(key.export_key('PEM', passphrase=self.passphrase))
        self.public_key = key.public_key().export_key('PEM')
        print(self.public_key)
        self.client.add_user(self.fio, self.public_key)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
