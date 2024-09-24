# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'full menue newOQPyLW.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(180, 1250)
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.FLMANLOGO = QLabel(Form)
        self.FLMANLOGO.setObjectName(u"FLMANLOGO")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FLMANLOGO.sizePolicy().hasHeightForWidth())
        self.FLMANLOGO.setSizePolicy(sizePolicy)
        self.FLMANLOGO.setMaximumSize(QSize(180, 42))
        self.FLMANLOGO.setPixmap(QPixmap(u":/Icons/Icons/Asset 1 (1).svg"))
        self.FLMANLOGO.setScaledContents(True)
        self.FLMANLOGO.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FLMANLOGO.setIndent(0)

        self.verticalLayout_3.addWidget(self.FLMANLOGO)
        self.verticalLayout_3.setContentsMargins(4,0,4,0)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 15, 0, 0)
        self.DAMain = QPushButton(Form)
        self.DAMain.setObjectName(u"DAMain")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.DAMain.sizePolicy().hasHeightForWidth())
        self.DAMain.setSizePolicy(sizePolicy1)
        self.DAMain.setMinimumSize(QSize(80, 45))
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(13)
        font.setBold(False)
        self.DAMain.setFont(font)
        self.DAMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.DAMain.setAutoFillBackground(False)
  

        icon = QIcon()
        icon.addFile(u":/Icons/Icons/speedometer (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DAMain.setIcon(icon)
        self.DAMain.setIconSize(QSize(23, 23))
        self.DAMain.setCheckable(True)
        self.DAMain.setAutoExclusive(True)
        self.DAMain.setAutoRepeatInterval(97)
        self.DAMain.setFlat(False)

        self.verticalLayout.addWidget(self.DAMain)

        self.TEMain = QPushButton(Form)
        self.TEMain.setObjectName(u"TEMain")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TEMain.sizePolicy().hasHeightForWidth())
        self.TEMain.setSizePolicy(sizePolicy2)
        self.TEMain.setMinimumSize(QSize(80, 45))
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(13)
        self.TEMain.setFont(font1)
        self.TEMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/group (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TEMain.setIcon(icon1)
        self.TEMain.setIconSize(QSize(23, 23))
        self.TEMain.setCheckable(True)
        self.TEMain.setAutoExclusive(True)
        self.TEMain.setFlat(True)

        self.verticalLayout.addWidget(self.TEMain)

        self.ANMain = QPushButton(Form)
        self.ANMain.setObjectName(u"ANMain")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ANMain.sizePolicy().hasHeightForWidth())
        self.ANMain.setSizePolicy(sizePolicy3)
        self.ANMain.setMinimumSize(QSize(80, 45))
        self.ANMain.setFont(font1)
        self.ANMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ANMain.setAutoFillBackground(False)
 
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/bar-chart (3).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ANMain.setIcon(icon2)
        self.ANMain.setIconSize(QSize(24, 23))
        self.ANMain.setCheckable(True)
        self.ANMain.setAutoExclusive(True)
        self.ANMain.setFlat(True)

        self.verticalLayout.addWidget(self.ANMain)

        self.CEMain = QPushButton(Form)
        self.CEMain.setObjectName(u"CEMain")
        sizePolicy2.setHeightForWidth(self.CEMain.sizePolicy().hasHeightForWidth())
        self.CEMain.setSizePolicy(sizePolicy2)
        self.CEMain.setMinimumSize(QSize(80, 45))
        self.CEMain.setFont(font1)
        self.CEMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.CEMain.setIcon(icon1)
        self.CEMain.setIconSize(QSize(23, 23))
        self.CEMain.setCheckable(True)
        self.CEMain.setAutoExclusive(True)
        self.CEMain.setFlat(True)

        self.verticalLayout.addWidget(self.CEMain)

        self.SEMain = QPushButton(Form)
        self.SEMain.setObjectName(u"SEMain")
        sizePolicy3.setHeightForWidth(self.SEMain.sizePolicy().hasHeightForWidth())
        self.SEMain.setSizePolicy(sizePolicy3)
        self.SEMain.setMinimumSize(QSize(80, 45))
        self.SEMain.setFont(font1)
        self.SEMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SEMain.setIcon(icon3)
        self.SEMain.setIconSize(QSize(23, 23))
        self.SEMain.setCheckable(True)
        self.SEMain.setAutoExclusive(True)
        self.SEMain.setFlat(True)

        self.verticalLayout.addWidget(self.SEMain)

        self.FSMain = QPushButton(Form)
        self.FSMain.setObjectName(u"FSMain")
        sizePolicy3.setHeightForWidth(self.FSMain.sizePolicy().hasHeightForWidth())
        self.FSMain.setSizePolicy(sizePolicy3)
        self.FSMain.setMinimumSize(QSize(80, 45))
        self.FSMain.setFont(font1)
        self.FSMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/chat-bubble (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.FSMain.setIcon(icon4)
        self.FSMain.setIconSize(QSize(23, 23))
        self.FSMain.setCheckable(True)
        self.FSMain.setAutoExclusive(True)
        self.FSMain.setFlat(True)

        self.verticalLayout.addWidget(self.FSMain)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.HomeButton = QPushButton(Form)
        self.HomeButton.setObjectName(u"HomeButton")
        sizePolicy3.setHeightForWidth(self.HomeButton.sizePolicy().hasHeightForWidth())
        self.HomeButton.setSizePolicy(sizePolicy3)
        self.HomeButton.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setPointSize(12)
        self.HomeButton.setFont(font2)
        self.HomeButton.setStyleSheet(u"color: #ffffff")
        self.HomeButton.setCheckable(True)
        self.HomeButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.HomeButton)

        self.NewPostsButton = QPushButton(Form)
        self.NewPostsButton.setObjectName(u"NewPostsButton")
        sizePolicy3.setHeightForWidth(self.NewPostsButton.sizePolicy().hasHeightForWidth())
        self.NewPostsButton.setSizePolicy(sizePolicy3)
        self.NewPostsButton.setMinimumSize(QSize(0, 20))
        self.NewPostsButton.setFont(font2)
        self.NewPostsButton.setStyleSheet(u"color: #ffffff")
        self.NewPostsButton.setCheckable(True)
        self.NewPostsButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.NewPostsButton)

        self.VaultButton = QPushButton(Form)
        self.VaultButton.setObjectName(u"VaultButton")
        sizePolicy3.setHeightForWidth(self.VaultButton.sizePolicy().hasHeightForWidth())
        self.VaultButton.setSizePolicy(sizePolicy3)
        self.VaultButton.setMinimumSize(QSize(0, 20))
        self.VaultButton.setFont(font2)
        self.VaultButton.setStyleSheet(u"color: #ffffff")
        self.VaultButton.setCheckable(True)
        self.VaultButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.VaultButton)

        self.QueueButton = QPushButton(Form)
        self.QueueButton.setObjectName(u"QueueButton")
        sizePolicy3.setHeightForWidth(self.QueueButton.sizePolicy().hasHeightForWidth())
        self.QueueButton.setSizePolicy(sizePolicy3)
        self.QueueButton.setMinimumSize(QSize(0, 20))
        self.QueueButton.setFont(font2)
        self.QueueButton.setStyleSheet(u"color: #ffffff")
        self.QueueButton.setCheckable(True)
        self.QueueButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.QueueButton)

        self.NotificationsButton = QPushButton(Form)
        self.NotificationsButton.setObjectName(u"NotificationsButton")
        sizePolicy3.setHeightForWidth(self.NotificationsButton.sizePolicy().hasHeightForWidth())
        self.NotificationsButton.setSizePolicy(sizePolicy3)
        self.NotificationsButton.setMinimumSize(QSize(0, 20))
        self.NotificationsButton.setFont(font2)
        self.NotificationsButton.setStyleSheet(u"color: #ffffff")
        self.NotificationsButton.setCheckable(True)
        self.NotificationsButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.NotificationsButton)

        self.InsightsButton = QPushButton(Form)
        self.InsightsButton.setObjectName(u"InsightsButton")
        sizePolicy3.setHeightForWidth(self.InsightsButton.sizePolicy().hasHeightForWidth())
        self.InsightsButton.setSizePolicy(sizePolicy3)
        self.InsightsButton.setMinimumSize(QSize(0, 20))
        self.InsightsButton.setFont(font2)
        self.InsightsButton.setStyleSheet(u"color: #ffffff")
        self.InsightsButton.setCheckable(True)
        self.InsightsButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.InsightsButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        self.HomeButton.setDefault(False)
        self.NewPostsButton.setDefault(False)
        self.VaultButton.setDefault(False)
        self.QueueButton.setDefault(False)
        self.NotificationsButton.setDefault(False)
        self.InsightsButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.FLMANLOGO.setText("")
        self.DAMain.setText(QCoreApplication.translate("Form", u" Dashboard", None))
#if QT_CONFIG(shortcut)
        self.DAMain.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.TEMain.setText(QCoreApplication.translate("Form", u" Team", None))
        self.ANMain.setText(QCoreApplication.translate("Form", u" Analytics", None))
#if QT_CONFIG(shortcut)
        self.ANMain.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.CEMain.setText(QCoreApplication.translate("Form", u" Creators", None))
        self.SEMain.setText(QCoreApplication.translate("Form", u" Settings", None))
        self.FSMain.setText(QCoreApplication.translate("Form", u" Fan Service", None))
        self.HomeButton.setText(QCoreApplication.translate("Form", u"Home", None))
        self.NewPostsButton.setText(QCoreApplication.translate("Form", u"New Posts", None))
        self.VaultButton.setText(QCoreApplication.translate("Form", u"Vault", None))
        self.QueueButton.setText(QCoreApplication.translate("Form", u"Queue", None))
        self.NotificationsButton.setText(QCoreApplication.translate("Form", u"Notifications", None))
        self.InsightsButton.setText(QCoreApplication.translate("Form", u"Insights", None))
    # retranslateUi

style_sheet = """
QPushButton#DAMain, QPushButton#TEMain, QPushButton#ANMain, QPushButton#CEMain, 
QPushButton#SEMain, QPushButton#FSMain {
    background-color: #373737;
    color: white;
    border-radius: 15px;
    padding: 5px;  /* Adjust padding */
    font-family: 'Futura PT';
    font-size: 13pt;
    text-align: center;  /* Align text to the left */
}

QPushButton#DAMain:hover, QPushButton#TEMain:hover, QPushButton#ANMain:hover, QPushButton#CEMain:hover, 
QPushButton#SEMain:hover, QPushButton#FSMain:hover {
    background-color: white;
    color: #373737;
}

QPushButton#DAMain:checked, QPushButton#TEMain:checked, QPushButton#ANMain:checked, QPushButton#CEMain:checked, 
QPushButton#SEMain:checked, QPushButton#FSMain:checked {
    background-color: #ef910d;
    color: white;
}
"""




class MenuWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setStyleSheet(style_sheet)
 



