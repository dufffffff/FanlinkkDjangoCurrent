# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChatterAnalytics.ui'
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

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(803, 873)
        self.verticalLayout = QVBoxLayout(widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_2 = QScrollArea(widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        font = QFont()
        font.setFamilies([u"Gill Sans MT"])
        font.setPointSize(12)
        font.setBold(True)
        self.scrollArea_2.setFont(font)
        self.scrollArea_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setMidLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 771, 853))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.CRLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.CRLabel.setObjectName(u"CRLabel")
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setKerning(True)
        self.CRLabel.setFont(font1)
        self.CRLabel.setStyleSheet(u"color:#f5f5f5")

        self.horizontalLayout_5.addWidget(self.CRLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.CRDateSelector = QHBoxLayout()
        self.CRDateSelector.setObjectName(u"CRDateSelector")
        self.CRDateSelector.setContentsMargins(0, -1, 0, -1)
        self.DayButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.DayButton.setObjectName(u"DayButton")
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.DayButton.setFont(font2)
        self.DayButton.setStyleSheet(u"	color:#f5f5f5;\n"
"\n"
"QPushButton::hover{\n"
"        background-color:green;\n"
"    }")
        self.DayButton.setCheckable(True)
        self.DayButton.setAutoExclusive(True)

        self.CRDateSelector.addWidget(self.DayButton)

        self.WeekButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.WeekButton.setObjectName(u"WeekButton")
        self.WeekButton.setFont(font2)
        self.WeekButton.setStyleSheet(u"	color:#f5f5f5;\n"
"    \n"
"")
        self.WeekButton.setCheckable(True)
        self.WeekButton.setAutoExclusive(True)

        self.CRDateSelector.addWidget(self.WeekButton)

        self.MonthButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.MonthButton.setObjectName(u"MonthButton")
        self.MonthButton.setFont(font2)
        self.MonthButton.setStyleSheet(u"	color:#f5f5f5;\n"
"\n"
"")
        self.MonthButton.setCheckable(True)
        self.MonthButton.setAutoExclusive(True)

        self.CRDateSelector.addWidget(self.MonthButton)

        self.YearButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.YearButton.setObjectName(u"YearButton")
        self.YearButton.setFont(font2)
        self.YearButton.setStyleSheet(u"	color:#f5f5f5;\n"
"")
        self.YearButton.setCheckable(True)
        self.YearButton.setAutoExclusive(True)

        self.CRDateSelector.addWidget(self.YearButton)


        self.horizontalLayout_5.addLayout(self.CRDateSelector)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 5)

        self.verticalLayout_16.addLayout(self.horizontalLayout_5)

        self.ModelComboWidget = QHBoxLayout()
        self.ModelComboWidget.setObjectName(u"ModelComboWidget")
        self.SecondHoriLayout = QHBoxLayout()
        self.SecondHoriLayout.setSpacing(0)
        self.SecondHoriLayout.setObjectName(u"SecondHoriLayout")
        self.CRSalesBreakdownWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.CRSalesBreakdownWidget.setObjectName(u"CRSalesBreakdownWidget")
        self.CRSalesBreakdownWidget.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.CRSalesBreakdownWidget)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(4, 4, 4, 4)
        self.CRSalesBreakdownLayout = QWidget(self.CRSalesBreakdownWidget)
        self.CRSalesBreakdownLayout.setObjectName(u"CRSalesBreakdownLayout")
        self.CRSalesBreakdownLayout.setMinimumSize(QSize(380, 0))
        self.CRSalesBreakdownLayout.setStyleSheet(u"")
        self.verticalLayout_50 = QVBoxLayout(self.CRSalesBreakdownLayout)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, -1, -1, -1)
        self.SaleBreakdownSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.SaleBreakdownSpacerLeft)

        self.SalesBreakdownCR = QLabel(self.CRSalesBreakdownLayout)
        self.SalesBreakdownCR.setObjectName(u"SalesBreakdownCR")
        font3 = QFont()
        font3.setFamilies([u"Futura PT"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setKerning(True)
        self.SalesBreakdownCR.setFont(font3)
        self.SalesBreakdownCR.setStyleSheet(u"Color:#EBEBEB")

        self.horizontalLayout_46.addWidget(self.SalesBreakdownCR)

        self.SlaesBreakdownSpacerRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.SlaesBreakdownSpacerRight)


        self.verticalLayout_50.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(14, -1, -1, -1)
        self.PostIconCR = QLabel(self.CRSalesBreakdownLayout)
        self.PostIconCR.setObjectName(u"PostIconCR")
        self.PostIconCR.setMaximumSize(QSize(24, 22))
        self.PostIconCR.setStyleSheet(u"border: none;")
        self.PostIconCR.setLineWidth(0)
        self.PostIconCR.setTextFormat(Qt.TextFormat.AutoText)
        self.PostIconCR.setPixmap(QPixmap(u":/Icons/Icons/paper-plane.svg"))
        self.PostIconCR.setScaledContents(True)
        self.PostIconCR.setWordWrap(False)
        self.PostIconCR.setMargin(3)
        self.PostIconCR.setIndent(19)

        self.horizontalLayout_16.addWidget(self.PostIconCR)

        self.PostLabelCR = QLabel(self.CRSalesBreakdownLayout)
        self.PostLabelCR.setObjectName(u"PostLabelCR")
        self.PostLabelCR.setFont(font2)
        self.PostLabelCR.setStyleSheet(u"border:none;\n"
"border-left: 5px black;\n"
"")
        self.PostLabelCR.setFrameShape(QFrame.Shape.Box)
        self.PostLabelCR.setMidLineWidth(6)
        self.PostLabelCR.setScaledContents(False)
        self.PostLabelCR.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PostLabelCR.setMargin(6)

        self.horizontalLayout_16.addWidget(self.PostLabelCR)

        self.PostDollarCR = QLabel(self.CRSalesBreakdownLayout)
        self.PostDollarCR.setObjectName(u"PostDollarCR")
        font4 = QFont()
        font4.setFamilies([u"Futura PT"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.PostDollarCR.setFont(font4)
        self.PostDollarCR.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_16.addWidget(self.PostDollarCR)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_55)


        self.verticalLayout_50.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(14, -1, -1, -1)
        self.SubscribeIconCR = QLabel(self.CRSalesBreakdownLayout)
        self.SubscribeIconCR.setObjectName(u"SubscribeIconCR")
        self.SubscribeIconCR.setMaximumSize(QSize(24, 24))
        self.SubscribeIconCR.setStyleSheet(u"border: none;")
        self.SubscribeIconCR.setLineWidth(0)
        self.SubscribeIconCR.setTextFormat(Qt.TextFormat.AutoText)
        self.SubscribeIconCR.setPixmap(QPixmap(u":/Icons/Icons/recycle.svg"))
        self.SubscribeIconCR.setScaledContents(True)
        self.SubscribeIconCR.setWordWrap(False)
        self.SubscribeIconCR.setMargin(0)
        self.SubscribeIconCR.setIndent(19)

        self.horizontalLayout_39.addWidget(self.SubscribeIconCR)

        self.SubscriberLabelCR = QLabel(self.CRSalesBreakdownLayout)
        self.SubscriberLabelCR.setObjectName(u"SubscriberLabelCR")
        self.SubscriberLabelCR.setFont(font2)
        self.SubscriberLabelCR.setStyleSheet(u"")
        self.SubscriberLabelCR.setMargin(6)

        self.horizontalLayout_39.addWidget(self.SubscriberLabelCR)

        self.SubscribeDollarCR = QLabel(self.CRSalesBreakdownLayout)
        self.SubscribeDollarCR.setObjectName(u"SubscribeDollarCR")
        self.SubscribeDollarCR.setFont(font4)
        self.SubscribeDollarCR.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_39.addWidget(self.SubscribeDollarCR)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_56)


        self.verticalLayout_50.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(14, -1, -1, -1)
        self.MessagesIconCR = QLabel(self.CRSalesBreakdownLayout)
        self.MessagesIconCR.setObjectName(u"MessagesIconCR")
        self.MessagesIconCR.setMaximumSize(QSize(24, 22))
        self.MessagesIconCR.setStyleSheet(u"border: none;\n"
"")
        self.MessagesIconCR.setLineWidth(0)
        self.MessagesIconCR.setTextFormat(Qt.TextFormat.AutoText)
        self.MessagesIconCR.setPixmap(QPixmap(u":/Icons/Icons/email.svg"))
        self.MessagesIconCR.setScaledContents(True)
        self.MessagesIconCR.setWordWrap(False)
        self.MessagesIconCR.setMargin(0)
        self.MessagesIconCR.setIndent(19)

        self.horizontalLayout_40.addWidget(self.MessagesIconCR)

        self.MessagesLabelCR = QLabel(self.CRSalesBreakdownLayout)
        self.MessagesLabelCR.setObjectName(u"MessagesLabelCR")
        self.MessagesLabelCR.setFont(font2)
        self.MessagesLabelCR.setStyleSheet(u"")
        self.MessagesLabelCR.setMargin(6)

        self.horizontalLayout_40.addWidget(self.MessagesLabelCR)

        self.MessagesDollarCR = QLabel(self.CRSalesBreakdownLayout)
        self.MessagesDollarCR.setObjectName(u"MessagesDollarCR")
        self.MessagesDollarCR.setFont(font4)
        self.MessagesDollarCR.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_40.addWidget(self.MessagesDollarCR)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_57)


        self.verticalLayout_50.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(14, -1, -1, -1)
        self.ReferralsIconCR = QLabel(self.CRSalesBreakdownLayout)
        self.ReferralsIconCR.setObjectName(u"ReferralsIconCR")
        self.ReferralsIconCR.setMaximumSize(QSize(24, 22))
        self.ReferralsIconCR.setStyleSheet(u"border: none;")
        self.ReferralsIconCR.setLineWidth(0)
        self.ReferralsIconCR.setTextFormat(Qt.TextFormat.AutoText)
        self.ReferralsIconCR.setPixmap(QPixmap(u":/Icons/Icons/link.svg"))
        self.ReferralsIconCR.setScaledContents(True)
        self.ReferralsIconCR.setWordWrap(False)
        self.ReferralsIconCR.setMargin(0)
        self.ReferralsIconCR.setIndent(19)

        self.horizontalLayout_41.addWidget(self.ReferralsIconCR)

        self.ReferralsLabelCR = QLabel(self.CRSalesBreakdownLayout)
        self.ReferralsLabelCR.setObjectName(u"ReferralsLabelCR")
        self.ReferralsLabelCR.setFont(font2)
        self.ReferralsLabelCR.setStyleSheet(u"")
        self.ReferralsLabelCR.setMargin(6)

        self.horizontalLayout_41.addWidget(self.ReferralsLabelCR)

        self.ReferralDollarCR = QLabel(self.CRSalesBreakdownLayout)
        self.ReferralDollarCR.setObjectName(u"ReferralDollarCR")
        self.ReferralDollarCR.setFont(font4)
        self.ReferralDollarCR.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_41.addWidget(self.ReferralDollarCR)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_58)


        self.verticalLayout_50.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(14, -1, -1, -1)
        self.TipsIconsCR = QLabel(self.CRSalesBreakdownLayout)
        self.TipsIconsCR.setObjectName(u"TipsIconsCR")
        self.TipsIconsCR.setMaximumSize(QSize(24, 24))
        self.TipsIconsCR.setStyleSheet(u"border: none;\n"
"")
        self.TipsIconsCR.setLineWidth(0)
        self.TipsIconsCR.setTextFormat(Qt.TextFormat.AutoText)
        self.TipsIconsCR.setPixmap(QPixmap(u":/Icons/Icons/give-money.svg"))
        self.TipsIconsCR.setScaledContents(True)
        self.TipsIconsCR.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.TipsIconsCR.setWordWrap(False)
        self.TipsIconsCR.setMargin(0)
        self.TipsIconsCR.setIndent(-1)

        self.horizontalLayout_42.addWidget(self.TipsIconsCR)

        self.TipsLabelCR = QLabel(self.CRSalesBreakdownLayout)
        self.TipsLabelCR.setObjectName(u"TipsLabelCR")
        self.TipsLabelCR.setFont(font2)
        self.TipsLabelCR.setStyleSheet(u"")
        self.TipsLabelCR.setMargin(6)

        self.horizontalLayout_42.addWidget(self.TipsLabelCR)

        self.TipsDollarCR = QLabel(self.CRSalesBreakdownLayout)
        self.TipsDollarCR.setObjectName(u"TipsDollarCR")
        self.TipsDollarCR.setFont(font4)
        self.TipsDollarCR.setStyleSheet(u"border: none;\n"
"color:#EBEBEB;")

        self.horizontalLayout_42.addWidget(self.TipsDollarCR)

        self.TipsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.TipsSpacer)


        self.verticalLayout_50.addLayout(self.horizontalLayout_42)


        self.verticalLayout_18.addWidget(self.CRSalesBreakdownLayout)


        self.SecondHoriLayout.addWidget(self.CRSalesBreakdownWidget)


        self.ModelComboWidget.addLayout(self.SecondHoriLayout)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(4, 4, 6, 4)
        self.ModalSelectorComboCR = QComboBox(self.scrollAreaWidgetContents_2)
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ModalSelectorComboCR.addItem(icon, "")
        self.ModalSelectorComboCR.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/user (2).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ModalSelectorComboCR.addItem(icon1, "")
        self.ModalSelectorComboCR.setObjectName(u"ModalSelectorComboCR")
        self.ModalSelectorComboCR.setMinimumSize(QSize(336, 57))
        font5 = QFont()
        font5.setFamilies([u"Futura PT"])
        font5.setPointSize(14)
        font5.setBold(False)
        self.ModalSelectorComboCR.setFont(font5)
        self.ModalSelectorComboCR.setStyleSheet(u"	color:#f5f5f5;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: #373737;\n"
"")
        self.ModalSelectorComboCR.setIconSize(QSize(32, 32))

        self.verticalLayout_22.addWidget(self.ModalSelectorComboCR)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer)


        self.ModelComboWidget.addLayout(self.verticalLayout_22)

        self.ModelComboWidget.setStretch(0, 1)
        self.ModelComboWidget.setStretch(1, 1)

        self.verticalLayout_16.addLayout(self.ModelComboWidget)

        self.RevenueSummaryWidgetCR = QWidget(self.scrollAreaWidgetContents_2)
        self.RevenueSummaryWidgetCR.setObjectName(u"RevenueSummaryWidgetCR")
        self.RevenueSummaryWidgetCR.setMinimumSize(QSize(725, 0))
        self.verticalLayout_24 = QVBoxLayout(self.RevenueSummaryWidgetCR)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 2, 4, 2)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.RevenueSummaryLabel_2 = QLabel(self.RevenueSummaryWidgetCR)
        self.RevenueSummaryLabel_2.setObjectName(u"RevenueSummaryLabel_2")
        self.RevenueSummaryLabel_2.setFont(font5)
        self.RevenueSummaryLabel_2.setStyleSheet(u"color:#f5f5f5;")

        self.horizontalLayout_18.addWidget(self.RevenueSummaryLabel_2)

        self.horizontalSpacer_19 = QSpacerItem(408, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_19)


        self.verticalLayout_21.addLayout(self.horizontalLayout_18)

        self.RevenueSummaryGraphCR = PlotWidget(self.RevenueSummaryWidgetCR)
        self.RevenueSummaryGraphCR.setObjectName(u"RevenueSummaryGraphCR")
        self.RevenueSummaryGraphCR.setMinimumSize(QSize(0, 220))
        self.RevenueSummaryGraphCR.setStyleSheet(u"background-color:blue\n"
"")

        self.verticalLayout_21.addWidget(self.RevenueSummaryGraphCR)

        self.verticalLayout_21.setStretch(0, 1)
        self.verticalLayout_21.setStretch(1, 9)

        self.verticalLayout_24.addLayout(self.verticalLayout_21)


        self.verticalLayout_16.addWidget(self.RevenueSummaryWidgetCR)

        self.RevenueStreamsWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.RevenueStreamsWidget.setObjectName(u"RevenueStreamsWidget")
        self.RevenueStreamsWidget.setMinimumSize(QSize(725, 0))
        self.verticalLayout_23 = QVBoxLayout(self.RevenueStreamsWidget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 2, 4, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.RevenueStreamsLabel = QLabel(self.RevenueStreamsWidget)
        self.RevenueStreamsLabel.setObjectName(u"RevenueStreamsLabel")
        self.RevenueStreamsLabel.setFont(font5)
        self.RevenueStreamsLabel.setStyleSheet(u"color:#f5f5f5;")

        self.horizontalLayout_17.addWidget(self.RevenueStreamsLabel)

        self.horizontalSpacer_20 = QSpacerItem(408, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_20)


        self.verticalLayout_23.addLayout(self.horizontalLayout_17)

        self.RevenueStreamsGraphCR = PlotWidget(self.RevenueStreamsWidget)
        self.RevenueStreamsGraphCR.setObjectName(u"RevenueStreamsGraphCR")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RevenueStreamsGraphCR.sizePolicy().hasHeightForWidth())
        self.RevenueStreamsGraphCR.setSizePolicy(sizePolicy)
        self.RevenueStreamsGraphCR.setMinimumSize(QSize(0, 220))
        self.RevenueStreamsGraphCR.setStyleSheet(u"background-color:blue\n"
"")

        self.verticalLayout_23.addWidget(self.RevenueStreamsGraphCR)

        self.verticalLayout_23.setStretch(0, 1)
        self.verticalLayout_23.setStretch(1, 6)

        self.verticalLayout_16.addWidget(self.RevenueStreamsWidget)


        self.verticalLayout_19.addLayout(self.verticalLayout_16)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)


        self.retranslateUi(widget)

        self.ModalSelectorComboCR.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.CRLabel.setText(QCoreApplication.translate("widget", u"Chatter Reports", None))
        self.DayButton.setText(QCoreApplication.translate("widget", u"Day", None))
        self.WeekButton.setText(QCoreApplication.translate("widget", u"Week", None))
        self.MonthButton.setText(QCoreApplication.translate("widget", u"Month", None))
        self.YearButton.setText(QCoreApplication.translate("widget", u"Year", None))
        self.SalesBreakdownCR.setText(QCoreApplication.translate("widget", u"Sales Breakdown ", None))
        self.PostIconCR.setText("")
        self.PostLabelCR.setText(QCoreApplication.translate("widget", u"Posts", None))
        self.PostDollarCR.setText(QCoreApplication.translate("widget", u"$00.00", None))
        self.SubscribeIconCR.setText("")
        self.SubscriberLabelCR.setText(QCoreApplication.translate("widget", u"Subscriptions", None))
        self.SubscribeDollarCR.setText(QCoreApplication.translate("widget", u"$00.00", None))
        self.MessagesIconCR.setText("")
        self.MessagesLabelCR.setText(QCoreApplication.translate("widget", u"Messages", None))
        self.MessagesDollarCR.setText(QCoreApplication.translate("widget", u"$00.00", None))
        self.ReferralsIconCR.setText("")
        self.ReferralsLabelCR.setText(QCoreApplication.translate("widget", u"Referrals", None))
        self.ReferralDollarCR.setText(QCoreApplication.translate("widget", u"$00.00", None))
        self.TipsIconsCR.setText("")
        self.TipsLabelCR.setText(QCoreApplication.translate("widget", u"Tips", None))
        self.TipsDollarCR.setText(QCoreApplication.translate("widget", u"$00.00", None))
        self.ModalSelectorComboCR.setItemText(0, QCoreApplication.translate("widget", u"PlaceHolder", None))
        self.ModalSelectorComboCR.setItemText(1, QCoreApplication.translate("widget", u"PlaceHolder", None))
        self.ModalSelectorComboCR.setItemText(2, QCoreApplication.translate("widget", u"PlaceHolder", None))

        self.ModalSelectorComboCR.setCurrentText(QCoreApplication.translate("widget", u"PlaceHolder", None))
        self.RevenueSummaryLabel_2.setText(QCoreApplication.translate("widget", u"Revenue Summary", None))
        self.RevenueStreamsLabel.setText(QCoreApplication.translate("widget", u"Revenue Streams", None))
    # retranslateUi

class ChatterAnalyticia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_widget()
        self.ui.setupUi(self)

