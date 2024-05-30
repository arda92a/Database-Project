from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.setEnabled(True)
        LoginPage.resize(444, 548)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        LoginPage.setWindowIcon(icon)
        LoginPage.setAutoFillBackground(False)
        LoginPage.setStyleSheet("* {\n"
"    background-color: #111010;\n"
"    color: white;\n"
"}")
        LoginPage.setDockNestingEnabled(True)
        LoginPage.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=LoginPage)
        self.centralwidget.setEnabled(True)
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
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widgetHeader = QtWidgets.QWidget(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetHeader.sizePolicy().hasHeightForWidth())
        self.widgetHeader.setSizePolicy(sizePolicy)
        self.widgetHeader.setMinimumSize(QtCore.QSize(400, 0))
        self.widgetHeader.setObjectName("widgetHeader")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetHeader)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLogo = QtWidgets.QLabel(parent=self.widgetHeader)
        self.labelLogo.setMaximumSize(QtCore.QSize(200, 200))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout_2.addWidget(self.labelLogo, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_5.addWidget(self.widgetHeader, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.frameMain = QtWidgets.QFrame(parent=self.frame)
        self.frameMain.setMinimumSize(QtCore.QSize(300, 0))
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMain.setObjectName("frameMain")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameMain)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
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
        self.inputUsername.setStyleSheet("padding: 4px;\n"
"color: black;\n"
"background-color: white;")
        self.inputUsername.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhLowercaseOnly)
        self.inputUsername.setFrame(False)
        self.inputUsername.setObjectName("inputUsername")
        self.verticalLayout.addWidget(self.inputUsername)
        self.verticalLayout_4.addWidget(self.frameUsername)
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
        self.inputPassword.setStyleSheet("padding: 4px;\n"
"color: black;\n"
"background-color: white;")
        self.inputPassword.setFrame(False)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.verticalLayout_2.addWidget(self.inputPassword)
        self.verticalLayout_4.addWidget(self.framePassword)
        self.frameButtons = QtWidgets.QFrame(parent=self.frameMain)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogin = QtWidgets.QPushButton(parent=self.frameButtons)
        self.btnLogin.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnLogin.setCheckable(False)
        self.btnLogin.setChecked(False)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnRegister = QtWidgets.QPushButton(parent=self.frameButtons)
        self.btnRegister.setStyleSheet("")
        self.btnRegister.setObjectName("btnRegister")
        self.horizontalLayout.addWidget(self.btnRegister)
        self.verticalLayout_4.addWidget(self.frameButtons)
        self.frameUsername.raise_()
        self.frameButtons.raise_()
        self.framePassword.raise_()
        self.verticalLayout_5.addWidget(self.frameMain, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_3.addWidget(self.frame)
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 26))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Login - PowerWatch"))
        self.labelUsername.setText(_translate("LoginPage", "Username"))
        self.labelPassword.setText(_translate("LoginPage", "Password"))
        self.btnLogin.setText(_translate("LoginPage", "Login"))
        self.btnRegister.setText(_translate("LoginPage", "Register"))
