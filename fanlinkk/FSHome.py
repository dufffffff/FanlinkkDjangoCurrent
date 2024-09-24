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
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineCookieStore
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, )
from PySide6.QtNetwork import QNetworkCookie
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select, create_engine
from db_utils import get_active_user, get_models_for_user, users, user_models, models, Session  # Add other necessary imports
  
import logging


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 600)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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
        font.setBold(True)
        self.HomeLabel.setFont(font)
        self.HomeLabel.setStyleSheet(u"color:#FFFFFF")

        self.horizontalLayout.addWidget(self.HomeLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, -1, -1)

        
        self.HomeMSelector = QComboBox(Form)
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.HomeMSelector.addItem(icon, "")
        self.HomeMSelector.setObjectName(u"HomeMSelector")
        sizePolicy.setHeightForWidth(self.HomeMSelector.sizePolicy().hasHeightForWidth())
        self.HomeMSelector.setSizePolicy(sizePolicy)
        self.HomeMSelector.setMinimumSize(QSize(120, 30))
        self.HomeMSelector.setMaximumSize(QSize(120, 40))
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(15)
        self.HomeMSelector.setFont(font1)
        self.HomeMSelector.setStyleSheet("""
    QComboBox {
        background-color: #ffffff;  /* Background color */
        color: #000000;  /* Text color */
        font-size: 24px;  /* Font size */
        padding-left: 30px;
        padding-right: 20px;  /* Corrected px */
        font-family: "Futura PT";  /* Font family */
    }
""")

        self.horizontalLayout_2.addWidget(self.HomeMSelector)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.HomeWebWidget = QWidget(Form)
        self.HomeWebWidget.setObjectName(u"HomeWebWidget")
        self.HomeWebWidget.setStyleSheet(u"background-color: 141414;\n"
"")

        self.verticalLayout.addWidget(self.HomeWebWidget)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 9)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.HomeLabel.setText(QCoreApplication.translate("Form", u"Fan Service", None))
        self.HomeMSelector.setItemText(0, QCoreApplication.translate("Form", u"Placeholder", None))

    # retranslateUi


class FSHomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Create an in-memory browser profile
        self.profile = QWebEngineProfile(self)

        # Set the profile to use in-memory storage for cookies and cache
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        self.profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)

        # Create a QWebEnginePage using this profile
        self.page = QWebEnginePage(self.profile, self)

        # Create the browser window and set the page with the custom profile
        self.browser_window = QWebEngineView()
        self.browser_window.setPage(self.page)

        # Set up the layout and add the browser window
        browser_layout = QVBoxLayout(self.ui.HomeWebWidget)
        browser_layout.addWidget(self.browser_window)

        # Load the initial URL
        self.browser_window.setUrl(QUrl("https://fanvue.com/home"))

        # Populate the dropdown menu with models
        self.populate_model_selector()

        # Connect the dropdown menu to handle login when a model is selected
        self.ui.HomeMSelector.currentIndexChanged.connect(self.on_model_selected)

        # Connect the URL change to a method that checks for 'settings'
        self.browser_window.urlChanged.connect(self.check_url_and_redirect)


    def populate_model_selector(self):
        session = Session()
        try:
            # Get the currently active user's email
            active_user_email = get_active_user()
            if not active_user_email:
                logging.error("No active user found.")
                return

            # Fetch the user ID based on the active user's email
            user_query = select(users.c.id).where(users.c.email == active_user_email)
            user_id = session.execute(user_query).scalar()

            if not user_id:
                logging.error(f"User with email {active_user_email} not found.")
                return

            # Fetch models assigned to the active user using user_models table
            query = (
                select(models.c.name, models.c.csrf_cookies, models.c.auth_token)
                .select_from(user_models.join(models))
                .where(user_models.c.user_id == user_id)
                .order_by(models.c.name)
            )
            result = session.execute(query).fetchall()

            self.ui.HomeMSelector.clear()

            if result:
                for model_name, csrf_cookies, auth_token in result:
                    self.ui.HomeMSelector.addItem(model_name, userData=(csrf_cookies, auth_token))
                logging.info("Model dropdown populated successfully with active user's models.")

                # If there's only one model, manually trigger selection
                if len(result) == 1:
                    self.ui.HomeMSelector.setCurrentIndex(0)  # Select the first item
                    self.on_model_selected(0)  # Trigger the selection manually
            else:
                logging.warning("No models found for the active user.")
        except Exception as e:
            logging.error(f"An error occurred while populating the model dropdown: {e}")
        finally:
            session.close()
    def check_url_and_redirect(self, url):
        """Checks the URL and redirects if it contains 'settings'."""
        url_string = url.toString()
        if 'settings' in url_string:
            logging.info(f"Redirecting from {url_string} to https://fanvue.com/home")
            self.browser_window.setUrl(QUrl("https://fanvue.com/home"))  # Redirect to home
        else:
            logging.info(f"URL loaded: {url_string}")   




    def on_model_selected(self, index):
        selected_data = self.ui.HomeMSelector.itemData(index)

        if selected_data:
            # Assuming selected_data is a tuple (csrf_cookies, auth_token)
            csrf_cookies, auth_token = selected_data
            logging.info(f"Selected model's tokens - CSRF: {csrf_cookies}, Auth: {auth_token}")

            # Inject the tokens into the browser and log in
            self.inject_tokens_and_login(csrf_cookies, auth_token)


    def inject_tokens_and_login(self, csrf_cookies, auth_token):
        logging.info("Attempting to inject tokens for model login.")
        
        if self.profile is None:
            logging.error("Profile has already been deleted, cannot inject tokens.")
            return

        def clear_and_set_cookies(profile, csrf_cookies, auth_token):
            cookie_store = profile.cookieStore()
            
            # Clear all cookies first
            cookie_store.deleteAllCookies()
            logging.info("All cookies cleared from the browser profile.")

            # Create and set the new cookies
            domain = ".fanvue.com"
            
            csrf_cookie = QNetworkCookie("_Host-next-auth.csrf-token".encode(), csrf_cookies.encode())
            csrf_cookie.setDomain(domain)
            csrf_cookie.setPath("/")
            csrf_cookie.setSecure(True)

            auth_cookie = QNetworkCookie("fv-auth.session-token".encode(), auth_token.encode())
            auth_cookie.setDomain(domain)
            auth_cookie.setPath("/")
            auth_cookie.setSecure(True)

            # Set cookies
            cookie_store.setCookie(csrf_cookie)
            cookie_store.setCookie(auth_cookie)
            logging.info("Cookies set successfully in the browser profile.")

        try:
            clear_and_set_cookies(self.profile, csrf_cookies, auth_token)  # Pass cookies and tokens
            self.browser_window.reload()  # Reload the page after setting the cookies
            logging.info("Browser reloaded to apply cookies.")
            self.browser_window.urlChanged.connect(self.check_if_login_successful)
        except Exception as e:
            logging.error(f"Error injecting cookies: {e}")
            
    def check_if_login_successful(self, url):
        """Checks if the login was successful based on the URL."""
        url_string = url.toString()
        
        if 'fanvue.com/home' in url_string:
            logging.info("Login successful - navigated to home page!")
        else:
            logging.error(f"Login failed: URL is {url_string}. CSRF or Auth token may have been invalid.")
                
    def closeEvent(self, event):
        logging.info("Closing FSHomePage and cleaning up profile.")

        # Safely close and clean up the browser window and other components
        try:
            if self.browser_window is not None:
                self.browser_window.close()
                self.browser_window.setParent(None)
                self.browser_window.deleteLater()
                self.browser_window = None
                print("Browser window closed and cleaned up.")
        except RuntimeError:
            print("Browser window already deleted.")

        # Clean up the QWebEnginePage if it still exists
        try:
            if self.page is not None:
                self.page.deleteLater()
                self.page = None
                print("QWebEnginePage cleaned up.")
        except RuntimeError:
            print("QWebEnginePage already deleted.")

        # Clean up the QWebEngineProfile if it still exists
        try:
            if self.profile is not None:
                self.profile.clearHttpCache()
                self.profile.clearAllVisitedLinks()
                self.profile.deleteLater()
                self.profile = None
                print("QWebEngineProfile cleaned up.")
        except RuntimeError:
            print("QWebEngineProfile already deleted.")

        super().closeEvent(event)
