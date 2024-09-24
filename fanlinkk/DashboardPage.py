

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardfVIxsf.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1007, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setStyleSheet(u"background-color:#141414")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0,14,18,0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(208, 39, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.DashaboardLabel = QLabel(Form)
        self.DashaboardLabel.setObjectName(u"DashaboardLabel")
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(24)
        font.setBold(True)
        self.DashaboardLabel.setFont(font)
        self.DashaboardLabel.setStyleSheet(u"color:#f5f5f5;\n"
"background-color:#141414\n"
"")

        self.horizontalLayout_2.addWidget(self.DashaboardLabel)

        self.horizontalSpacer_4 = QSpacerItem(208, 39, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(24)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0,12,0,20)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(280, 260))
        self.frame.setMaximumSize(QSize(300, 280))
        self.frame.setStyleSheet(u"    border-radius: 36px; \n"
"    background-color: #373737;\n"
"    color: #ffffff; \n"
"    padding: 6px; ")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SalesBreakDownLabel = QLabel(self.frame)
        self.SalesBreakDownLabel.setObjectName(u"SalesBreakDownLabel")
        self.SalesBreakDownLabel.setMaximumSize(QSize(330, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(16)
        self.SalesBreakDownLabel.setFont(font1)
        self.SalesBreakDownLabel.setStyleSheet(u"")
        self.SalesBreakDownLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.SalesBreakDownLabel)

        self.verticalSpacer_2 = QSpacerItem(17, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(19)
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(120, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 80))
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setBold(False)
        self.frame_10.setFont(font2)
        self.frame_10.setStyleSheet(u"background-color:#ffffff;\n"
"    border-radius: 24px; \n"
"    color: white; \n"
"    padding: 3px; ")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.TotalLabelDash = QLabel(self.frame_10)
        self.TotalLabelDash.setObjectName(u"TotalLabelDash")
        self.TotalLabelDash.setMaximumSize(QSize(103, 16777215))
        self.TotalLabelDash.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Futura PT"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.TotalLabelDash.setFont(font3)
        self.TotalLabelDash.setStyleSheet(u"color: #000000 ;\n"
"background-color: none")
        self.TotalLabelDash.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TotalLabelDash.setMargin(6)

        self.verticalLayout_9.addWidget(self.TotalLabelDash, 0, Qt.AlignmentFlag.AlignHCenter)

        self.TotalDollarDash = QLabel(self.frame_10)
        self.TotalDollarDash.setObjectName(u"TotalDollarDash")
        self.TotalDollarDash.setMaximumSize(QSize(103, 16777215))
        self.TotalDollarDash.setFont(font3)
        self.TotalDollarDash.setStyleSheet(u"color: #000000 ;\n"
"background-color: none")
        self.TotalDollarDash.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.TotalDollarDash, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(120, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 80))
        self.frame_11.setFont(font2)
        self.frame_11.setStyleSheet(u"background-color:#ffffff;\n"
"    border-radius: 24px; \n"
"    color: white; \n"
"    padding: 3px; ")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.SubscribersLabelDash = QLabel(self.frame_11)
        self.SubscribersLabelDash.setObjectName(u"SubscribersLabelDash")
        self.SubscribersLabelDash.setMaximumSize(QSize(103, 16777215))
        self.SubscribersLabelDash.setSizeIncrement(QSize(0, 0))
        self.SubscribersLabelDash.setFont(font3)
        self.SubscribersLabelDash.setStyleSheet(u"color:#000000;\n"
"background-color: none")
        self.SubscribersLabelDash.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SubscribersLabelDash.setMargin(6)

        self.verticalLayout_10.addWidget(self.SubscribersLabelDash, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.SubscribersDollarDash = QLabel(self.frame_11)
        self.SubscribersDollarDash.setObjectName(u"SubscribersDollarDash")
        self.SubscribersDollarDash.setMaximumSize(QSize(103, 16777215))
        self.SubscribersDollarDash.setFont(font3)
        self.SubscribersDollarDash.setStyleSheet(u"color: #000000 ;\n"
"background-color: none")
        self.SubscribersDollarDash.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.SubscribersDollarDash, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_11, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(120, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setFont(font2)
        self.frame_12.setStyleSheet(u"background-color:#ffffff;\n"
"    border-radius: 24px; \n"
"    color: white; \n"
"    padding: 3px; ")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.TipsLabelDash = QLabel(self.frame_12)
        self.TipsLabelDash.setObjectName(u"TipsLabelDash")
        self.TipsLabelDash.setMaximumSize(QSize(103, 16777215))
        self.TipsLabelDash.setSizeIncrement(QSize(0, 0))
        self.TipsLabelDash.setFont(font3)
        self.TipsLabelDash.setStyleSheet(u"color: #000000 ;\n"
"background-color: none")
        self.TipsLabelDash.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TipsLabelDash.setMargin(6)

        self.verticalLayout_16.addWidget(self.TipsLabelDash, 0, Qt.AlignmentFlag.AlignHCenter)

        self.TipsDollarDash = QLabel(self.frame_12)
        self.TipsDollarDash.setObjectName(u"TipsDollarDash")
        self.TipsDollarDash.setMaximumSize(QSize(103, 16777215))
        self.TipsDollarDash.setFont(font3)
        self.TipsDollarDash.setStyleSheet(u"color: #000000 ;\n"
"background-color: none")
        self.TipsDollarDash.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.TipsDollarDash, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.frame_12, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(120, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 80))
        self.frame_13.setFont(font2)
        self.frame_13.setStyleSheet(u"background-color:#ffffff;\n"
"    border-radius: 24px; \n"
"    color: white; \n"
"    padding: 2px; ")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.PurchasesLabelDash = QLabel(self.frame_13)
        self.PurchasesLabelDash.setObjectName(u"PurchasesLabelDash")
        self.PurchasesLabelDash.setMaximumSize(QSize(103, 16777215))
        self.PurchasesLabelDash.setSizeIncrement(QSize(0, 0))
        self.PurchasesLabelDash.setFont(font3)
        self.PurchasesLabelDash.setStyleSheet(u"color: #000000 ;\n"
"background-color: none")
        self.PurchasesLabelDash.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PurchasesLabelDash.setMargin(6)

        self.verticalLayout_17.addWidget(self.PurchasesLabelDash, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.PurchasesDollarDash = QLabel(self.frame_13)
        self.PurchasesDollarDash.setObjectName(u"PurchasesDollarDash")
        self.PurchasesDollarDash.setMaximumSize(QSize(103, 16777215))
        self.PurchasesDollarDash.setFont(font3)
        self.PurchasesDollarDash.setStyleSheet(u"color: #000000 ;\n"
"background-color: none")
        self.PurchasesDollarDash.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.PurchasesDollarDash, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.frame_13, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_7 = QFrame(Form)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(285, 260))
        self.frame_7.setMaximumSize(QSize(330, 280))
        font4 = QFont()
        font4.setFamilies([u"Futura PT"])
        self.frame_7.setFont(font4)
        self.frame_7.setStyleSheet(u"    border-radius: 36px; \n"
"    background-color: #373737;\n"
"    color: #ffffff; \n"
"    padding: 6px; ")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ModelsLabel = QLabel(self.frame_7)
        self.ModelsLabel.setObjectName(u"ModelsLabel")
        font5 = QFont()
        font5.setFamilies([u"Futura PT"])
        font5.setPointSize(16)
        font5.setBold(False)
        self.ModelsLabel.setFont(font5)
        self.ModelsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.ModelsLabel)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(32)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.Model_1Pic = QLabel(self.frame_7)
        self.Model_1Pic.setObjectName(u"Model_1Pic")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Model_1Pic.sizePolicy().hasHeightForWidth())
        self.Model_1Pic.setSizePolicy(sizePolicy1)
        self.Model_1Pic.setMinimumSize(QSize(0, 0))
        self.Model_1Pic.setMaximumSize(QSize(48, 48))
        self.Model_1Pic.setLineWidth(0)
        self.Model_1Pic.setPixmap(QPixmap(u":/Icons/Icons/group (1).svg"))
        self.Model_1Pic.setScaledContents(True)
        self.Model_1Pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Model_1Pic.setIndent(0)

        self.horizontalLayout_6.addWidget(self.Model_1Pic)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_16)

        self.MBoxone = QCheckBox(self.frame_7)
        self.MBoxone.setObjectName(u"MBoxone")

        self.horizontalLayout_5.addWidget(self.MBoxone)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.Modle_2Pic = QLabel(self.frame_7)
        self.Modle_2Pic.setObjectName(u"Modle_2Pic")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Modle_2Pic.sizePolicy().hasHeightForWidth())
        self.Modle_2Pic.setSizePolicy(sizePolicy2)
        self.Modle_2Pic.setMinimumSize(QSize(0, 0))
        self.Modle_2Pic.setMaximumSize(QSize(48, 48))
        self.Modle_2Pic.setLineWidth(0)
        self.Modle_2Pic.setPixmap(QPixmap(u":/Icons/Icons/group (1).svg"))
        self.Modle_2Pic.setScaledContents(True)
        self.Modle_2Pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Modle_2Pic.setIndent(0)

        self.horizontalLayout.addWidget(self.Modle_2Pic)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.MBoxtwo = QCheckBox(self.frame_7)
        self.MBoxtwo.setObjectName(u"MBoxtwo")

        self.horizontalLayout_3.addWidget(self.MBoxtwo)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_18)

        self.Model_3Pic = QLabel(self.frame_7)
        self.Model_3Pic.setObjectName(u"Model_3Pic")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Model_3Pic.sizePolicy().hasHeightForWidth())
        self.Model_3Pic.setSizePolicy(sizePolicy3)
        self.Model_3Pic.setMinimumSize(QSize(0, 0))
        self.Model_3Pic.setMaximumSize(QSize(48, 48))
        self.Model_3Pic.setLineWidth(0)
        self.Model_3Pic.setPixmap(QPixmap(u":/Icons/Icons/group (1).svg"))
        self.Model_3Pic.setScaledContents(True)
        self.Model_3Pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Model_3Pic.setIndent(0)

        self.horizontalLayout_7.addWidget(self.Model_3Pic)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_20)

        self.MBoxthree = QCheckBox(self.frame_7)
        self.MBoxthree.setObjectName(u"MBoxthree")

        self.horizontalLayout_8.addWidget(self.MBoxthree)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_19)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 1, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_22)

        self.Model_4Pic = QLabel(self.frame_7)
        self.Model_4Pic.setObjectName(u"Model_4Pic")
        sizePolicy2.setHeightForWidth(self.Model_4Pic.sizePolicy().hasHeightForWidth())
        self.Model_4Pic.setSizePolicy(sizePolicy2)
        self.Model_4Pic.setMinimumSize(QSize(0, 0))
        self.Model_4Pic.setMaximumSize(QSize(48, 48))
        self.Model_4Pic.setLineWidth(0)
        self.Model_4Pic.setPixmap(QPixmap(u":/Icons/Icons/group (1).svg"))
        self.Model_4Pic.setScaledContents(True)
        self.Model_4Pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Model_4Pic.setIndent(0)

        self.horizontalLayout_10.addWidget(self.Model_4Pic)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_21)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_23)

        self.MBoxfour = QCheckBox(self.frame_7)
        self.MBoxfour.setObjectName(u"MBoxfour")

        self.horizontalLayout_9.addWidget(self.MBoxfour)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_24)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 1, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.verticalLayout_14.setStretch(2, 9)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(280, 260))
        self.frame_2.setMaximumSize(QSize(330, 280))
        self.frame_2.setStyleSheet(u"    border-radius: 36px; \n"
"    background-color: #373737;\n"
"    color: #ffffff; \n"
"    padding: 6px; ")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.DateLabel = QLabel(self.frame_2)
        self.DateLabel.setObjectName(u"DateLabel")
        self.DateLabel.setMaximumSize(QSize(297, 31))
        self.DateLabel.setFont(font1)
        self.DateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.DateLabel)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DateTodayButton = QPushButton(self.frame_2)
        self.DateTodayButton.setObjectName(u"DateTodayButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.DateTodayButton.sizePolicy().hasHeightForWidth())
        self.DateTodayButton.setSizePolicy(sizePolicy4)
        self.DateTodayButton.setMinimumSize(QSize(75, 40))
        font6 = QFont()
        font6.setFamilies([u"Futura PT"])
        font6.setPointSize(13)
        self.DateTodayButton.setFont(font6)
        self.DateTodayButton.setStyleSheet(u"    border-radius: 20px; \n"
"    background-color: #ffffff; \n"
"    color: #373737; \n"
"    padding: 9px; ")
        self.DateTodayButton.setCheckable(True)
        self.DateTodayButton.setAutoExclusive(True)
        self.DateTodayButton.setFlat(True)

        self.verticalLayout.addWidget(self.DateTodayButton)

        self.DateYesterdayButton = QPushButton(self.frame_2)
        self.DateYesterdayButton.setObjectName(u"DateYesterdayButton")
        self.DateYesterdayButton.setMinimumSize(QSize(75, 40))
        self.DateYesterdayButton.setFont(font1)
        self.DateYesterdayButton.setStyleSheet(u"    border-radius: 20px; \n"
"    background-color: #ffffff; \n"
"    color: #373737; \n"
"    padding: 9px; ")
        self.DateYesterdayButton.setCheckable(True)
        self.DateYesterdayButton.setAutoExclusive(True)
        self.DateYesterdayButton.setFlat(True)

        self.verticalLayout.addWidget(self.DateYesterdayButton)

        self.DateWeekButton = QPushButton(self.frame_2)
        self.DateWeekButton.setObjectName(u"DateWeekButton")
        self.DateWeekButton.setMinimumSize(QSize(75, 40))
        self.DateWeekButton.setFont(font1)
        self.DateWeekButton.setStyleSheet(u"    border-radius: 20px; \n"
"    background-color: #ffffff; \n"
"    color: #373737; \n"
"    padding: 9px; ")
        self.DateWeekButton.setCheckable(True)
        self.DateWeekButton.setAutoExclusive(True)
        self.DateWeekButton.setFlat(True)

        self.verticalLayout.addWidget(self.DateWeekButton)

        self.DateMonthButton = QPushButton(self.frame_2)
        self.DateMonthButton.setObjectName(u"DateMonthButton")
        self.DateMonthButton.setMinimumSize(QSize(75, 40))
        self.DateMonthButton.setFont(font1)
        self.DateMonthButton.setStyleSheet(u"    border-radius: 20px; \n"
"    background-color: #ffffff; \n"
"    color: #373737; \n"
"    padding: 9px; ")
        self.DateMonthButton.setCheckable(True)
        self.DateMonthButton.setAutoExclusive(True)
        self.DateMonthButton.setFlat(True)

        self.verticalLayout.addWidget(self.DateMonthButton)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_6.setStretch(1, 9)

        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.SalesGraphDashboard = QWidget(Form)
        self.SalesGraphDashboard.setObjectName(u"SalesGraphDashboard")
        self.SalesGraphDashboard.setMinimumSize(QSize(0, 300))
        self.SalesGraphDashboard.setStyleSheet(u"    border-radius: 48px; \n"
"    background-color: #141414;\n"
"    color: #ffffff; \n"
"    padding: 24px; ")

        self.verticalLayout_3.addWidget(self.SalesGraphDashboard)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.DashaboardLabel.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.SalesBreakDownLabel.setText(QCoreApplication.translate("Form", u"Sales Breakdown", None))
        self.TotalLabelDash.setText(QCoreApplication.translate("Form", u"Total", None))
        self.TotalDollarDash.setText(QCoreApplication.translate("Form", u"$0.00", None))
        self.SubscribersLabelDash.setText(QCoreApplication.translate("Form", u"Subs", None))
        self.SubscribersDollarDash.setText(QCoreApplication.translate("Form", u"$0.00", None))
        self.TipsLabelDash.setText(QCoreApplication.translate("Form", u"Tips", None))
        self.TipsDollarDash.setText(QCoreApplication.translate("Form", u"$0.00", None))
        self.PurchasesLabelDash.setText(QCoreApplication.translate("Form", u"Purschases", None))
        self.PurchasesDollarDash.setText(QCoreApplication.translate("Form", u"$0.00", None))
        self.ModelsLabel.setText(QCoreApplication.translate("Form", u"Models", None))
        self.Model_1Pic.setText("")
        self.MBoxone.setText(QCoreApplication.translate("Form", u"MBoxone", None))
        self.Modle_2Pic.setText("")
        self.MBoxtwo.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.Model_3Pic.setText("")
        self.MBoxthree.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.Model_4Pic.setText("")
        self.MBoxfour.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.DateLabel.setText(QCoreApplication.translate("Form", u"Date Filter", None))
        self.DateTodayButton.setText(QCoreApplication.translate("Form", u"Today", None))
        self.DateYesterdayButton.setText(QCoreApplication.translate("Form", u"Yesterday", None))
        self.DateWeekButton.setText(QCoreApplication.translate("Form", u"Last 7 Days", None))
        self.DateMonthButton.setText(QCoreApplication.translate("Form", u"Last Month", None))
    # retranslateUi



style_sheet_date_buttons = """
QPushButton#DateTodayButton, QPushButton#DateYesterdayButton, QPushButton#DateWeekButton, QPushButton#DateMonthButton {
    background-color: #ffffff;
    color: #373737;
    border-radius: 20px;
    padding: 9px;
    font-family: 'Futura PT';
    font-size: 13pt;
}

QPushButton#DateTodayButton:hover, QPushButton#DateYesterdayButton:hover, QPushButton#DateWeekButton:hover, 
QPushButton#DateMonthButton:hover {
    background-color: #141414;
    color: white;
}

QPushButton#DateTodayButton:checked, QPushButton#DateYesterdayButton:checked, QPushButton#DateWeekButton:checked, 
QPushButton#DateMonthButton:checked {
    background-color: #ef910d;
    color: white;
}
"""




class DashboardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.DateTodayButton.setStyleSheet(style_sheet_date_buttons)
        self.ui.DateYesterdayButton.setStyleSheet(style_sheet_date_buttons)
        self.ui.DateWeekButton.setStyleSheet(style_sheet_date_buttons)
        self.ui.DateMonthButton.setStyleSheet(style_sheet_date_buttons)
        self.ui.MBoxone.setStyleSheet("""
            QCheckBox::indicator {
                background-color: #373737;
                border: 1px solid #373737;
                width: 0px;
                height: 0px;
            }
            QCheckBox {
                color: white;
                padding-left: 0px;  /* Remove extra left padding */
            }
            QCheckBox:checked {
                color: #EF910D;
            }
        """)

        self.ui.MBoxtwo.setStyleSheet("""
                QCheckBox::indicator {
                    background-color: #373737;
                    border: 1px solid #373737;
                    width: 0px;
                    height: 0px;
                }
                QCheckBox {
                    color: white;
                    padding-left: 0px;  /* Remove extra left padding */
                }
                QCheckBox:checked {
                    color: #EF910D;
                }
            """)

        self.ui.MBoxthree.setStyleSheet("""
                QCheckBox::indicator {
                    background-color: #373737;
                    border: 1px solid #373737;
                    width: 0px;
                    height: 0px;
                }
                QCheckBox {
                    color: white;
                    padding-left: 0px;  /* Remove extra left padding */
                }
                QCheckBox:checked {
                    color: #EF910D;
                }
            """)

        self.ui.MBoxfour.setStyleSheet("""
                QCheckBox::indicator {
                    background-color: #373737;
                    border: 1px solid #373737;
                    width: 0px;
                    height: 0px;
                }
                QCheckBox {
                    color: white;
                    padding-left: 0px;  /* Remove extra left padding */
                }
                QCheckBox:checked {
                    color: #EF910D;
                }
            """)
        


