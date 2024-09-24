# Modify brows.py to allow URL setting
import sys
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineHttpRequest
from PySide6.QtNetwork import QNetworkCookie
import os
# Force software rendering
os.environ["QT_QUICK_BACKEND"] = "software"
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"

class BrowserWindow(QMainWindow):
    def __init__(self, csrf_token, jwt_token, url):
        super().__init__()

        self.setWindowTitle("Qt Web Browser")
        self.resize(1000, 1000)

        # Store the tokens and URL as instance attributes
        self.csrf_token = csrf_token
        self.jwt_token = jwt_token
        self.url = url

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.browser = QWebEngineView()
        profile = QWebEngineProfile.defaultProfile()
        cookie_store = profile.cookieStore()

        # Set JWT and CSRF cookies
        csrf_cookie = QNetworkCookie("__Host-next-auth.csrf-token".encode(), csrf_token.encode())
        csrf_cookie.setDomain(".fanvue.com")
        csrf_cookie.setPath("/")
        cookie_store.setCookie(csrf_cookie, QUrl(self.url))

        jwt_cookie = QNetworkCookie("fv-auth.session-token".encode(), jwt_token.encode())
        jwt_cookie.setDomain(".fanvue.com")
        jwt_cookie.setPath("/")
        cookie_store.setCookie(jwt_cookie, QUrl(self.url))

        layout.addWidget(self.browser)

        # Set a timer to load the page after cookies are set
        QTimer.singleShot(1000, self.load_homepage)

    def load_homepage(self):
        # Load the homepage and set Authorization header
        profile = self.browser.page().profile()
        request = QWebEngineHttpRequest(QUrl(self.url))
        request.setHeader(b'Authorization', f'Bearer {self.jwt_token}'.encode())
        self.browser.page().load(request)
        
if __name__ == "__main__":
    csrf_token = "your_csrf_token"
    jwt_token = "your_jwt_token"
    url = "https://www.fanvue.com/home"  # Default URL

    app = QApplication(sys.argv)
    window = BrowserWindow(csrf_token, jwt_token, url)
    window.show()
    sys.exit(app.exec())
