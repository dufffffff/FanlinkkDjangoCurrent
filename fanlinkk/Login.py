

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeroDANSu.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget, QMessageBox)
import requests
from PySide6.QtWidgets import QDialog, QMessageBox
import json
from db_utils import verify_login, set_active_user


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(400, 300)
        self.verticalLayout_3 = QVBoxLayout(LoginForm)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 8, 0, 8)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.LoginLabel = QLabel(LoginForm)
        self.LoginLabel.setObjectName(u"LoginLabel")
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(20)
        self.LoginLabel.setFont(font)

        self.horizontalLayout.addWidget(self.LoginLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.EmailLineEdit = QLineEdit(LoginForm)
        self.EmailLineEdit.setObjectName(u"EmailLineEdit")
        self.EmailLineEdit.setPlaceholderText("Email")  # Set placeholder text



        self.horizontalLayout_2.addWidget(self.EmailLineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.PasswordLineEdit = QLineEdit(LoginForm)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_3.addWidget(self.PasswordLineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.buttonBox = QDialogButtonBox(LoginForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.buttonBox)

        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 2)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
        
    # setupUi


    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Dialog", None))
        self.LoginLabel.setText(QCoreApplication.translate("LoginForm", u"Log In", None))
        self.EmailLineEdit.setText(QCoreApplication.translate("LoginForm", u"", None))
        self.PasswordLineEdit.setText(QCoreApplication.translate("LoginForm", u"Password", None))
    # retranslateUi

import requests
from PySide6.QtWidgets import QDialog, QMessageBox
import json

class LoginPage(QDialog):
    session = requests.Session()  # Persistent session for the user
    jwt_token = None 
    refresh_token = None
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("Icon.ico")) 
        self.ui.buttonBox.accepted.connect(self.verify_login)
        self.ui.buttonBox.rejected.connect(self.reject)

    def verify_login(self):
        email = self.ui.EmailLineEdit.text()
        password = self.ui.PasswordLineEdit.text()

        login_url = 'http://127.0.0.1:8000/api/login/'  # Replace with your server's login API URL
        data = {
            'email': email,
            'password': password,
        }

        # Send login request
        try:
            response = self.session.post(login_url, data=data)
            if response.status_code == 200:
                result = response.json()
                access_token= result.get('token')
                refresh_token = result.get('refresh')
                if access_token and refresh_token:
                    print(f'JWT TOKENS SAVED: \n ACCESS TOKEN:{access_token} \n \n REFRESH TOKEN:{refresh_token}')
                    # Save token for later use
                    self.save_session(email, password, access_token, refresh_token )
                    QMessageBox.information(self, 'Login Success', "Login successful!")
                    self.accept()  # Close the dialog on success
                else:
                    QMessageBox.warning(self, 'Login Failed', 'No token returned.')
            else:
                QMessageBox.warning(self, 'Error', f"Failed to login: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, 'Error', f"Could not connect to the server: {e}")

    def save_session(self, email, password, access_token, refresh_token):
        with open('session.json', 'w') as session_file:
            json.dump({
                'email': email,
                'password': password,
                'access_token': access_token,
                'refresh_token': refresh_token
            }, session_file)
            
    def get_email(self):
        return self.ui.EmailLineEdit.text()

    def get_password(self):
        return self.ui.PasswordLineEdit.text()

    def get_token(self):
        try:
            with open('session.json', 'r') as session_file:
                session_data = json.load(session_file)
            return session_data.get('token')#, session_data.get('refresh')
        except Exception as e:
            return None
