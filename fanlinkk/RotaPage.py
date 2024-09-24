# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RotaPage.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(708, 872)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.widget_9 = QWidget(Form)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_29 = QVBoxLayout(self.widget_9)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.RotaControlLabel = QLabel(self.widget_9)
        self.RotaControlLabel.setObjectName(u"RotaControlLabel")
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(24)
        self.RotaControlLabel.setFont(font)

        self.horizontalLayout_22.addWidget(self.RotaControlLabel)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_26)


        self.verticalLayout_29.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.AddshiftButton = QPushButton(self.widget_9)
        self.AddshiftButton.setObjectName(u"AddshiftButton")
        self.AddshiftButton.setMinimumSize(QSize(100, 42))
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.AddshiftButton.setFont(font1)
        self.AddshiftButton.setStyleSheet(u"background-color: 373737;\n"
"")
        self.AddshiftButton.setFlat(True)

        self.horizontalLayout_23.addWidget(self.AddshiftButton)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_27)


        self.verticalLayout_29.addLayout(self.horizontalLayout_23)

        self.verticalLayout_29.setStretch(1, 1)

        self.verticalLayout_31.addWidget(self.widget_9)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(5, 0))
        self.calendarWidget.setMaximumSize(QSize(841, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setPointSize(13)
        self.calendarWidget.setFont(font2)
        self.calendarWidget.setStyleSheet(u"")
        self.calendarWidget.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.calendarWidget.setSelectedDate(QDate(2024, 7, 19))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.LongDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)

        self.horizontalLayout_24.addWidget(self.calendarWidget)

        self.ShiftFrame = QFrame(Form)
        self.ShiftFrame.setObjectName(u"ShiftFrame")
        self.ShiftFrame.setMinimumSize(QSize(240, 0))
        self.ShiftFrame.setStyleSheet(u"background-color:#141414;\n"
"")
        self.ShiftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ShiftFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.ShiftFrame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.splitter = QSplitter(self.ShiftFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.label_41 = QLabel(self.splitter)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"background-color:#333333")
        self.splitter.addWidget(self.label_41)
        self.label_42 = QLabel(self.splitter)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"background-color:#333333")
        self.splitter.addWidget(self.label_42)
        self.label_43 = QLabel(self.splitter)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"background-color:#333333")
        self.splitter.addWidget(self.label_43)
        self.label_44 = QLabel(self.splitter)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"background-color:#333333")
        self.splitter.addWidget(self.label_44)

        self.verticalLayout_30.addWidget(self.splitter)


        self.horizontalLayout_24.addWidget(self.ShiftFrame)

        self.horizontalLayout_24.setStretch(0, 10)
        self.horizontalLayout_24.setStretch(1, 1)

        self.verticalLayout_31.addLayout(self.horizontalLayout_24)

        self.verticalLayout_31.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_31)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.RotaControlLabel.setText(QCoreApplication.translate("Form", u"Rota Control", None))
        self.AddshiftButton.setText(QCoreApplication.translate("Form", u"Add Shift", None))
        self.label_41.setText("")
        self.label_42.setText("")
        self.label_43.setText("")
        self.label_44.setText("")
    # retranslateUi

class Rota(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

