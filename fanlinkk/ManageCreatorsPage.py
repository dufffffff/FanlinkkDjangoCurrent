# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManageCreatorsPageHKTqGY.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 600)
        Form.setStyleSheet(u"background-color:#141414")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.ManageCreatorsLabel = QLabel(Form)
        self.ManageCreatorsLabel.setObjectName(u"ManageCreatorsLabel")
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(24)
        font.setBold(True)
        self.ManageCreatorsLabel.setFont(font)
        self.ManageCreatorsLabel.setStyleSheet(u"\n"
"color:#ffffff")

        self.horizontalLayout_20.addWidget(self.ManageCreatorsLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.AddCreatorFrame = QFrame(Form)
        self.AddCreatorFrame.setObjectName(u"AddCreatorFrame")
        self.AddCreatorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AddCreatorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.AddCreatorFrame)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 2, 9, 2)
        self.DisplayNameLabel = QLabel(self.AddCreatorFrame)
        self.DisplayNameLabel.setObjectName(u"DisplayNameLabel")
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(14)
        self.DisplayNameLabel.setFont(font1)
        self.DisplayNameLabel.setStyleSheet(u"\n"
"color:#ffffff")

        self.horizontalLayout_7.addWidget(self.DisplayNameLabel)

        self.DisplayNameLineEdit = QLineEdit(self.AddCreatorFrame)
        self.DisplayNameLineEdit.setObjectName(u"DisplayNameLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DisplayNameLineEdit.sizePolicy().hasHeightForWidth())
        self.DisplayNameLineEdit.setSizePolicy(sizePolicy)
        self.DisplayNameLineEdit.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setPointSize(11)
        self.DisplayNameLineEdit.setFont(font2)
        self.DisplayNameLineEdit.setStyleSheet(u"color:#ffffff;\n"
"background-color: #373737")

        self.horizontalLayout_7.addWidget(self.DisplayNameLineEdit)

        self.LoginEmailLabel = QLabel(self.AddCreatorFrame)
        self.LoginEmailLabel.setObjectName(u"LoginEmailLabel")
        self.LoginEmailLabel.setFont(font1)
        self.LoginEmailLabel.setStyleSheet(u"\n"
"color:#ffffff")

        self.horizontalLayout_7.addWidget(self.LoginEmailLabel)

        self.LoginEmailLineEdit = QLineEdit(self.AddCreatorFrame)
        self.LoginEmailLineEdit.setObjectName(u"LoginEmailLineEdit")
        sizePolicy.setHeightForWidth(self.LoginEmailLineEdit.sizePolicy().hasHeightForWidth())
        self.LoginEmailLineEdit.setSizePolicy(sizePolicy)
        self.LoginEmailLineEdit.setFont(font2)
        self.LoginEmailLineEdit.setStyleSheet(u"color:#ffffff;\n"
"background-color: #373737")

        self.horizontalLayout_7.addWidget(self.LoginEmailLineEdit)

        self.PasswordLabel = QLabel(self.AddCreatorFrame)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setFont(font1)
        self.PasswordLabel.setStyleSheet(u"\n"
"color:#ffffff")

        self.horizontalLayout_7.addWidget(self.PasswordLabel)

        self.PasswordLineEdit = QLineEdit(self.AddCreatorFrame)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        sizePolicy.setHeightForWidth(self.PasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.PasswordLineEdit.setSizePolicy(sizePolicy)
        self.PasswordLineEdit.setFont(font2)
        self.PasswordLineEdit.setStyleSheet(u"color:#ffffff;\n"
"background-color: #373737")
        self.PasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_7.addWidget(self.PasswordLineEdit)

        self.LinkAccountButton = QPushButton(self.AddCreatorFrame)
        self.LinkAccountButton.setObjectName(u"LinkAccountButton")
        self.LinkAccountButton.setMinimumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamilies([u"Futura PT"])
        font3.setPointSize(12)
        self.LinkAccountButton.setFont(font3)
        self.LinkAccountButton.setStyleSheet(u"""
            QPushButton {
                border-radius: 12px;
                background-color: #ffffff;  /* Default background color */
                color: #373737;  /* Default text color */
                padding: 3px;
            }
            QPushButton:hover {
                background-color: #373737;  /* Inverted background color on hover */
                color: #ffffff;  /* Inverted text color on hover */
            }
        """)
        self.LinkAccountButton.setFlat(False)

        self.horizontalLayout_7.addWidget(self.LinkAccountButton)

        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(5, 2)

        self.horizontalLayout_26.addWidget(self.AddCreatorFrame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_26)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font4 = QFont()
        font4.setFamilies([u"Futura PT"])
        font4.setPointSize(13)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        font5 = QFont()
        font5.setFamilies([u"Futura PT"])
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem10)
        font6 = QFont()
        font6.setFamilies([u"Futura PT"])
        font6.setPointSize(9)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font6);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.tableWidget.setItem(3, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.tableWidget.setItem(4, 2, __qtablewidgetitem22)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"background-color:#1f1f1f;\n"
"color:#ffffff")
        self.tableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.verticalHeader().setDefaultSectionSize(62)

        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 10)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ManageCreatorsLabel.setText(QCoreApplication.translate("Form", u"Manage Creators", None))
        self.DisplayNameLabel.setText(QCoreApplication.translate("Form", u"Display name: ", None))
        self.LoginEmailLabel.setText(QCoreApplication.translate("Form", u"Login Email: ", None))
        self.PasswordLabel.setText(QCoreApplication.translate("Form", u"Password: ", None))
        self.LinkAccountButton.setText(QCoreApplication.translate("Form", u"Link Acccount", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Creators", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Active", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Edit", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"1.", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"2.", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"3.", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"4.", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"5.", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi




class ManageCreators(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setVisible(False)

        self.ui.tableWidget.setStyleSheet("""
            QTableWidget {
                color: #ffffff;  /* Text color */
                background-color: #141414;  /* Background color */
                border-radius: 20px;  /* Adjust this value for more rounded corners */
                border: 2px solid #373737;  /* Outer border color for the table */
                padding: 5px;  /* Padding to prevent content from touching the border */
            }

            QTableWidget::item {
                background-color: #292929;  /* Cell background color */
                border: 3px solid #141414;  /* Cell border color matching table background */
                color: #ffffff;  /* Text color inside cells */
                border-radius: 6px;  /* Adjust this value for more rounded corners */
                padding: 2px;  /* Padding to prevent content from touching the border */

            }
                                          

            QHeaderView::section {
                background-color: #141414;  /* Background color of header */
                color: #ef910d;  /* Header text color */
                border: none;  /* No borders for the headers */
                padding: 5px;
                font-family: "Futura PT";  /* Set header font to match Models/Employees Under Management */
                font-size: 18px;  /* Adjust font size if needed */
                text-align: center;  /* Align text in the center */
            }

            QTableCornerButton::section {
                background-color: #141414;  /* Corner button (top-left of table) background color */
                border: none;  /* No border for the corner button */
            }
        """)



