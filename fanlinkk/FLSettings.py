from db_utils import get_user_by_email, get_active_user  # Ensure you import the required functions
from UserDetails import UserEditDialog
from PySide6.QtWidgets import QDialog
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FLSettingsAcecFV.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(805, 694)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.FLSettingLabel = QLabel(Form)
        self.FLSettingLabel.setObjectName(u"FLSettingLabel")
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(24)
        font.setBold(True)
        self.FLSettingLabel.setFont(font)
        self.FLSettingLabel.setStyleSheet(u"color:#ffffff")

        self.horizontalLayout_10.addWidget(self.FLSettingLabel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.DetailsWidget = QWidget(Form)
        self.DetailsWidget.setObjectName(u"DetailsWidget")
        self.gridLayout = QGridLayout(self.DetailsWidget)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.EmailLineEdit = QLineEdit(self.DetailsWidget)
        self.EmailLineEdit.setObjectName(u"EmailLineEdit")
        self.EmailLineEdit.setMinimumSize(QSize(150, 60))
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(12)
        self.EmailLineEdit.setFont(font1)
        self.EmailLineEdit.setStyleSheet(u"color:#ffffff;\n"
"background-color:#373737")

        self.gridLayout.addWidget(self.EmailLineEdit, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.NameLineEdit = QLineEdit(self.DetailsWidget)
        self.NameLineEdit.setObjectName(u"NameLineEdit")
        self.NameLineEdit.setMinimumSize(QSize(150, 60))
        self.NameLineEdit.setFont(font1)
        self.NameLineEdit.setStyleSheet(u"color:#ffffff;\n"
"background-color:#373737")

        self.gridLayout.addWidget(self.NameLineEdit, 0, 0, 1, 1)

        self.EditButton = QPushButton(self.DetailsWidget)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setMinimumSize(QSize(0, 40))
        self.EditButton.setFont(font1)
        self.EditButton.setStyleSheet(u"color:#ffffff;\n"
"background-color:#373737")

        self.gridLayout.addWidget(self.EditButton, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(4, 2)

        self.horizontalLayout.addWidget(self.DetailsWidget)

        self.SystemMessagesWidget = QWidget(Form)
        self.SystemMessagesWidget.setObjectName(u"SystemMessagesWidget")
        self.SystemMessagesWidget.setMinimumSize(QSize(472, 0))
        self.SystemMessagesWidget.setStyleSheet(u"background-color:#373737")
        self.verticalLayout_9 = QVBoxLayout(self.SystemMessagesWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.label_19 = QLabel(self.SystemMessagesWidget)
        self.label_19.setObjectName(u"label_19")
        font2 = QFont()
        font2.setFamilies([u"Futura PT"])
        font2.setPointSize(19)
        font2.setWeight(QFont.DemiBold)
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color:#ffffff;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_19)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.SystemMessagesArea = QLabel(self.SystemMessagesWidget)
        self.SystemMessagesArea.setObjectName(u"SystemMessagesArea")
        font3 = QFont()
        font3.setFamilies([u"Futura PT Book"])
        font3.setPointSize(12)
        self.SystemMessagesArea.setFont(font3)
        self.SystemMessagesArea.setStyleSheet(u"color:#ffffff;\n"
"")
        self.SystemMessagesArea.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.SystemMessagesArea.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.SystemMessagesArea)


        self.horizontalLayout.addWidget(self.SystemMessagesWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 293, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 8)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.FLSettingLabel.setText(QCoreApplication.translate("Form", u"Fanlinkk Settings", None))
        self.EmailLineEdit.setText("")
        self.EmailLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.NameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Name:", None))
        self.EditButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"System Messages", None))
        self.SystemMessagesArea.setText(QCoreApplication.translate("Form", u"FANLINKK Message area Will be update from server - to detail new updates, changes and important information to all users ", None))
    # retranslateUi





class FLSettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.SystemMessagesWidget.setStyleSheet("""
    background-color: #373737;
    border-radius: 20px;  /* Adjust this value for more rounded corners */
    color: #ffffff;  /* Text color inside the widget */
""")

        self.ui.EditButton.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;  /* Default background color */
                color: #373737;  /* Default text color */
                border-radius: 10px;  /* Rounded corners */
                padding: 10px;  /* Padding around the text */
                font-size: 14px;  /* Font size for the text */
                font-family: "Futura PT";  /* Font family */
            }
            
            QPushButton:hover {
                background-color: #373737;  /* Inverted background color on hover */
                color: #ffffff;  /* Inverted text color on hover */
            }

            QPushButton:pressed {
                background-color: #ffffff;  /* Pressed state background color */
                color: #373737;  /* Pressed state text color */
            }
        """)

        self.ui.NameLineEdit.setStyleSheet("""
            QLineEdit {
                background-color: #373737;  /* Background color */
                color: #ffffff;  /* Text color */
                border-radius: 10px;  /* Rounded corners */
                padding: 10px;  /* Padding inside the text box */
                font-size: 14px;  /* Font size */
                font-family: "Futura PT";  /* Font family */
                border: 1px solid #373737;  /* Border color matching background */
            }

            QLineEdit:focus {
                background-color: #ffffff;  /* Background color when focused */
                color: #373737;  /* Text color when focused */
                border: 1px solid #ef910d;  /* Border color when focused */
            }
        """)

        self.ui.EmailLineEdit.setStyleSheet("""
            QLineEdit {
                background-color: #373737;  /* Background color */
                color: #ffffff;  /* Text color */
                border-radius: 10px;  /* Rounded corners */
                padding: 10px;  /* Padding inside the text box */
                font-size: 14px;  /* Font size */
                font-family: "Futura PT";  /* Font family */
                border: 1px solid #373737;  /* Border color matching background */
            }

            QLineEdit:focus {
                background-color: #ffffff;  /* Background color when focused */
                color: #373737;  /* Text color when focused */
                border: 1px solid #ef910d;  /* Border color when focused */
            }
        """)

        self.ui.NameLineEdit.setReadOnly(True)
        self.ui.EmailLineEdit.setReadOnly(True)
        
        # Fetch the active user's email
        active_user_email = get_active_user()
    
        if active_user_email:
            # Get the user details by email
            user_data = get_user_by_email(active_user_email)
            
            if user_data:
                # Populate the fields with the user's name and email
                self.ui.NameLineEdit.setText(user_data['name'])
                self.ui.EmailLineEdit.setText(user_data['email'])

        self.ui.EditButton.clicked.connect(self.open_user_edit_dialog)

    def open_user_edit_dialog(self):
        # Create an instance of the dialog
        dialog = UserEditDialog(self)
        # Open the dialog
        if dialog.exec() == QDialog.Accepted:
            # Handle saving logic if the user clicks "OK"
            # You can retrieve updated data from the dialog here if needed
            print("Dialog accepted")
        else:
            print("Dialog rejected")
