# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FSHome.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, )
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select, create_engine
from db_utils import models   
import logging

engine = create_engine('sqlite:///my_database.db')
Session = sessionmaker(bind=engine)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, -1, -1, -1)
        self.HomeHLayout = QHBoxLayout()
        self.HomeHLayout.setObjectName(u"HomeHLayout")
        self.HomeHLayout.setContentsMargins(4, -1, -1, -1)
        self.HomeLabel = QLabel(Form)
        self.HomeLabel.setObjectName(u"HomeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HomeLabel.sizePolicy().hasHeightForWidth())
        self.HomeLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(24)
        self.HomeLabel.setFont(font)

        self.HomeHLayout.addWidget(self.HomeLabel)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HomeHLayout.addItem(self.horizontalSpacer_22)

        self.HomeMSelector = QComboBox(Form)
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.HomeMSelector.addItem(icon, "")
        self.HomeMSelector.setObjectName(u"HomeMSelector")
        sizePolicy.setHeightForWidth(self.HomeMSelector.sizePolicy().hasHeightForWidth())
        self.HomeMSelector.setSizePolicy(sizePolicy)
        self.HomeMSelector.setMinimumSize(QSize(124, 54))
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(12)
        self.HomeMSelector.setFont(font1)
        self.HomeMSelector.setStyleSheet(u"")

        self.HomeHLayout.addWidget(self.HomeMSelector)

        self.horizontalSpacer_21 = QSpacerItem(588, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HomeHLayout.addItem(self.horizontalSpacer_21)

        self.HomeHLayout.setStretch(0, 1)
        self.HomeHLayout.setStretch(1, 9)
        self.HomeHLayout.setStretch(2, 1)
        self.HomeHLayout.setStretch(3, 1)

        self.verticalLayout_25.addLayout(self.HomeHLayout)

        self.HomeWebWidget = QWidget(Form)
        self.HomeWebWidget.setObjectName(u"HomeWebWidget")
        self.HomeWebWidget.setStyleSheet(u"background-color: white;\n"
"")

        self.verticalLayout_25.addWidget(self.HomeWebWidget)

        self.verticalLayout_25.setStretch(0, 1)
        self.verticalLayout_25.setStretch(1, 12)

        self.verticalLayout.addLayout(self.verticalLayout_25)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.HomeLabel.setText(QCoreApplication.translate("Form", u"Home", None))
        self.HomeMSelector.setItemText(0, QCoreApplication.translate("Form", u"Placeholder", None))


class FSHomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Create a separate browser profile for FSLists
        self.profile = QWebEngineProfile("fs_lists_profile", self)

        # Create a QWebEnginePage using this profile
        self.page = QWebEnginePage(self.profile, self)

        # Create the browser window and set the page with the custom profile
        self.browser_window = QWebEngineView()
        self.browser_window.setPage(self.page)

        # Set up the layout and add the browser window
        browser_layout = QVBoxLayout(self.ui.HomeWebWidget)
        browser_layout.addWidget(self.browser_window)

        self.browser_window.setUrl(QUrl("https://fanvue.com/lists"))

        # Populate the dropdown menu with models
        self.populate_model_selector()

        # Connect the dropdown menu to a method that handles login when a model is selected
        self.ui.HomeMSelector.currentIndexChanged.connect(self.on_model_selected)

    def populate_model_selector(self):
        session = Session()
        try:
            query = select(models.c.name, models.c.csrf_cookies, models.c.auth_token).order_by(models.c.name)
            result = session.execute(query).fetchall()

            self.ui.HomeMSelector.clear()

            if result:
                for model_name, csrf_cookies, auth_token in result:
                    self.ui.HomeMSelector.addItem(model_name, userData=(csrf_cookies, auth_token))
                logging.info("Model dropdown populated successfully.")
            else:
                logging.warning("No models found in the database.")
        except Exception as e:
            logging.error(f"An error occurred while populating the model dropdown: {e}")
        finally:
            session.close()

    def on_model_selected(self, index):
        selected_data = self.ui.HomeMSelector.itemData(index)

        if selected_data:
            csrf_cookies, auth_token = selected_data
            logging.info(f"Selected model's tokens - CSRF: {csrf_cookies}, Auth: {auth_token}")

            # Inject the tokens into the browser and log in
            self.inject_tokens_and_login(csrf_cookies, auth_token)

    def inject_tokens_and_login(self, csrf_cookies, auth_token):
        logging.info(f"Attempting to inject tokens for model login.")

        def clear_cookies(profile):
            cookie_store = profile.cookieStore()
            cookie_store.deleteAllCookies()
            logging.info("All cookies cleared from the browser profile.")

        # Clear all cookies from the current profile
        clear_cookies(self.profile)

        # JavaScript to set new cookies
        js_code = f"""
        try {{
            console.log("Setting new cookies and clearing sessionStorage...");

            // Set new cookies and sessionStorage
            document.cookie = "_Host-next-auth.csrf-token={csrf_cookies}; path=/; secure;";
            document.cookie = "fv-auth.session-token={auth_token}; path=/; secure;";
            
            sessionStorage.setItem('someKey', 'someValue');  // Example if needed

            console.log("New cookies set successfully.");

            // Reload the page to apply cookies
            window.location.reload();
        }} catch (error) {{
            console.error("Error during token injection: ", error);
        }}
        """

        try:
            self.browser_window.page().runJavaScript(js_code)
            logging.info("JavaScript executed, cookies cleared and injected.")
        except Exception as e:
            logging.error(f"Error injecting cookies: {e}")
     
    def closeEvent(self, event):
        logging.info("Cleaning up FSHomePage web resources.")
        self.browser_window.setPage(None)
        self.page.deleteLater()
        super().closeEvent(event)