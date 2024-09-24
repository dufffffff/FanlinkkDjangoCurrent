# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'icon_menupcqYsk.ui'
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

class Ui_IconMenu(object):
    def setupUi(self, IconMenu):
        if not IconMenu.objectName():
            IconMenu.setObjectName(u"IconMenu")
        IconMenu.setWindowModality(Qt.WindowModality.WindowModal)
        IconMenu.resize(40, 450)
        IconMenu.setMinimumSize(QSize(50, 450))
        IconMenu.setMaximumSize(QSize(50, 1200))
        IconMenu.setStyleSheet(u"background-color:#0A0A0A;")
        self.verticalLayout_3 = QVBoxLayout(IconMenu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8,6,0,8)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.FLICON = QLabel(IconMenu)
        self.FLICON.setObjectName(u"FLICON")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FLICON.sizePolicy().hasHeightForWidth())
        self.FLICON.setSizePolicy(sizePolicy)
        self.FLICON.setMaximumSize(QSize(40, 40))
        self.FLICON.setStyleSheet(u"")
        self.FLICON.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.FLICON.setTextFormat(Qt.TextFormat.MarkdownText)
        self.FLICON.setPixmap(QPixmap(u":/Icons/Icons/FL.ico"))
        self.FLICON.setScaledContents(True)
        self.FLICON.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FLICON.setWordWrap(False)
        self.FLICON.setMargin(0)
        self.FLICON.setIndent(0)
    

        self.verticalLayout_2.addWidget(self.FLICON)

        self.verticalSpacer_2 = QSpacerItem(13, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DAICON = QPushButton(IconMenu)
        self.DAICON.setObjectName(u"DAICON")
        self.DAICON.setMinimumSize(QSize(42, 42))
        self.DAICON.setMaximumSize(QSize(48, 48))
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/dashboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Icons/Icons/dashboard (5).svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon.addFile(u":/Icons/Icons/dashboard (4).svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.DAICON.setIcon(icon)
        self.DAICON.setIconSize(QSize(38, 38))
        self.DAICON.setCheckable(True)
        self.DAICON.setAutoRepeat(False)
        self.DAICON.setAutoExclusive(True)
        self.DAICON.setFlat(True)

        self.verticalLayout.addWidget(self.DAICON)

        self.ANIcon = QPushButton(IconMenu)
        self.ANIcon.setObjectName(u"ANIcon")
        self.ANIcon.setMinimumSize(QSize(42, 42))
        self.ANIcon.setMaximumSize(QSize(48, 48))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/bar-chart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Icons/bar-chart (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon1.addFile(u":/Icons/Icons/bar-chart (1).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon1.addFile(u":/Icons/Icons/bar-chart (1).svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.ANIcon.setIcon(icon1)
        self.ANIcon.setIconSize(QSize(38, 38))
        self.ANIcon.setCheckable(True)
        self.ANIcon.setAutoExclusive(True)
        self.ANIcon.setFlat(True)

        self.verticalLayout.addWidget(self.ANIcon)

        self.FSIcon = QPushButton(IconMenu)
        self.FSIcon.setObjectName(u"FSIcon")
        self.FSIcon.setMinimumSize(QSize(42, 42))
        self.FSIcon.setMaximumSize(QSize(48, 48))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/FanService (3).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Icons/FanService (2).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon2.addFile(u":/Icons/Icons/FanService (2).svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.FSIcon.setIcon(icon2)
        self.FSIcon.setIconSize(QSize(38, 38))
        self.FSIcon.setCheckable(True)
        self.FSIcon.setAutoExclusive(True)
        self.FSIcon.setFlat(True)

        self.verticalLayout.addWidget(self.FSIcon)

        self.CEIcon = QPushButton(IconMenu)
        self.CEIcon.setObjectName(u"CEIcon")
        self.CEIcon.setMinimumSize(QSize(42, 42))
        self.CEIcon.setMaximumSize(QSize(48, 48))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Icons/user (2).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon3.addFile(u":/Icons/Icons/user (2).svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.CEIcon.setIcon(icon3)
        self.CEIcon.setIconSize(QSize(38, 38))
        self.CEIcon.setCheckable(True)
        self.CEIcon.setAutoExclusive(True)
        self.CEIcon.setFlat(True)

        self.verticalLayout.addWidget(self.CEIcon)

        self.TEICon = QPushButton(IconMenu)
        self.TEICon.setObjectName(u"TEICon")
        self.TEICon.setMinimumSize(QSize(42, 42))
        self.TEICon.setMaximumSize(QSize(48, 48))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/team.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/Icons/team (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon4.addFile(u":/Icons/Icons/team (1).svg", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon4.addFile(u":/Icons/Icons/team (1).svg", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon4.addFile(u":/Icons/Icons/team (1).svg", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon4.addFile(u":/Icons/Icons/team (2).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon4.addFile(u":/Icons/Icons/team (1).svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon4.addFile(u":/Icons/Icons/team (2).svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.TEICon.setIcon(icon4)
        self.TEICon.setIconSize(QSize(38, 38))
        self.TEICon.setCheckable(True)
        self.TEICon.setAutoExclusive(True)
        self.TEICon.setFlat(True)

        self.verticalLayout.addWidget(self.TEICon)

        self.SEICON = QPushButton(IconMenu)
        self.SEICON.setObjectName(u"SEICON")
        self.SEICON.setMinimumSize(QSize(42, 42))
        self.SEICON.setMaximumSize(QSize(48, 48))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/setting-lines.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/Icons/setting-lines (1).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon5.addFile(u":/Icons/Icons/setting-lines (1).svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.SEICON.setIcon(icon5)
        self.SEICON.setIconSize(QSize(38, 38))
        self.SEICON.setCheckable(True)
        self.SEICON.setAutoExclusive(True)
        self.SEICON.setFlat(True)

        self.verticalLayout.addWidget(self.SEICON)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(IconMenu)

        QMetaObject.connectSlotsByName(IconMenu)
    # setupUi

    def retranslateUi(self, IconMenu):
        self.FLICON.setText("")
        self.DAICON.setText("")
        self.ANIcon.setText("")
        self.FSIcon.setText("")
        self.CEIcon.setText("")
        self.TEICon.setText("")
        self.SEICON.setText("")
        pass
    # retranslateUi




# Wrapper class that uses the generated UI
class IconMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_IconMenu()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI in this QWidget
        with open("styles.qss", "r") as style_file:
                style_str = style_file.read()
        self.setStyleSheet(style_str)

