# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModelDetailsQwrHyr.ui'
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
    QHBoxLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ModelDetailsPopUp(object):
    def setupUi(self, ModelDetailsPopUp):
        if not ModelDetailsPopUp.objectName():
            ModelDetailsPopUp.setObjectName(u"ModelDetailsPopUp")
        ModelDetailsPopUp.resize(491, 126)
        self.horizontalLayout_2 = QHBoxLayout(ModelDetailsPopUp)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ModelImageButton = QPushButton(ModelDetailsPopUp)
        self.ModelImageButton.setObjectName(u"ModelImageButton")
        self.ModelImageButton.setMinimumSize(QSize(80, 80))
        self.ModelImageButton.setStyleSheet(u"")
        self.ModelImageButton.setFlat(False)

        self.horizontalLayout.addWidget(self.ModelImageButton)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ModelNameLineEdit = QLineEdit(ModelDetailsPopUp)
        self.ModelNameLineEdit.setObjectName(u"ModelNameLineEdit")
        self.ModelNameLineEdit.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.ModelNameLineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(ModelDetailsPopUp)
        self.buttonBox.setObjectName(u"buttonBox")
        font = QFont()
        font.setFamilies([u"Futura PT Book"])
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Discard|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(ModelDetailsPopUp)
        self.buttonBox.accepted.connect(ModelDetailsPopUp.accept)
        self.buttonBox.rejected.connect(ModelDetailsPopUp.reject)

        QMetaObject.connectSlotsByName(ModelDetailsPopUp)
    # setupUi

    def retranslateUi(self, ModelDetailsPopUp):
        ModelDetailsPopUp.setWindowTitle(QCoreApplication.translate("ModelDetailsPopUp", u"Dialog", None))
        self.ModelImageButton.setText(QCoreApplication.translate("ModelDetailsPopUp", u"Add Image", None))
    # retranslateUi

