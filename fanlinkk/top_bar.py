# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'top_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Resources_rc

class Ui_TopBar(object):
    def setupUi(self, TopBar):
        if not TopBar.objectName():
            TopBar.setObjectName(u"TopBar")
        TopBar.resize(586, 48)
        TopBar.setMinimumSize(QSize(0, 20))
        TopBar.setMaximumSize(QSize(16777215, 50))
        TopBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        TopBar.setStyleSheet(u"background-color:#1f1f1f;")
        self.horizontalLayout = QHBoxLayout(TopBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 8, 0)
        self.SidebarExpand = QPushButton(TopBar)
        self.SidebarExpand.setObjectName(u"SidebarExpand")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SidebarExpand.sizePolicy().hasHeightForWidth())
        self.SidebarExpand.setSizePolicy(sizePolicy)
        self.SidebarExpand.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/hamburger.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SidebarExpand.setIcon(icon)
        self.SidebarExpand.setIconSize(QSize(28, 28))
        self.SidebarExpand.setCheckable(True)
        self.SidebarExpand.setAutoExclusive(False)
        self.SidebarExpand.setFlat(True)

        self.horizontalLayout.addWidget(self.SidebarExpand)

        self.horizontalSpacer = QSpacerItem(428, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PRTopBar = QPushButton(TopBar)
        self.PRTopBar.setObjectName(u"PRTopBar")
        self.PRTopBar.setMinimumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/user (3).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PRTopBar.setIcon(icon1)
        self.PRTopBar.setIconSize(QSize(32, 32))
        self.PRTopBar.setCheckable(True)
        self.PRTopBar.setAutoExclusive(True)
        self.PRTopBar.setFlat(True)

        self.horizontalLayout.addWidget(self.PRTopBar)

        self.NOTopBar = QPushButton(TopBar)
        self.NOTopBar.setObjectName(u"NOTopBar")
        self.NOTopBar.setMinimumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/notification.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.NOTopBar.setIcon(icon2)
        self.NOTopBar.setIconSize(QSize(32, 32))
        self.NOTopBar.setCheckable(True)
        self.NOTopBar.setAutoExclusive(True)
        self.NOTopBar.setFlat(True)

        self.horizontalLayout.addWidget(self.NOTopBar)


        self.retranslateUi(TopBar)

        QMetaObject.connectSlotsByName(TopBar)
    # setupUi

    def retranslateUi(self, TopBar):
        self.SidebarExpand.setText("")
        self.PRTopBar.setText("")
        self.NOTopBar.setText("")
        pass
    # retranslateUi



class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TopBar()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI in this QWidget
        with open("styles.qss", "r") as style_file:
                style_str = style_file.read()
        self.setStyleSheet(style_str)
