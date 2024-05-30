from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegisterPage(object):
    def setupUi(self, RegisterPage):
        RegisterPage.setObjectName("RegisterPage")
        RegisterPage.resize(444, 704)
        RegisterPage.setWindowTitle("Register - PowerWatch")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        RegisterPage.setWindowIcon(icon)
        RegisterPage.setStyleSheet("* {\n"
"background-color: #111010;\n"
"color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=RegisterPage)
        self.centralwidget.setStyleSheet("QPushButton { \n"
"padding: 3px;\n"
"border-color: white;\n"
"border: 1px solid white;\n"
"color: black;\n"
"background-color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"  background-color: #facc15; /* Yellow shade */\n"
"  color: black; /* Text color */\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #facc15;\n"
"        color: #000000;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover:!pressed {\n"
"        background-color: #eab308;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        background-color: grey;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widgetHeader = QtWidgets.QWidget(parent=self.frame)
        self.widgetHeader.setMinimumSize(QtCore.QSize(400, 0))
        self.widgetHeader.setObjectName("widgetHeader")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetHeader)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLogo = QtWidgets.QLabel(parent=self.widgetHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLogo.sizePolicy().hasHeightForWidth())
        self.labelLogo.setSizePolicy(sizePolicy)
        self.labelLogo.setMaximumSize(QtCore.QSize(200, 200))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout_2.addWidget(self.labelLogo)
        self.verticalLayout_7.addWidget(self.widgetHeader, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.frameMain = QtWidgets.QFrame(parent=self.frame)
        self.frameMain.setMinimumSize(QtCore.QSize(300, 0))
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMain.setObjectName("frameMain")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameMain)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frameName = QtWidgets.QFrame(parent=self.frameMain)
        self.frameName.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameName.setObjectName("frameName")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameName)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelName = QtWidgets.QLabel(parent=self.frameName)
        self.labelName.setStyleSheet("")
        self.labelName.setObjectName("labelName")
        self.verticalLayout_5.addWidget(self.labelName)
        self.inputName = QtWidgets.QLineEdit(parent=self.frameName)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputName.sizePolicy().hasHeightForWidth())
        self.inputName.setSizePolicy(sizePolicy)
        self.inputName.setStyleSheet("padding: 4px;\n"
"color: black;\n"
"background-color: white;")
        self.inputName.setFrame(False)
        self.inputName.setObjectName("inputName")
        self.verticalLayout_5.addWidget(self.inputName)
        self.verticalLayout_6.addWidget(self.frameName)
        self.frameSurname = QtWidgets.QFrame(parent=self.frameMain)
        self.frameSurname.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameSurname.setObjectName("frameSurname")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameSurname)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelSurname = QtWidgets.QLabel(parent=self.frameSurname)
        self.labelSurname.setStyleSheet("")
        self.labelSurname.setObjectName("labelSurname")
        self.verticalLayout_4.addWidget(self.labelSurname)
        self.inputSurname = QtWidgets.QLineEdit(parent=self.frameSurname)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputSurname.sizePolicy().hasHeightForWidth())
        self.inputSurname.setSizePolicy(sizePolicy)
        self.inputSurname.setStyleSheet("padding: 4px;\n"
"color: black;\n"
"background-color: white;")
        self.inputSurname.setFrame(False)
        self.inputSurname.setObjectName("inputSurname")
        self.verticalLayout_4.addWidget(self.inputSurname)
        self.verticalLayout_6.addWidget(self.frameSurname)
        self.frameUsername = QtWidgets.QFrame(parent=self.frameMain)
        self.frameUsername.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameUsername.setObjectName("frameUsername")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameUsername)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUsername = QtWidgets.QLabel(parent=self.frameUsername)
        self.labelUsername.setStyleSheet("")
        self.labelUsername.setObjectName("labelUsername")
        self.verticalLayout.addWidget(self.labelUsername)
        self.inputUsername = QtWidgets.QLineEdit(parent=self.frameUsername)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputUsername.sizePolicy().hasHeightForWidth())
        self.inputUsername.setSizePolicy(sizePolicy)
        self.inputUsername.setStyleSheet("padding: 4px;\n"
"color: black;\n"
"background-color: white;")
        self.inputUsername.setText("")
        self.inputUsername.setFrame(False)
        self.inputUsername.setObjectName("inputUsername")
        self.verticalLayout.addWidget(self.inputUsername)
        self.verticalLayout_6.addWidget(self.frameUsername)
        self.framePassword = QtWidgets.QFrame(parent=self.frameMain)
        self.framePassword.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.framePassword.setObjectName("framePassword")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.framePassword)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelPassword = QtWidgets.QLabel(parent=self.framePassword)
        self.labelPassword.setStyleSheet("")
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout_2.addWidget(self.labelPassword)
        self.inputPassword = QtWidgets.QLineEdit(parent=self.framePassword)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPassword.sizePolicy().hasHeightForWidth())
        self.inputPassword.setSizePolicy(sizePolicy)
        self.inputPassword.setStyleSheet("padding: 4px;\n"
"color: black;\n"
"background-color: white;")
        self.inputPassword.setFrame(False)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.verticalLayout_2.addWidget(self.inputPassword)
        self.verticalLayout_6.addWidget(self.framePassword)
        self.frameButtons = QtWidgets.QFrame(parent=self.frameMain)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRegister = QtWidgets.QPushButton(parent=self.frameButtons)
        self.btnRegister.setStyleSheet("")
        self.btnRegister.setObjectName("btnRegister")
        self.horizontalLayout.addWidget(self.btnRegister)
        self.verticalLayout_6.addWidget(self.frameButtons)
        self.verticalLayout_7.addWidget(self.frameMain, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_3.addWidget(self.frame)
        RegisterPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RegisterPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 26))
        self.menubar.setObjectName("menubar")
        RegisterPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RegisterPage)
        self.statusbar.setObjectName("statusbar")
        RegisterPage.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterPage)
        QtCore.QMetaObject.connectSlotsByName(RegisterPage)

    def retranslateUi(self, RegisterPage):
        _translate = QtCore.QCoreApplication.translate
        self.labelName.setText(_translate("RegisterPage", "Name"))
        self.labelSurname.setText(_translate("RegisterPage", "Surname"))
        self.labelUsername.setText(_translate("RegisterPage", "Username"))
        self.labelPassword.setText(_translate("RegisterPage", "Password"))
        self.btnRegister.setText(_translate("RegisterPage", "Register"))
