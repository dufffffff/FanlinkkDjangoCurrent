# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EmployeeReportsPage.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import Resources_rc
import Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(783, 898)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_3 = QScrollArea(Form)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        font = QFont()
        font.setFamilies([u"Gill Sans MT"])
        font.setPointSize(12)
        font.setBold(True)
        self.scrollArea_3.setFont(font)
        self.scrollArea_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setMidLineWidth(0)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 751, 878))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.EmployeeReportsLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.EmployeeReportsLabel.setObjectName(u"EmployeeReportsLabel")
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(24)
        font1.setBold(False)
        self.EmployeeReportsLabel.setFont(font1)
        self.EmployeeReportsLabel.setStyleSheet(u"color:#f5f5f5;")

        self.horizontalLayout_6.addWidget(self.EmployeeReportsLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.DayButtonER = QPushButton(self.scrollAreaWidgetContents_3)
        self.DayButtonER.setObjectName(u"DayButtonER")
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.DayButtonER.setFont(font2)
        self.DayButtonER.setStyleSheet(u"	color:#f5f5f5;\n"
"    ")
        self.DayButtonER.setCheckable(True)
        self.DayButtonER.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.DayButtonER)

        self.WeekButtonER = QPushButton(self.scrollAreaWidgetContents_3)
        self.WeekButtonER.setObjectName(u"WeekButtonER")
        self.WeekButtonER.setFont(font2)
        self.WeekButtonER.setStyleSheet(u"	color:#f5f5f5;\n"
"\n"
"")
        self.WeekButtonER.setCheckable(True)
        self.WeekButtonER.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.WeekButtonER)

        self.MonthButtonER = QPushButton(self.scrollAreaWidgetContents_3)
        self.MonthButtonER.setObjectName(u"MonthButtonER")
        self.MonthButtonER.setFont(font2)
        self.MonthButtonER.setStyleSheet(u"	color:#f5f5f5;\n"
"")
        self.MonthButtonER.setCheckable(True)
        self.MonthButtonER.setAutoExclusive(True)
        self.MonthButtonER.setFlat(False)

        self.horizontalLayout_19.addWidget(self.MonthButtonER)

        self.YearButtonER = QPushButton(self.scrollAreaWidgetContents_3)
        self.YearButtonER.setObjectName(u"YearButtonER")
        self.YearButtonER.setFont(font2)
        self.YearButtonER.setStyleSheet(u"	color:#f5f5f5;\n"
"")
        self.YearButtonER.setCheckable(True)
        self.YearButtonER.setAutoExclusive(True)

        self.horizontalLayout_19.addWidget(self.YearButtonER)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.SecondHoriLayout_2 = QHBoxLayout()
        self.SecondHoriLayout_2.setObjectName(u"SecondHoriLayout_2")
        self.ERSalesBreakdownWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.ERSalesBreakdownWidget.setObjectName(u"ERSalesBreakdownWidget")
        self.ERSalesBreakdownWidget.setMinimumSize(QSize(380, 0))
        self.ERSalesBreakdownWidget.setStyleSheet(u"")
        self.verticalLayout_46 = QVBoxLayout(self.ERSalesBreakdownWidget)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_60)

        self.ERSalesBreakdownLabel = QLabel(self.ERSalesBreakdownWidget)
        self.ERSalesBreakdownLabel.setObjectName(u"ERSalesBreakdownLabel")
        font3 = QFont()
        font3.setFamilies([u"Futura PT"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setKerning(True)
        self.ERSalesBreakdownLabel.setFont(font3)
        self.ERSalesBreakdownLabel.setStyleSheet(u"Color:#EBEBEB")

        self.horizontalLayout_47.addWidget(self.ERSalesBreakdownLabel)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_61)


        self.verticalLayout_46.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, -1, -1, -1)
        self.PostIconER = QLabel(self.ERSalesBreakdownWidget)
        self.PostIconER.setObjectName(u"PostIconER")
        self.PostIconER.setMaximumSize(QSize(24, 22))
        self.PostIconER.setStyleSheet(u"border: none;")
        self.PostIconER.setLineWidth(0)
        self.PostIconER.setTextFormat(Qt.TextFormat.AutoText)
        self.PostIconER.setPixmap(QPixmap(u":/Icons/Icons/paper-plane.svg"))
        self.PostIconER.setScaledContents(True)
        self.PostIconER.setWordWrap(False)
        self.PostIconER.setMargin(3)
        self.PostIconER.setIndent(19)

        self.horizontalLayout_27.addWidget(self.PostIconER)

        self.PostsLabelER = QLabel(self.ERSalesBreakdownWidget)
        self.PostsLabelER.setObjectName(u"PostsLabelER")
        self.PostsLabelER.setFont(font2)
        self.PostsLabelER.setStyleSheet(u"border:none;\n"
"border-left: 5px black;\n"
"")
        self.PostsLabelER.setFrameShape(QFrame.Shape.Box)
        self.PostsLabelER.setMidLineWidth(6)
        self.PostsLabelER.setScaledContents(False)
        self.PostsLabelER.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PostsLabelER.setMargin(6)

        self.horizontalLayout_27.addWidget(self.PostsLabelER)

        self.PostDollarER = QLabel(self.ERSalesBreakdownWidget)
        self.PostDollarER.setObjectName(u"PostDollarER")
        font4 = QFont()
        font4.setFamilies([u"Futura PT"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.PostDollarER.setFont(font4)
        self.PostDollarER.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_27.addWidget(self.PostDollarER)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_62)


        self.verticalLayout_46.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(3, -1, -1, -1)
        self.SubscribeIconER = QLabel(self.ERSalesBreakdownWidget)
        self.SubscribeIconER.setObjectName(u"SubscribeIconER")
        self.SubscribeIconER.setMaximumSize(QSize(24, 24))
        self.SubscribeIconER.setStyleSheet(u"border: none;")
        self.SubscribeIconER.setLineWidth(0)
        self.SubscribeIconER.setTextFormat(Qt.TextFormat.AutoText)
        self.SubscribeIconER.setPixmap(QPixmap(u":/Icons/Icons/recycle.svg"))
        self.SubscribeIconER.setScaledContents(True)
        self.SubscribeIconER.setWordWrap(False)
        self.SubscribeIconER.setMargin(0)
        self.SubscribeIconER.setIndent(19)

        self.horizontalLayout_28.addWidget(self.SubscribeIconER)

        self.SubscriptionsLabelER = QLabel(self.ERSalesBreakdownWidget)
        self.SubscriptionsLabelER.setObjectName(u"SubscriptionsLabelER")
        self.SubscriptionsLabelER.setFont(font2)
        self.SubscriptionsLabelER.setStyleSheet(u"")
        self.SubscriptionsLabelER.setMargin(6)

        self.horizontalLayout_28.addWidget(self.SubscriptionsLabelER)

        self.SubscribeDollarER = QLabel(self.ERSalesBreakdownWidget)
        self.SubscribeDollarER.setObjectName(u"SubscribeDollarER")
        self.SubscribeDollarER.setFont(font4)
        self.SubscribeDollarER.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_28.addWidget(self.SubscribeDollarER)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_63)


        self.verticalLayout_46.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(3, -1, -1, -1)
        self.MessagesIconER = QLabel(self.ERSalesBreakdownWidget)
        self.MessagesIconER.setObjectName(u"MessagesIconER")
        self.MessagesIconER.setMaximumSize(QSize(24, 22))
        self.MessagesIconER.setStyleSheet(u"border: none;\n"
"")
        self.MessagesIconER.setLineWidth(0)
        self.MessagesIconER.setTextFormat(Qt.TextFormat.AutoText)
        self.MessagesIconER.setPixmap(QPixmap(u":/Icons/Icons/email.svg"))
        self.MessagesIconER.setScaledContents(True)
        self.MessagesIconER.setWordWrap(False)
        self.MessagesIconER.setMargin(0)
        self.MessagesIconER.setIndent(19)

        self.horizontalLayout_29.addWidget(self.MessagesIconER)

        self.MessagesLabelER = QLabel(self.ERSalesBreakdownWidget)
        self.MessagesLabelER.setObjectName(u"MessagesLabelER")
        self.MessagesLabelER.setFont(font2)
        self.MessagesLabelER.setStyleSheet(u"")
        self.MessagesLabelER.setMargin(6)

        self.horizontalLayout_29.addWidget(self.MessagesLabelER)

        self.MessagesDollarER = QLabel(self.ERSalesBreakdownWidget)
        self.MessagesDollarER.setObjectName(u"MessagesDollarER")
        self.MessagesDollarER.setFont(font4)
        self.MessagesDollarER.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_29.addWidget(self.MessagesDollarER)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_64)


        self.verticalLayout_46.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(3, -1, -1, -1)
        self.ReferralsIconER = QLabel(self.ERSalesBreakdownWidget)
        self.ReferralsIconER.setObjectName(u"ReferralsIconER")
        self.ReferralsIconER.setMaximumSize(QSize(24, 22))
        self.ReferralsIconER.setStyleSheet(u"border: none;")
        self.ReferralsIconER.setLineWidth(0)
        self.ReferralsIconER.setTextFormat(Qt.TextFormat.AutoText)
        self.ReferralsIconER.setPixmap(QPixmap(u":/Icons/Icons/link.svg"))
        self.ReferralsIconER.setScaledContents(True)
        self.ReferralsIconER.setWordWrap(False)
        self.ReferralsIconER.setMargin(0)
        self.ReferralsIconER.setIndent(19)

        self.horizontalLayout_30.addWidget(self.ReferralsIconER)

        self.ReferralsLabelER = QLabel(self.ERSalesBreakdownWidget)
        self.ReferralsLabelER.setObjectName(u"ReferralsLabelER")
        self.ReferralsLabelER.setFont(font2)
        self.ReferralsLabelER.setStyleSheet(u"")
        self.ReferralsLabelER.setMargin(6)

        self.horizontalLayout_30.addWidget(self.ReferralsLabelER)

        self.ReferralDollarER = QLabel(self.ERSalesBreakdownWidget)
        self.ReferralDollarER.setObjectName(u"ReferralDollarER")
        self.ReferralDollarER.setFont(font4)
        self.ReferralDollarER.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_30.addWidget(self.ReferralDollarER)

        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_65)


        self.verticalLayout_46.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(3, -1, -1, -1)
        self.TipsIconsER = QLabel(self.ERSalesBreakdownWidget)
        self.TipsIconsER.setObjectName(u"TipsIconsER")
        self.TipsIconsER.setMaximumSize(QSize(24, 24))
        self.TipsIconsER.setStyleSheet(u"border: none;\n"
"")
        self.TipsIconsER.setLineWidth(0)
        self.TipsIconsER.setTextFormat(Qt.TextFormat.AutoText)
        self.TipsIconsER.setPixmap(QPixmap(u":/Icons/Icons/give-money.svg"))
        self.TipsIconsER.setScaledContents(True)
        self.TipsIconsER.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.TipsIconsER.setWordWrap(False)
        self.TipsIconsER.setMargin(0)
        self.TipsIconsER.setIndent(-1)

        self.horizontalLayout_31.addWidget(self.TipsIconsER)

        self.TipsLabelER = QLabel(self.ERSalesBreakdownWidget)
        self.TipsLabelER.setObjectName(u"TipsLabelER")
        self.TipsLabelER.setFont(font2)
        self.TipsLabelER.setStyleSheet(u"")
        self.TipsLabelER.setMargin(6)

        self.horizontalLayout_31.addWidget(self.TipsLabelER)

        self.TipsDollarER = QLabel(self.ERSalesBreakdownWidget)
        self.TipsDollarER.setObjectName(u"TipsDollarER")
        self.TipsDollarER.setFont(font4)
        self.TipsDollarER.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_31.addWidget(self.TipsDollarER)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_66)


        self.verticalLayout_46.addLayout(self.horizontalLayout_31)


        self.SecondHoriLayout_2.addWidget(self.ERSalesBreakdownWidget)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.ModalSelectorComboER = QComboBox(self.scrollAreaWidgetContents_3)
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ModalSelectorComboER.addItem(icon, "")
        self.ModalSelectorComboER.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/user (2).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ModalSelectorComboER.addItem(icon1, "")
        self.ModalSelectorComboER.setObjectName(u"ModalSelectorComboER")
        self.ModalSelectorComboER.setMinimumSize(QSize(345, 57))
        font5 = QFont()
        font5.setFamilies([u"Futura PT"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.ModalSelectorComboER.setFont(font5)
        self.ModalSelectorComboER.setStyleSheet(u"	color:#f6f6f8;\n"
"	border:none;")
        self.ModalSelectorComboER.setIconSize(QSize(32, 32))

        self.verticalLayout_35.addWidget(self.ModalSelectorComboER)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_12)


        self.SecondHoriLayout_2.addLayout(self.verticalLayout_35)

        self.SecondHoriLayout_2.setStretch(0, 1)
        self.SecondHoriLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.SecondHoriLayout_2)

        self.ContentWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.ContentWidget.setObjectName(u"ContentWidget")
        self.verticalLayout = QVBoxLayout(self.ContentWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.RevenueSummaryWidget = QVBoxLayout()
        self.RevenueSummaryWidget.setObjectName(u"RevenueSummaryWidget")
        self.RevenueSummaryWidget.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.RevenueSummaryLabel = QLabel(self.ContentWidget)
        self.RevenueSummaryLabel.setObjectName(u"RevenueSummaryLabel")
        self.RevenueSummaryLabel.setFont(font5)
        self.RevenueSummaryLabel.setStyleSheet(u"color:#f5f5f5;")

        self.horizontalLayout_33.addWidget(self.RevenueSummaryLabel)

        self.horizontalSpacer_28 = QSpacerItem(408, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_28)


        self.RevenueSummaryWidget.addLayout(self.horizontalLayout_33)

        self.ERRevenueSummaryGraph = PlotWidget(self.ContentWidget)
        self.ERRevenueSummaryGraph.setObjectName(u"ERRevenueSummaryGraph")
        self.ERRevenueSummaryGraph.setMinimumSize(QSize(0, 220))
        self.ERRevenueSummaryGraph.setStyleSheet(u"background-color:blue\n"
"")

        self.RevenueSummaryWidget.addWidget(self.ERRevenueSummaryGraph)


        self.verticalLayout.addLayout(self.RevenueSummaryWidget)

        self.RevenueStreamsWidget_2 = QVBoxLayout()
        self.RevenueStreamsWidget_2.setObjectName(u"RevenueStreamsWidget_2")
        self.RevenueStreamsWidget_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.RevenueStreamLabel = QLabel(self.ContentWidget)
        self.RevenueStreamLabel.setObjectName(u"RevenueStreamLabel")
        self.RevenueStreamLabel.setFont(font5)
        self.RevenueStreamLabel.setStyleSheet(u"color:#f5f5f5;")

        self.horizontalLayout_34.addWidget(self.RevenueStreamLabel)

        self.horizontalSpacer_36 = QSpacerItem(408, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_36)


        self.RevenueStreamsWidget_2.addLayout(self.horizontalLayout_34)

        self.ERRevenueStreamGraph = PlotWidget(self.ContentWidget)
        self.ERRevenueStreamGraph.setObjectName(u"ERRevenueStreamGraph")
        self.ERRevenueStreamGraph.setMinimumSize(QSize(0, 220))
        self.ERRevenueStreamGraph.setStyleSheet(u"background-color:blue\n"
"")

        self.RevenueStreamsWidget_2.addWidget(self.ERRevenueStreamGraph)


        self.verticalLayout.addLayout(self.RevenueStreamsWidget_2)


        self.verticalLayout_3.addWidget(self.ContentWidget)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_3)


        self.retranslateUi(Form)

        self.ModalSelectorComboER.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.EmployeeReportsLabel.setText(QCoreApplication.translate("Form", u"Employee Reports", None))
        self.DayButtonER.setText(QCoreApplication.translate("Form", u"Day", None))
        self.WeekButtonER.setText(QCoreApplication.translate("Form", u"Week", None))
        self.MonthButtonER.setText(QCoreApplication.translate("Form", u"Month", None))
        self.YearButtonER.setText(QCoreApplication.translate("Form", u"Year", None))
        self.ERSalesBreakdownLabel.setText(QCoreApplication.translate("Form", u"Sales Breakdown ", None))
        self.PostIconER.setText("")
        self.PostsLabelER.setText(QCoreApplication.translate("Form", u"Posts", None))
        self.PostDollarER.setText(QCoreApplication.translate("Form", u"$00.00", None))
        self.SubscribeIconER.setText("")
        self.SubscriptionsLabelER.setText(QCoreApplication.translate("Form", u"Subscriptions", None))
        self.SubscribeDollarER.setText(QCoreApplication.translate("Form", u"$00.00", None))
        self.MessagesIconER.setText("")
        self.MessagesLabelER.setText(QCoreApplication.translate("Form", u"Messages", None))
        self.MessagesDollarER.setText(QCoreApplication.translate("Form", u"$00.00", None))
        self.ReferralsIconER.setText("")
        self.ReferralsLabelER.setText(QCoreApplication.translate("Form", u"Referrals", None))
        self.ReferralDollarER.setText(QCoreApplication.translate("Form", u"$00.00", None))
        self.TipsIconsER.setText("")
        self.TipsLabelER.setText(QCoreApplication.translate("Form", u"Tips", None))
        self.TipsDollarER.setText(QCoreApplication.translate("Form", u"$00.00", None))
        self.ModalSelectorComboER.setItemText(0, QCoreApplication.translate("Form", u"PlaceHolder", None))
        self.ModalSelectorComboER.setItemText(1, QCoreApplication.translate("Form", u"PlaceHolder", None))
        self.ModalSelectorComboER.setItemText(2, QCoreApplication.translate("Form", u"PlaceHolder", None))

        self.ModalSelectorComboER.setCurrentText(QCoreApplication.translate("Form", u"PlaceHolder", None))
        self.RevenueSummaryLabel.setText(QCoreApplication.translate("Form", u"Revenue Summary", None))
        self.RevenueStreamLabel.setText(QCoreApplication.translate("Form", u"Revenue Streams", None))
    # retranslateUi

class EmployeeReports(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

