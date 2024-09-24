# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'full_menutVickE.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import Resources_rc

class Ui_FullMenu(object):
    def setupUi(self, FullMenu):
        if not FullMenu.objectName():
            FullMenu.setObjectName(u"FullMenu")
        FullMenu.resize(180, 916)
        FullMenu.setMinimumSize(QSize(180, 900))
        FullMenu.setMaximumSize(QSize(168, 1200))
        FullMenu.setStyleSheet(u"background-color:#373737;\n"
"")
        self.verticalLayout_53 = QVBoxLayout(FullMenu)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.FLMANLOGO = QLabel(FullMenu)
        self.FLMANLOGO.setObjectName(u"FLMANLOGO")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FLMANLOGO.sizePolicy().hasHeightForWidth())
        self.FLMANLOGO.setSizePolicy(sizePolicy)
        self.FLMANLOGO.setMinimumSize(QSize(180, 40))
        self.FLMANLOGO.setMaximumSize(QSize(65, 32))
        self.FLMANLOGO.setAutoFillBackground(False)
        self.FLMANLOGO.setStyleSheet(u"")
        self.FLMANLOGO.setFrameShape(QFrame.Shape.NoFrame)
        self.FLMANLOGO.setLineWidth(0)
        self.FLMANLOGO.setTextFormat(Qt.TextFormat.PlainText)
        self.FLMANLOGO.setPixmap(QPixmap(u":/Icons/Icons/Asset 1.svg"))
        self.FLMANLOGO.setScaledContents(True)
        self.FLMANLOGO.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FLMANLOGO.setWordWrap(False)
        self.FLMANLOGO.setMargin(3)
        self.FLMANLOGO.setIndent(0)

        self.verticalLayout_14.addWidget(self.FLMANLOGO)

        self.ButtonPages = QStackedWidget(FullMenu)
        self.ButtonPages.setObjectName(u"ButtonPages")
        font = QFont()
        font.setPointSize(11)
        self.ButtonPages.setFont(font)
        self.AnalyticsSidebarPage = QWidget()
        self.AnalyticsSidebarPage.setObjectName(u"AnalyticsSidebarPage")
        self.verticalLayout_3 = QVBoxLayout(self.AnalyticsSidebarPage)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 6, 0, 0)
        self.ERButton = QPushButton(self.AnalyticsSidebarPage)
        self.ERButton.setObjectName(u"ERButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ERButton.sizePolicy().hasHeightForWidth())
        self.ERButton.setSizePolicy(sizePolicy1)
        self.ERButton.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Futura PT Book"])
        font1.setPointSize(14)
        self.ERButton.setFont(font1)
        self.ERButton.setCheckable(True)
        self.ERButton.setFlat(True)

        self.verticalLayout_3.addWidget(self.ERButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.ButtonPages.addWidget(self.AnalyticsSidebarPage)
        self.FanserviceSidebarPage = QWidget()
        self.FanserviceSidebarPage.setObjectName(u"FanserviceSidebarPage")
        self.verticalLayout_55 = QVBoxLayout(self.FanserviceSidebarPage)
        self.verticalLayout_55.setSpacing(2)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.HomeButton = QPushButton(self.FanserviceSidebarPage)
        self.HomeButton.setObjectName(u"HomeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.HomeButton.sizePolicy().hasHeightForWidth())
        self.HomeButton.setSizePolicy(sizePolicy2)
        self.HomeButton.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setPointSize(14)
        self.HomeButton.setFont(font2)
        self.HomeButton.setCheckable(True)
        self.HomeButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.HomeButton)

        self.DiscoverButton = QPushButton(self.FanserviceSidebarPage)
        self.DiscoverButton.setObjectName(u"DiscoverButton")
        sizePolicy2.setHeightForWidth(self.DiscoverButton.sizePolicy().hasHeightForWidth())
        self.DiscoverButton.setSizePolicy(sizePolicy2)
        self.DiscoverButton.setMinimumSize(QSize(0, 40))
        self.DiscoverButton.setFont(font2)
        self.DiscoverButton.setCheckable(True)
        self.DiscoverButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.DiscoverButton)

        self.NotificationsButton = QPushButton(self.FanserviceSidebarPage)
        self.NotificationsButton.setObjectName(u"NotificationsButton")
        sizePolicy2.setHeightForWidth(self.NotificationsButton.sizePolicy().hasHeightForWidth())
        self.NotificationsButton.setSizePolicy(sizePolicy2)
        self.NotificationsButton.setMinimumSize(QSize(0, 40))
        self.NotificationsButton.setFont(font2)
        self.NotificationsButton.setStyleSheet(u"margin:")
        self.NotificationsButton.setCheckable(True)
        self.NotificationsButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.NotificationsButton)

        self.VaultButton = QPushButton(self.FanserviceSidebarPage)
        self.VaultButton.setObjectName(u"VaultButton")
        sizePolicy2.setHeightForWidth(self.VaultButton.sizePolicy().hasHeightForWidth())
        self.VaultButton.setSizePolicy(sizePolicy2)
        self.VaultButton.setMinimumSize(QSize(0, 40))
        self.VaultButton.setFont(font2)
        self.VaultButton.setStyleSheet(u"")
        self.VaultButton.setCheckable(True)
        self.VaultButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.VaultButton)

        self.QueueButton = QPushButton(self.FanserviceSidebarPage)
        self.QueueButton.setObjectName(u"QueueButton")
        sizePolicy2.setHeightForWidth(self.QueueButton.sizePolicy().hasHeightForWidth())
        self.QueueButton.setSizePolicy(sizePolicy2)
        self.QueueButton.setMinimumSize(QSize(0, 40))
        self.QueueButton.setFont(font2)
        self.QueueButton.setCheckable(True)
        self.QueueButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.QueueButton)

        self.InsightsButton = QPushButton(self.FanserviceSidebarPage)
        self.InsightsButton.setObjectName(u"InsightsButton")
        sizePolicy2.setHeightForWidth(self.InsightsButton.sizePolicy().hasHeightForWidth())
        self.InsightsButton.setSizePolicy(sizePolicy2)
        self.InsightsButton.setMinimumSize(QSize(0, 40))
        self.InsightsButton.setFont(font2)
        self.InsightsButton.setCheckable(True)
        self.InsightsButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.InsightsButton)

        self.ProfileButton = QPushButton(self.FanserviceSidebarPage)
        self.ProfileButton.setObjectName(u"ProfileButton")
        sizePolicy2.setHeightForWidth(self.ProfileButton.sizePolicy().hasHeightForWidth())
        self.ProfileButton.setSizePolicy(sizePolicy2)
        self.ProfileButton.setMinimumSize(QSize(3, 40))
        self.ProfileButton.setFont(font2)
        self.ProfileButton.setCheckable(True)
        self.ProfileButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.ProfileButton)

        self.NewPostsButton = QPushButton(self.FanserviceSidebarPage)
        self.NewPostsButton.setObjectName(u"NewPostsButton")
        sizePolicy2.setHeightForWidth(self.NewPostsButton.sizePolicy().hasHeightForWidth())
        self.NewPostsButton.setSizePolicy(sizePolicy2)
        self.NewPostsButton.setMinimumSize(QSize(0, 40))
        self.NewPostsButton.setFont(font2)
        self.NewPostsButton.setCheckable(True)
        self.NewPostsButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.NewPostsButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_55.addLayout(self.verticalLayout_4)

        self.ButtonPages.addWidget(self.FanserviceSidebarPage)
        self.EmptySidebarPage = QWidget()
        self.EmptySidebarPage.setObjectName(u"EmptySidebarPage")
        self.verticalLayout_54 = QVBoxLayout(self.EmptySidebarPage)
        self.verticalLayout_54.setSpacing(5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_11)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_10)


        self.verticalLayout_54.addLayout(self.verticalLayout_13)

        self.ButtonPages.addWidget(self.EmptySidebarPage)
        self.CreatorSidebarPage = QWidget()
        self.CreatorSidebarPage.setObjectName(u"CreatorSidebarPage")
        self.verticalLayout_10 = QVBoxLayout(self.CreatorSidebarPage)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ManageCreatorsButton = QPushButton(self.CreatorSidebarPage)
        self.ManageCreatorsButton.setObjectName(u"ManageCreatorsButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ManageCreatorsButton.sizePolicy().hasHeightForWidth())
        self.ManageCreatorsButton.setSizePolicy(sizePolicy3)
        self.ManageCreatorsButton.setMinimumSize(QSize(0, 40))
        self.ManageCreatorsButton.setFont(font1)
        self.ManageCreatorsButton.setCheckable(True)
        self.ManageCreatorsButton.setFlat(True)

        self.verticalLayout_6.addWidget(self.ManageCreatorsButton)

        self.FanvueSettingsButton = QPushButton(self.CreatorSidebarPage)
        self.FanvueSettingsButton.setObjectName(u"FanvueSettingsButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.FanvueSettingsButton.sizePolicy().hasHeightForWidth())
        self.FanvueSettingsButton.setSizePolicy(sizePolicy4)
        self.FanvueSettingsButton.setMinimumSize(QSize(0, 40))
        self.FanvueSettingsButton.setFont(font1)
        self.FanvueSettingsButton.setCheckable(True)
        self.FanvueSettingsButton.setFlat(True)

        self.verticalLayout_6.addWidget(self.FanvueSettingsButton)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.ButtonPages.addWidget(self.CreatorSidebarPage)
        self.TeamSidebarPage = QWidget()
        self.TeamSidebarPage.setObjectName(u"TeamSidebarPage")
        self.verticalLayout_7 = QVBoxLayout(self.TeamSidebarPage)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 0)
        self.TeamLayoutButton = QPushButton(self.TeamSidebarPage)
        self.TeamLayoutButton.setObjectName(u"TeamLayoutButton")
        sizePolicy3.setHeightForWidth(self.TeamLayoutButton.sizePolicy().hasHeightForWidth())
        self.TeamLayoutButton.setSizePolicy(sizePolicy3)
        self.TeamLayoutButton.setMinimumSize(QSize(0, 40))
        self.TeamLayoutButton.setFont(font1)
        self.TeamLayoutButton.setCheckable(True)
        self.TeamLayoutButton.setFlat(True)

        self.verticalLayout_7.addWidget(self.TeamLayoutButton)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.ButtonPages.addWidget(self.TeamSidebarPage)

        self.verticalLayout_14.addWidget(self.ButtonPages)

        self.MainButtonLayout = QVBoxLayout()
        self.MainButtonLayout.setSpacing(0)
        self.MainButtonLayout.setObjectName(u"MainButtonLayout")
        self.DAMain = QPushButton(FullMenu)
        self.DAMain.setObjectName(u"DAMain")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.DAMain.sizePolicy().hasHeightForWidth())
        self.DAMain.setSizePolicy(sizePolicy5)
        self.DAMain.setMinimumSize(QSize(180, 40))
        font3 = QFont()
        font3.setFamilies([u"Futura PT"])
        font3.setPointSize(13)
        font3.setBold(False)
        self.DAMain.setFont(font3)
        self.DAMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.DAMain.setAutoFillBackground(False)
        self.DAMain.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/dashboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Icons/Icons/dashboard (4).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.DAMain.setIcon(icon)
        self.DAMain.setIconSize(QSize(30, 30))
        self.DAMain.setCheckable(True)
        self.DAMain.setAutoExclusive(True)
        self.DAMain.setAutoRepeatInterval(97)
        self.DAMain.setFlat(True)

        self.MainButtonLayout.addWidget(self.DAMain)

        self.FSMain = QPushButton(FullMenu)
        self.FSMain.setObjectName(u"FSMain")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.FSMain.sizePolicy().hasHeightForWidth())
        self.FSMain.setSizePolicy(sizePolicy6)
        self.FSMain.setMinimumSize(QSize(180, 40))
        font4 = QFont()
        font4.setFamilies([u"Futura PT"])
        font4.setPointSize(13)
        self.FSMain.setFont(font4)
        self.FSMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/FanService (3).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Icons/FanService (2).svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FSMain.setIcon(icon1)
        self.FSMain.setIconSize(QSize(28, 28))
        self.FSMain.setCheckable(True)
        self.FSMain.setAutoExclusive(True)
        self.FSMain.setFlat(True)

        self.MainButtonLayout.addWidget(self.FSMain)

        self.ANMain = QPushButton(FullMenu)
        self.ANMain.setObjectName(u"ANMain")
        sizePolicy6.setHeightForWidth(self.ANMain.sizePolicy().hasHeightForWidth())
        self.ANMain.setSizePolicy(sizePolicy6)
        self.ANMain.setMinimumSize(QSize(180, 40))
        self.ANMain.setFont(font4)
        self.ANMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ANMain.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/bar-chart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Icons/bar-chart (1).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.ANMain.setIcon(icon2)
        self.ANMain.setIconSize(QSize(28, 28))
        self.ANMain.setCheckable(True)
        self.ANMain.setAutoExclusive(True)
        self.ANMain.setFlat(True)

        self.MainButtonLayout.addWidget(self.ANMain)

        self.TEMain = QPushButton(FullMenu)
        self.TEMain.setObjectName(u"TEMain")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.TEMain.sizePolicy().hasHeightForWidth())
        self.TEMain.setSizePolicy(sizePolicy7)
        self.TEMain.setMinimumSize(QSize(180, 40))
        self.TEMain.setFont(font4)
        self.TEMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/team.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Icons/team (2).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.TEMain.setIcon(icon3)
        self.TEMain.setIconSize(QSize(30, 30))
        self.TEMain.setCheckable(True)
        self.TEMain.setAutoExclusive(True)
        self.TEMain.setFlat(True)

        self.MainButtonLayout.addWidget(self.TEMain)

        self.CEMain = QPushButton(FullMenu)
        self.CEMain.setObjectName(u"CEMain")
        sizePolicy7.setHeightForWidth(self.CEMain.sizePolicy().hasHeightForWidth())
        self.CEMain.setSizePolicy(sizePolicy7)
        self.CEMain.setMinimumSize(QSize(180, 40))
        self.CEMain.setFont(font4)
        self.CEMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/Icons/user (2).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.CEMain.setIcon(icon4)
        self.CEMain.setIconSize(QSize(28, 28))
        self.CEMain.setCheckable(True)
        self.CEMain.setAutoExclusive(True)
        self.CEMain.setFlat(True)

        self.MainButtonLayout.addWidget(self.CEMain)

        self.SEMain = QPushButton(FullMenu)
        self.SEMain.setObjectName(u"SEMain")
        sizePolicy3.setHeightForWidth(self.SEMain.sizePolicy().hasHeightForWidth())
        self.SEMain.setSizePolicy(sizePolicy3)
        self.SEMain.setMinimumSize(QSize(150, 40))
        self.SEMain.setFont(font4)
        self.SEMain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/setting-lines.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/Icons/setting-lines (1).svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.SEMain.setIcon(icon5)
        self.SEMain.setIconSize(QSize(24, 24))
        self.SEMain.setCheckable(True)
        self.SEMain.setAutoExclusive(True)
        self.SEMain.setFlat(True)

        self.MainButtonLayout.addWidget(self.SEMain)


        self.verticalLayout_14.addLayout(self.MainButtonLayout)


        self.verticalLayout_53.addLayout(self.verticalLayout_14)


        self.retranslateUi(FullMenu)

        self.ButtonPages.setCurrentIndex(4)
        self.HomeButton.setDefault(False)
        self.DiscoverButton.setDefault(False)
        self.NotificationsButton.setDefault(False)
        self.VaultButton.setDefault(False)
        self.QueueButton.setDefault(False)
        self.InsightsButton.setDefault(False)
        self.ProfileButton.setDefault(False)
        self.NewPostsButton.setDefault(False)


        QMetaObject.connectSlotsByName(FullMenu)
    # setupUi

    def retranslateUi(self, FullMenu):
        self.FLMANLOGO.setText("")
        self.ERButton.setText(QCoreApplication.translate("FullMenu", u"Employee Reports", None))
        self.HomeButton.setText(QCoreApplication.translate("FullMenu", u"Home", None))
        self.DiscoverButton.setText(QCoreApplication.translate("FullMenu", u"Discover", None))
        self.NotificationsButton.setText(QCoreApplication.translate("FullMenu", u"Notifications", None))
        self.VaultButton.setText(QCoreApplication.translate("FullMenu", u"Vault", None))
        self.QueueButton.setText(QCoreApplication.translate("FullMenu", u"Queue", None))
        self.InsightsButton.setText(QCoreApplication.translate("FullMenu", u"Insights", None))
        self.ProfileButton.setText(QCoreApplication.translate("FullMenu", u"Profile", None))
        self.NewPostsButton.setText(QCoreApplication.translate("FullMenu", u"New Posts", None))
        self.ManageCreatorsButton.setText(QCoreApplication.translate("FullMenu", u"Manage Creators", None))
        self.FanvueSettingsButton.setText(QCoreApplication.translate("FullMenu", u"Fanvue Settings", None))
        self.TeamLayoutButton.setText(QCoreApplication.translate("FullMenu", u"Team Layout", None))
        self.DAMain.setText(QCoreApplication.translate("FullMenu", u" Dashboard", None))
#if QT_CONFIG(shortcut)
        self.DAMain.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.FSMain.setText(QCoreApplication.translate("FullMenu", u" Fan Service", None))
        self.ANMain.setText(QCoreApplication.translate("FullMenu", u" Analytics", None))
#if QT_CONFIG(shortcut)
        self.ANMain.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.TEMain.setText(QCoreApplication.translate("FullMenu", u" Team", None))
        self.CEMain.setText(QCoreApplication.translate("FullMenu", u" Creators", None))
        self.SEMain.setText(QCoreApplication.translate("FullMenu", u" Fanlinkk Settings", None))
        pass
    # retranslateUi





class FullMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FullMenu()
        self.ui.setupUi(self)

