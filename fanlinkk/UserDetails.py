from db_utils import get_active_user, get_user_by_email, update_user
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserChangevJthtW.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget, QMessageBox)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color:#141414")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.EmailLineEdit = QLineEdit(Dialog)
        self.EmailLineEdit.setObjectName(u"EmailLineEdit")
        self.EmailLineEdit.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(12)
        self.EmailLineEdit.setFont(font)
        self.EmailLineEdit.setStyleSheet(u"color:#ffffff")

        self.gridLayout.addWidget(self.EmailLineEdit, 1, 0, 1, 1)

        self.PasswordLineEdit = QLineEdit(Dialog)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setMinimumSize(QSize(150, 0))
        self.PasswordLineEdit.setFont(font)
        self.PasswordLineEdit.setStyleSheet(u"color:#ffffff")

        self.gridLayout.addWidget(self.PasswordLineEdit, 2, 0, 1, 1)

        self.NameLineEdit = QLineEdit(Dialog)
        self.NameLineEdit.setObjectName(u"NameLineEdit")
        self.NameLineEdit.setMinimumSize(QSize(150, 0))
        self.NameLineEdit.setFont(font)
        self.NameLineEdit.setStyleSheet(u"color:#ffffff")

        self.gridLayout.addWidget(self.NameLineEdit, 0, 0, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet(u"color:#ffffff")
        self.checkBox.setTristate(False)

        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(14)
        self.buttonBox.setFont(font1)
        self.buttonBox.setStyleSheet(u"color:#ffffff")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.EmailLineEdit.setText("")
        self.EmailLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.PasswordLineEdit.setText("")
        self.PasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.NameLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Show", None))
    # retranslateUi




class UserEditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()  # Using the dialog UI form
        self.ui.setupUi(self)
        self.setWindowTitle("Edit User")
        self.setWindowIcon(QIcon("Icon.ico"))



    # Set styling for the QLineEdit fields
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

        self.ui.PasswordLineEdit.setStyleSheet("""
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

        # Set styling for the QCheckBox
        self.ui.checkBox.setStyleSheet("""
            QCheckBox {
                color: #ffffff;  /* Text color */
                font-family: "Futura PT";  /* Font family */
                font-size: 14px;  /* Font size */
            }
            
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }

            QCheckBox::indicator:unchecked {
                background-color: #373737;
                border: 1px solid #ffffff;
            }

            QCheckBox::indicator:checked {
                background-color: #ef910d;
                border: 1px solid #ffffff;
            }
        """)

        # Set styling for the QDialogButtonBox
        self.ui.buttonBox.setStyleSheet("""
            QDialogButtonBox {
                font-family: "Futura PT";
                font-size: 14px;
            }

            QDialogButtonBox QPushButton {
                background-color: #ffffff;
                color: #373737;
                border-radius: 10px;
                padding: 10px;
            }

            QDialogButtonBox QPushButton:hover {
                background-color: #373737;
                color: #ffffff;
            }

            QDialogButtonBox QPushButton:pressed {
                background-color: #ffffff;
                color: #373737;
            }
        """)        

        # Populate the dialog with the current user's information
        active_user_email = get_active_user()
        if active_user_email:
            user_data = get_user_by_email(active_user_email)
            if user_data:
                self.user_id = user_data['id']  # Ensure user ID is stored for updating
                self.ui.NameLineEdit.setText(user_data['name'])
                self.ui.EmailLineEdit.setText(user_data['email'])
                self.ui.PasswordLineEdit.setText('')  # Leave password blank
                self.ui.PasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)  # Hide password by default

                # Connect the checkbox to toggle password visibility
                self.ui.checkBox.toggled.connect(self.toggle_password_visibility)

        # Connect the Save button to the save function
        self.ui.buttonBox.accepted.connect(self.save_user_details)

    def toggle_password_visibility(self, checked):
        """Toggle between showing and hiding the password."""
        if checked:
            self.ui.PasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)  # Show the password
        else:
            self.ui.PasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)  # Hide the password

    def save_user_details(self):
        """Save the updated user details."""
        name = self.ui.NameLineEdit.text()
        email = self.ui.EmailLineEdit.text()
        password = self.ui.PasswordLineEdit.text()  # Fetch the password

        # Update the user in the database
        try:
            # Pass the user ID and password to ensure the correct user is updated
            update_user(self.user_id, name=name, email=email, password=password)
            QMessageBox.information(self, "Success", "User details updated successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")


