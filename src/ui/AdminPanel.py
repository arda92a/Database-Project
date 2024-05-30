from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(826, 634)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AdminPanel.setWindowIcon(icon)
        AdminPanel.setStyleSheet("* {\n"
"background-color: #111010;\n"
"color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=AdminPanel)
        self.centralwidget.setStyleSheet("QTabBar {\n"
"color: black;\n"
"}\n"
"QTabBar::tab {\n"
"background-color:#eab308;\n"
"}\n"
"QTabBar::tab:selected {\n"
"background-color: #facc15;\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"background-color: #eab308;\n"
"}\n"
"QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}\n"
"\n"
"QPushButton { \n"
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
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    background-color: black;\n"
"    selection-background-color: grey;\n"
"    color: white;\n"
"}\n"
"QDateEdit {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"}\n"
"QDateEdit::up-button, QDateEdit::down-button {\n"
"subcontrol-origin: padding;\n"
"}\n"
"QDateEdit::up-button {\n"
"subcontrol-position: top right;\n"
"}\n"
"QDateEdit::down-button {\n"
"subcontrol-position: bottom right;\n"
"}\n"
"QDoubleSpinBox {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"}\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: padding;\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color:#facc15;\n"
"    color: black;\n"
"    border-color: white;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border: 1px solid white;\n"
"    color:white;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border: 1px solid white;\n"
"}\n"
"\n"
"QTableView::item::selected {\n"
"    border-top: 1px solid #facc15;\n"
"    border-bottom: 1px solid #facc15;\n"
"}\n"
"QScrollBar {\n"
"background-color: #facc15;\n"
"}\n"
"QLineEdit {\n"
"padding: 3px;\n"
"color: black;\n"
"background-color: white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameHeader = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHeader.sizePolicy().hasHeightForWidth())
        self.frameHeader.setSizePolicy(sizePolicy)
        self.frameHeader.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameHeader.setObjectName("frameHeader")
        self.formLayout = QtWidgets.QFormLayout(self.frameHeader)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.widgetHeader = QtWidgets.QWidget(parent=self.frameHeader)
        self.widgetHeader.setObjectName("widgetHeader")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetHeader)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLogo = QtWidgets.QLabel(parent=self.widgetHeader)
        self.labelLogo.setMaximumSize(QtCore.QSize(50, 50))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout_2.addWidget(self.labelLogo)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widgetHeader)
        self.frameHeader_Name = QtWidgets.QFrame(parent=self.frameHeader)
        self.frameHeader_Name.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameHeader_Name.setObjectName("frameHeader_Name")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameHeader_Name)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelHeader_FNameandLnameDynamic = QtWidgets.QLabel(parent=self.frameHeader_Name)
        self.labelHeader_FNameandLnameDynamic.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelHeader_FNameandLnameDynamic.setObjectName("labelHeader_FNameandLnameDynamic")
        self.horizontalLayout.addWidget(self.labelHeader_FNameandLnameDynamic)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.frameHeader_Name)
        self.verticalLayout.addWidget(self.frameHeader)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabUserList = QtWidgets.QWidget()
        self.tabUserList.setObjectName("tabUserList")
        self.gridLayout = QtWidgets.QGridLayout(self.tabUserList)
        self.gridLayout.setObjectName("gridLayout")
        self.frameUserList = QtWidgets.QFrame(parent=self.tabUserList)
        self.frameUserList.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameUserList.setObjectName("frameUserList")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameUserList)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameHorizontalUserList = QtWidgets.QFrame(parent=self.frameUserList)
        self.frameHorizontalUserList.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameHorizontalUserList.setObjectName("frameHorizontalUserList")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameHorizontalUserList)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.inputUserList_Username = QtWidgets.QLineEdit(parent=self.frameHorizontalUserList)
        self.inputUserList_Username.setMinimumSize(QtCore.QSize(150, 0))
        self.inputUserList_Username.setFrame(False)
        self.inputUserList_Username.setObjectName("inputUserList_Username")
        self.horizontalLayout_3.addWidget(self.inputUserList_Username)
        self.btnUserList_OpenClient = QtWidgets.QPushButton(parent=self.frameHorizontalUserList)
        self.btnUserList_OpenClient.setObjectName("btnUserList_OpenClient")
        self.horizontalLayout_3.addWidget(self.btnUserList_OpenClient)
        self.btnUserLIst_ChangePassword = QtWidgets.QPushButton(parent=self.frameHorizontalUserList)
        self.btnUserLIst_ChangePassword.setObjectName("btnUserLIst_ChangePassword")
        self.horizontalLayout_3.addWidget(self.btnUserLIst_ChangePassword)
        self.btnUserList_ChangeUsername = QtWidgets.QPushButton(parent=self.frameHorizontalUserList)
        self.btnUserList_ChangeUsername.setObjectName("btnUserList_ChangeUsername")
        self.horizontalLayout_3.addWidget(self.btnUserList_ChangeUsername)
        self.btnUserList_MakeAdmin = QtWidgets.QPushButton(parent=self.frameHorizontalUserList)
        self.btnUserList_MakeAdmin.setObjectName("btnUserList_MakeAdmin")
        self.horizontalLayout_3.addWidget(self.btnUserList_MakeAdmin)
        self.btnUserList_DeleteUser = QtWidgets.QPushButton(parent=self.frameHorizontalUserList)
        self.btnUserList_DeleteUser.setObjectName("btnUserList_DeleteUser")
        self.horizontalLayout_3.addWidget(self.btnUserList_DeleteUser)
        self.verticalLayout_3.addWidget(self.frameHorizontalUserList, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.tableUserList = QtWidgets.QTableWidget(parent=self.frameUserList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableUserList.sizePolicy().hasHeightForWidth())
        self.tableUserList.setSizePolicy(sizePolicy)
        self.tableUserList.setStyleSheet("")
        self.tableUserList.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableUserList.setLineWidth(5)
        self.tableUserList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableUserList.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableUserList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableUserList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableUserList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableUserList.setObjectName("tableUserList")
        self.tableUserList.setColumnCount(5)
        self.tableUserList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUserList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUserList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUserList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUserList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUserList.setHorizontalHeaderItem(4, item)
        self.tableUserList.horizontalHeader().setDefaultSectionSize(156)
        self.tableUserList.horizontalHeader().setHighlightSections(False)
        self.tableUserList.horizontalHeader().setStretchLastSection(True)
        self.tableUserList.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableUserList, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.gridLayout.addWidget(self.frameUserList, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabUserList, "")
        self.tabStatistics = QtWidgets.QWidget()
        self.tabStatistics.setObjectName("tabStatistics")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabStatistics)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameMonthlyEnergyConsumptionStatistics = QtWidgets.QFrame(parent=self.tabStatistics)
        self.frameMonthlyEnergyConsumptionStatistics.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMonthlyEnergyConsumptionStatistics.setObjectName("frameMonthlyEnergyConsumptionStatistics")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frameMonthlyEnergyConsumptionStatistics)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.labelMonthlyEnergyConsumptionStatistics = QtWidgets.QLabel(parent=self.frameMonthlyEnergyConsumptionStatistics)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMonthlyEnergyConsumptionStatistics.setFont(font)
        self.labelMonthlyEnergyConsumptionStatistics.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelMonthlyEnergyConsumptionStatistics.setObjectName("labelMonthlyEnergyConsumptionStatistics")
        self.verticalLayout_19.addWidget(self.labelMonthlyEnergyConsumptionStatistics)
        self.frameHorizontalMonthlyEnergyConsumptionStatistics = QtWidgets.QFrame(parent=self.frameMonthlyEnergyConsumptionStatistics)
        self.frameHorizontalMonthlyEnergyConsumptionStatistics.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameHorizontalMonthlyEnergyConsumptionStatistics.setObjectName("frameHorizontalMonthlyEnergyConsumptionStatistics")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frameHorizontalMonthlyEnergyConsumptionStatistics)
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.formMonthlyEnergyConsumptionStatistics = QtWidgets.QFrame(parent=self.frameHorizontalMonthlyEnergyConsumptionStatistics)
        self.formMonthlyEnergyConsumptionStatistics.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.formMonthlyEnergyConsumptionStatistics.setObjectName("formMonthlyEnergyConsumptionStatistics")
        self.formLayout_13 = QtWidgets.QFormLayout(self.formMonthlyEnergyConsumptionStatistics)
        self.formLayout_13.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_13.setObjectName("formLayout_13")
        self.labelMonthlyEnergyConsumptionStatistics_MeterType = QtWidgets.QLabel(parent=self.formMonthlyEnergyConsumptionStatistics)
        self.labelMonthlyEnergyConsumptionStatistics_MeterType.setObjectName("labelMonthlyEnergyConsumptionStatistics_MeterType")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelMonthlyEnergyConsumptionStatistics_MeterType)
        self.comboMonthlyEnergyConsumptionStatistics_MeterType = QtWidgets.QComboBox(parent=self.formMonthlyEnergyConsumptionStatistics)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 204, 21))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 204, 21))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        self.comboMonthlyEnergyConsumptionStatistics_MeterType.setPalette(palette)
        self.comboMonthlyEnergyConsumptionStatistics_MeterType.setAutoFillBackground(False)
        self.comboMonthlyEnergyConsumptionStatistics_MeterType.setFrame(False)
        self.comboMonthlyEnergyConsumptionStatistics_MeterType.setObjectName("comboMonthlyEnergyConsumptionStatistics_MeterType")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboMonthlyEnergyConsumptionStatistics_MeterType)
        self.labelMonthlyEnergyConsumptionStatistics_Month = QtWidgets.QLabel(parent=self.formMonthlyEnergyConsumptionStatistics)
        self.labelMonthlyEnergyConsumptionStatistics_Month.setObjectName("labelMonthlyEnergyConsumptionStatistics_Month")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelMonthlyEnergyConsumptionStatistics_Month)
        self.comboMonthlyEnergyConsumptionStatistics_Month = QtWidgets.QComboBox(parent=self.formMonthlyEnergyConsumptionStatistics)
        self.comboMonthlyEnergyConsumptionStatistics_Month.setObjectName("comboMonthlyEnergyConsumptionStatistics_Month")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboMonthlyEnergyConsumptionStatistics_Month)
        self.labelMonthlyEnergyConsumptionStatistics_GraphType = QtWidgets.QLabel(parent=self.formMonthlyEnergyConsumptionStatistics)
        self.labelMonthlyEnergyConsumptionStatistics_GraphType.setObjectName("labelMonthlyEnergyConsumptionStatistics_GraphType")
        self.formLayout_13.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelMonthlyEnergyConsumptionStatistics_GraphType)
        self.comboMonthlyEnergyConsumptionStatistics_GraphType = QtWidgets.QComboBox(parent=self.formMonthlyEnergyConsumptionStatistics)
        self.comboMonthlyEnergyConsumptionStatistics_GraphType.setObjectName("comboMonthlyEnergyConsumptionStatistics_GraphType")
        self.comboMonthlyEnergyConsumptionStatistics_GraphType.addItem("")
        self.comboMonthlyEnergyConsumptionStatistics_GraphType.addItem("")
        self.formLayout_13.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboMonthlyEnergyConsumptionStatistics_GraphType)
        self.horizontalLayout_8.addWidget(self.formMonthlyEnergyConsumptionStatistics, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.graphicsMonthlyEnergyConsumptionStatistics = QtWidgets.QGraphicsView(parent=self.frameHorizontalMonthlyEnergyConsumptionStatistics)
        self.graphicsMonthlyEnergyConsumptionStatistics.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsMonthlyEnergyConsumptionStatistics.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsMonthlyEnergyConsumptionStatistics.setObjectName("graphicsMonthlyEnergyConsumptionStatistics")
        self.horizontalLayout_8.addWidget(self.graphicsMonthlyEnergyConsumptionStatistics)
        self.verticalLayout_19.addWidget(self.frameHorizontalMonthlyEnergyConsumptionStatistics)
        self.verticalLayout_2.addWidget(self.frameMonthlyEnergyConsumptionStatistics)
        self.frameTotalEnergyConsumptionStatistics = QtWidgets.QFrame(parent=self.tabStatistics)
        self.frameTotalEnergyConsumptionStatistics.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameTotalEnergyConsumptionStatistics.setObjectName("frameTotalEnergyConsumptionStatistics")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frameTotalEnergyConsumptionStatistics)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.labelTotalEnergyConsumptionStatistics = QtWidgets.QLabel(parent=self.frameTotalEnergyConsumptionStatistics)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelTotalEnergyConsumptionStatistics.setFont(font)
        self.labelTotalEnergyConsumptionStatistics.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTotalEnergyConsumptionStatistics.setObjectName("labelTotalEnergyConsumptionStatistics")
        self.verticalLayout_20.addWidget(self.labelTotalEnergyConsumptionStatistics)
        self.frameHorizontalTotalEnergyConsumptionStatistics = QtWidgets.QFrame(parent=self.frameTotalEnergyConsumptionStatistics)
        self.frameHorizontalTotalEnergyConsumptionStatistics.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameHorizontalTotalEnergyConsumptionStatistics.setObjectName("frameHorizontalTotalEnergyConsumptionStatistics")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frameHorizontalTotalEnergyConsumptionStatistics)
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.formTotalEnergyConsumptionStatistics = QtWidgets.QFrame(parent=self.frameHorizontalTotalEnergyConsumptionStatistics)
        self.formTotalEnergyConsumptionStatistics.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.formTotalEnergyConsumptionStatistics.setObjectName("formTotalEnergyConsumptionStatistics")
        self.formLayout_14 = QtWidgets.QFormLayout(self.formTotalEnergyConsumptionStatistics)
        self.formLayout_14.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_14.setObjectName("formLayout_14")
        self.labelTotalEnergyConsumptionStatistics_MeterType = QtWidgets.QLabel(parent=self.formTotalEnergyConsumptionStatistics)
        self.labelTotalEnergyConsumptionStatistics_MeterType.setObjectName("labelTotalEnergyConsumptionStatistics_MeterType")
        self.formLayout_14.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelTotalEnergyConsumptionStatistics_MeterType)
        self.comboTotalEnergyConsumptionStatistics_MeterType = QtWidgets.QComboBox(parent=self.formTotalEnergyConsumptionStatistics)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 204, 21))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 204, 21))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        self.comboTotalEnergyConsumptionStatistics_MeterType.setPalette(palette)
        self.comboTotalEnergyConsumptionStatistics_MeterType.setAutoFillBackground(False)
        self.comboTotalEnergyConsumptionStatistics_MeterType.setFrame(False)
        self.comboTotalEnergyConsumptionStatistics_MeterType.setObjectName("comboTotalEnergyConsumptionStatistics_MeterType")
        self.formLayout_14.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTotalEnergyConsumptionStatistics_MeterType)
        self.labelTotalEnergyConsumptionStatistics_GraphType = QtWidgets.QLabel(parent=self.formTotalEnergyConsumptionStatistics)
        self.labelTotalEnergyConsumptionStatistics_GraphType.setObjectName("labelTotalEnergyConsumptionStatistics_GraphType")
        self.formLayout_14.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelTotalEnergyConsumptionStatistics_GraphType)
        self.comboTotalEnergyConsumptionStatistics_GraphType = QtWidgets.QComboBox(parent=self.formTotalEnergyConsumptionStatistics)
        self.comboTotalEnergyConsumptionStatistics_GraphType.setObjectName("comboTotalEnergyConsumptionStatistics_GraphType")
        self.comboTotalEnergyConsumptionStatistics_GraphType.addItem("")
        self.comboTotalEnergyConsumptionStatistics_GraphType.addItem("")
        self.formLayout_14.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboTotalEnergyConsumptionStatistics_GraphType)
        self.horizontalLayout_9.addWidget(self.formTotalEnergyConsumptionStatistics, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.graphicsTotalEnergyConsumptionStatistics = QtWidgets.QGraphicsView(parent=self.frameHorizontalTotalEnergyConsumptionStatistics)
        self.graphicsTotalEnergyConsumptionStatistics.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsTotalEnergyConsumptionStatistics.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsTotalEnergyConsumptionStatistics.setObjectName("graphicsTotalEnergyConsumptionStatistics")
        self.horizontalLayout_9.addWidget(self.graphicsTotalEnergyConsumptionStatistics)
        self.verticalLayout_20.addWidget(self.frameHorizontalTotalEnergyConsumptionStatistics)
        self.verticalLayout_2.addWidget(self.frameTotalEnergyConsumptionStatistics)
        self.tabWidget.addTab(self.tabStatistics, "")
        self.verticalLayout.addWidget(self.tabWidget)
        AdminPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AdminPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 21))
        self.menubar.setObjectName("menubar")
        AdminPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AdminPanel)
        self.statusbar.setObjectName("statusbar")
        AdminPanel.setStatusBar(self.statusbar)

        self.retranslateUi(AdminPanel)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "Admin Panel - PowerWatch"))
        self.labelHeader_FNameandLnameDynamic.setText(_translate("AdminPanel", "{Fname and Lname}"))
        self.btnUserList_OpenClient.setText(_translate("AdminPanel", "Open Client"))
        self.btnUserLIst_ChangePassword.setText(_translate("AdminPanel", "Change Password"))
        self.btnUserList_ChangeUsername.setText(_translate("AdminPanel", "Change Username"))
        self.btnUserList_MakeAdmin.setText(_translate("AdminPanel", "Make Admin"))
        self.btnUserList_DeleteUser.setText(_translate("AdminPanel", "Delete User"))
        self.tableUserList.setSortingEnabled(False)
        item = self.tableUserList.horizontalHeaderItem(0)
        item.setText(_translate("AdminPanel", "User ID"))
        item = self.tableUserList.horizontalHeaderItem(1)
        item.setText(_translate("AdminPanel", "Username"))
        item = self.tableUserList.horizontalHeaderItem(2)
        item.setText(_translate("AdminPanel", "First Name"))
        item = self.tableUserList.horizontalHeaderItem(3)
        item.setText(_translate("AdminPanel", "Last Name"))
        item = self.tableUserList.horizontalHeaderItem(4)
        item.setText(_translate("AdminPanel", "User Type"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUserList), _translate("AdminPanel", "User List"))
        self.labelMonthlyEnergyConsumptionStatistics.setText(_translate("AdminPanel", "Monthly Energy Consumption Statistics"))
        self.labelMonthlyEnergyConsumptionStatistics_MeterType.setText(_translate("AdminPanel", "Meter Type"))
        self.labelMonthlyEnergyConsumptionStatistics_Month.setText(_translate("AdminPanel", "Month"))
        self.labelMonthlyEnergyConsumptionStatistics_GraphType.setText(_translate("AdminPanel", "Graph Type"))
        self.comboMonthlyEnergyConsumptionStatistics_GraphType.setItemText(0, _translate("AdminPanel", "Bar Graph"))
        self.comboMonthlyEnergyConsumptionStatistics_GraphType.setItemText(1, _translate("AdminPanel", "Pie Chart"))
        self.labelTotalEnergyConsumptionStatistics.setText(_translate("AdminPanel", "Total Energy Consumption Statistics"))
        self.labelTotalEnergyConsumptionStatistics_MeterType.setText(_translate("AdminPanel", "Meter Type"))
        self.labelTotalEnergyConsumptionStatistics_GraphType.setText(_translate("AdminPanel", "Graph Type"))
        self.comboTotalEnergyConsumptionStatistics_GraphType.setItemText(0, _translate("AdminPanel", "Bar Graph"))
        self.comboTotalEnergyConsumptionStatistics_GraphType.setItemText(1, _translate("AdminPanel", "Pie Chart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatistics), _translate("AdminPanel", "Statistics"))
