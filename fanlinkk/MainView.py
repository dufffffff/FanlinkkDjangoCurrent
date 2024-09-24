# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import Resources_rc
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
       # MainWindow.resize(1203, 400)
        
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#2a2a2a;")
        self.centralwidget.setContentsMargins(0,0,0,0)
        self.horizontalLayout_15 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 12, 0, 0)
        

        self.PageView = QStackedWidget(self.centralwidget)
        self.PageView.setObjectName(u"PageView")
        self.PageView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        font = QFont()
        font.setFamilies([u"Gill Sans MT"])
        font.setPointSize(14)
        self.PageView.setFont(font)
        self.PageView.setStyleSheet(u"background-color:#2a2a2a;")

        self.verticalLayout_47.addWidget(self.PageView)


        self.horizontalLayout_15.addLayout(self.verticalLayout_47)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.PageView.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi


class MainViewer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

