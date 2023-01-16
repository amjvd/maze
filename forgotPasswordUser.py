# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotPasswordUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forgotPasswordUserPage(object):
    def setupUi(self, forgotPasswordUserPage):
        forgotPasswordUserPage.setObjectName("forgotPasswordUserPage")
        forgotPasswordUserPage.resize(585, 804)
        forgotPasswordUserPage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(forgotPasswordUserPage)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 40, 521, 701))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 166);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lblname = QtWidgets.QLabel(self.frame)
        self.lblname.setGeometry(QtCore.QRect(80, 220, 151, 16))
        self.lblname.setStyleSheet("font: 75 17pt \"MS Serif\";")
        self.lblname.setObjectName("lblname")
        self.txtusername = QtWidgets.QLineEdit(self.frame)
        self.txtusername.setGeometry(QtCore.QRect(300, 220, 113, 20))
        self.txtusername.setObjectName("txtusername")
        self.btnclear = QtWidgets.QPushButton(self.frame)
        self.btnclear.setGeometry(QtCore.QRect(290, 450, 111, 41))
        self.btnclear.setObjectName("btnclear")
        self.btnsubmit = QtWidgets.QPushButton(self.frame)
        self.btnsubmit.setGeometry(QtCore.QRect(90, 450, 111, 41))
        self.btnsubmit.setObjectName("btnsubmit")
        self.btnlogin = QtWidgets.QPushButton(self.frame)
        self.btnlogin.setGeometry(QtCore.QRect(90, 560, 111, 41))
        self.btnlogin.setObjectName("btnlogin")
        self.lbltitle = QtWidgets.QLabel(self.frame)
        self.lbltitle.setGeometry(QtCore.QRect(20, 10, 351, 71))
        self.lbltitle.setStyleSheet("font: 75 48pt \"Rockwell Condensed\";")
        self.lbltitle.setObjectName("lbltitle")
        self.lbllogo = QtWidgets.QLabel(self.frame)
        self.lbllogo.setGeometry(QtCore.QRect(360, 10, 151, 171))
        self.lbllogo.setText("")
        self.lbllogo.setPixmap(QtGui.QPixmap("Images/Logo.png"))
        self.lbllogo.setScaledContents(True)
        self.lbllogo.setObjectName("lbllogo")
        self.btnregister = QtWidgets.QPushButton(self.frame)
        self.btnregister.setGeometry(QtCore.QRect(290, 560, 111, 41))
        self.btnregister.setObjectName("btnregister")
        forgotPasswordUserPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(forgotPasswordUserPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        forgotPasswordUserPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(forgotPasswordUserPage)
        self.statusbar.setObjectName("statusbar")
        forgotPasswordUserPage.setStatusBar(self.statusbar)

        self.retranslateUi(forgotPasswordUserPage)
        QtCore.QMetaObject.connectSlotsByName(forgotPasswordUserPage)

    def retranslateUi(self, forgotPasswordUserPage):
        _translate = QtCore.QCoreApplication.translate
        forgotPasswordUserPage.setWindowTitle(_translate("forgotPasswordUserPage", "MainWindow"))
        self.lblname.setText(_translate("forgotPasswordUserPage", "Username"))
        self.btnclear.setText(_translate("forgotPasswordUserPage", "Clear"))
        self.btnsubmit.setText(_translate("forgotPasswordUserPage", "Submit"))
        self.btnlogin.setText(_translate("forgotPasswordUserPage", "Login"))
        self.lbltitle.setText(_translate("forgotPasswordUserPage", "Forgot Password Page"))
        self.btnregister.setText(_translate("forgotPasswordUserPage", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    forgotPasswordUserPage = QtWidgets.QMainWindow()
    ui = Ui_forgotPasswordUserPage()
    ui.setupUi(forgotPasswordUserPage)
    forgotPasswordUserPage.show()
    sys.exit(app.exec_())