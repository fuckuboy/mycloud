# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\bakalavr\diplom\mycloud\ui\register_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(385, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fio_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.fio_txt.setGeometry(QtCore.QRect(40, 80, 311, 20))
        self.fio_txt.setObjectName("fio_txt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.role_cmb = QtWidgets.QComboBox(self.centralwidget)
        self.role_cmb.setGeometry(QtCore.QRect(40, 130, 311, 22))
        self.role_cmb.setObjectName("role_cmb")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 47, 13))
        self.label_4.setObjectName("label_4")
        self.login_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.login_txt.setGeometry(QtCore.QRect(40, 190, 311, 20))
        self.login_txt.setObjectName("login_txt")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 220, 47, 13))
        self.label_5.setObjectName("label_5")
        self.password_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.password_txt.setGeometry(QtCore.QRect(40, 240, 311, 20))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.password_txt.setFont(font)
        self.password_txt.setInputMask("")
        self.password_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_txt.setPlaceholderText("")
        self.password_txt.setObjectName("password_txt")
        self.register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(80, 300, 231, 51))
        self.register_btn.setObjectName("register_btn")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(140, 270, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("color: rgb(0, 0, 255);")
        self.login_btn.setObjectName("login_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Регистрация"))
        self.label_2.setText(_translate("MainWindow", "ФИО"))
        self.label_3.setText(_translate("MainWindow", "Должность"))
        self.label_4.setText(_translate("MainWindow", "Логин"))
        self.label_5.setText(_translate("MainWindow", "Пароль"))
        self.register_btn.setText(_translate("MainWindow", "Зарегистрировать"))
        self.login_btn.setText(_translate("MainWindow", "Уже есть аккаунт?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
