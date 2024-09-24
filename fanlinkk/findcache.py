
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import QVBoxLayout, QPushButton
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
import sys
import logging
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class CachePathFinder(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Press the button to find QtWebEngine Cache Path", self)
        layout.addWidget(self.label)

        btn = QPushButton("Find Cache Path", self)
        btn.clicked.connect(self.show_cache_path)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.setWindowTitle('QtWebEngine Cache Path Finder')
        self.show()

    def show_cache_path(self):
        # Get the default profile cache path
        profile = QWebEngineProfile.defaultProfile()
        cache_path = profile.cachePath()

        # Show the cache path in the label
        self.label.setText(f"Cache Path: {cache_path}")

def main():
    app = QApplication(sys.argv)
    window = CachePathFinder()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
