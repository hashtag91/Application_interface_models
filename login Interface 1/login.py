# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qtwidgets import PasswordEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 528)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"#LeftFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#RightFrame{\n"
"    \n"
"    background-color: rgb(166, 166, 166);\n"
"}\n"
"#RightPic{\n"
"    background : Transparent;\n"
"    border : none;\n"
"}\n"
"#usernameFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom : 3px solid gray;\n"
"}\n"
"#usernameFrame QLabel{\n"
"    background : transparent;\n"
"    border : none;\n"
"}\n"
"#usernameLine{\n"
"    background : transparent;\n"
"    border : none;\n"
"}\n"
"#passwordFrame{\n"
"    background : rgb(255,255,255);\n"
"    border-bottom : 3px solid gray;\n"
"}\n"
"#passwordFrame QLabel{\n"
"    background : transparent;\n"
"    border : none;\n"
"}\n"
"#passwordFrame QLineEdit{\n"
"    background : transparent;\n"
"    border : none;\n"
"}\n"
"#submit{\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-radius : 15px;\n"
"    color : white;\n"
"}\n"
"#submit:hover{\n"
"    background-color: rgb(92, 107, 149);\n"
"}\n"
"#signupBtn{\n"
"    background : transparent;\n"
"    border : none;\n"
"}\n"
"#signupBtn:hover{\n"
"    color : blue;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(80, 50, 80, 50)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftFrame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LeftFrame.setFont(font)
        self.LeftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftFrame.setObjectName("LeftFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LeftFrame)
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.LeftFrame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background : transparent;\n"
"border : None;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.usernameFrame = QtWidgets.QFrame(self.LeftFrame)
        self.usernameFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.usernameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usernameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usernameFrame.setObjectName("usernameFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.usernameFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.usernameFrame)
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ico/mail.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.usernameLine = QtWidgets.QLineEdit(self.usernameFrame)
        self.usernameLine.setMinimumSize(QtCore.QSize(0, 30))
        self.usernameLine.setMaximumSize(QtCore.QSize(16777215, 30))
        self.usernameLine.setObjectName("usernameLine")
        self.horizontalLayout_3.addWidget(self.usernameLine)
        self.verticalLayout.addWidget(self.usernameFrame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.passwordFrame = QtWidgets.QFrame(self.LeftFrame)
        self.passwordFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.passwordFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.passwordFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passwordFrame.setObjectName("passwordFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.passwordFrame)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.passwordFrame)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(30, 30))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ico/password.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.passwordLine = PasswordEdit(self.passwordFrame)
        self.passwordLine.setMinimumSize(QtCore.QSize(0, 30))
        self.passwordLine.setMaximumSize(QtCore.QSize(16777215, 30))
        self.passwordLine.setObjectName("passwordLine")
        self.horizontalLayout_4.addWidget(self.passwordLine)
        self.verticalLayout.addWidget(self.passwordFrame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.submit = QtWidgets.QPushButton(self.LeftFrame)
        self.submit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.submitAction)
        self.verticalLayout.addWidget(self.submit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.LeftFrame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background : transparent;\n"
"border : none;")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.signupBtn = QtWidgets.QPushButton(self.LeftFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.signupBtn.setFont(font)
        self.signupBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupBtn.setObjectName("signupBtn")
        self.horizontalLayout_5.addWidget(self.signupBtn)
        self.horizontalLayout_5.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(8, 1)
        self.horizontalLayout.addWidget(self.LeftFrame)
        self.RightFrame = QtWidgets.QFrame(self.centralwidget)
        self.RightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightFrame.setObjectName("RightFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.RightFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RightPic = QtWidgets.QLabel(self.RightFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightPic.sizePolicy().hasHeightForWidth())
        self.RightPic.setSizePolicy(sizePolicy)
        self.RightPic.setMaximumSize(QtCore.QSize(250, 400))
        self.RightPic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RightPic.setText("")
        self.RightPic.setPixmap(QtGui.QPixmap("Cool.png"))
        self.RightPic.setScaledContents(True)
        self.RightPic.setAlignment(QtCore.Qt.AlignCenter)
        self.RightPic.setObjectName("RightPic")
        self.horizontalLayout_2.addWidget(self.RightPic)
        self.horizontalLayout.addWidget(self.RightFrame)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Login System", "Login System"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.usernameLine.setPlaceholderText(_translate("MainWindow", "Enter your username *"))
        self.passwordLine.setPlaceholderText(_translate("MainWindow", "Enter your password *"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have an account ?"))
        self.signupBtn.setText(_translate("MainWindow", " Signup now"))
    def msgBox(self):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please fill all fields")
            msg.setStyleSheet("color : red")
            msg.exec()
    def submitAction(self):
            if self.usernameLine.text() == "":
                self.msgBox()
            elif self.passwordLine.text() == "":
                self.msgBox()
            else:
                print(self.usernameLine.text())
                print(self.passwordLine.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Login System")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
