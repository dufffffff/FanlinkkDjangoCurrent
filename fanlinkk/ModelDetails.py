from db_utils import remove_model_by_id_or_email, get_model_email_by_name
import logging 

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerxCLAbW.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Signal, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget, QFileDialog, QGridLayout)

import Resources_rc

class Ui_ModelDetailsPopUp(object):
    def setupUi(self, ModelDetailsPopUp):
        if not ModelDetailsPopUp.objectName():
            ModelDetailsPopUp.setObjectName(u"ModelDetailsPopUp")
        ModelDetailsPopUp.resize(394, 133)
        ModelDetailsPopUp.setStyleSheet(u"background-color:#141414")
        self.gridLayout = QGridLayout(ModelDetailsPopUp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ModelImageButton = QPushButton(ModelDetailsPopUp)
        self.ModelImageButton.setObjectName(u"ModelImageButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModelImageButton.sizePolicy().hasHeightForWidth())
        self.ModelImageButton.setSizePolicy(sizePolicy)
        self.ModelImageButton.setMinimumSize(QSize(64, 64))
        self.ModelImageButton.setMaximumSize(QSize(64, 64))
        self.ModelImageButton.setStyleSheet(u"    border-radius: 32px; \n"
"    background-color: #373737; \n"
"    padding: 4px; ")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/user (4).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ModelImageButton.setIcon(icon)
        self.ModelImageButton.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.ModelImageButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.UploadImageLabel = QLabel(ModelDetailsPopUp)
        self.UploadImageLabel.setObjectName(u"UploadImageLabel")
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(10)
        self.UploadImageLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.UploadImageLabel)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 12, -1, 6)
        self.label = QLabel(ModelDetailsPopUp)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.ModelNameLineEdit = QLineEdit(ModelDetailsPopUp)
        self.ModelNameLineEdit.setObjectName(u"ModelNameLineEdit")
        self.ModelNameLineEdit.setMinimumSize(QSize(0, 25))
        self.ModelNameLineEdit.setFont(font)
        self.ModelNameLineEdit.setStyleSheet(u"background-color:#373737")

        self.verticalLayout.addWidget(self.ModelNameLineEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(ModelDetailsPopUp)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font1)
        self.buttonBox.setStyleSheet(u"    border-radius: 10px; \n"
"    background-color: #ffffff; \n"
"    color: #373737; \n"
"    padding: 8px; ")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Discard|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.retranslateUi(ModelDetailsPopUp)
        self.buttonBox.accepted.connect(ModelDetailsPopUp.accept)
        self.buttonBox.rejected.connect(ModelDetailsPopUp.reject)

        QMetaObject.connectSlotsByName(ModelDetailsPopUp)
    # setupUi

    def retranslateUi(self, ModelDetailsPopUp):
        ModelDetailsPopUp.setWindowTitle(QCoreApplication.translate("ModelDetailsPopUp", u"Dialog", None))
        self.ModelImageButton.setText("")
        self.UploadImageLabel.setText(QCoreApplication.translate("ModelDetailsPopUp", u"Upload Image", None))
        self.label.setText(QCoreApplication.translate("ModelDetailsPopUp", u"Name:", None))
    # retranslateUi


class ModelDetailsDialog(QDialog):
    save_clicked = Signal(str, str)  # Emit both name and image path as two arguments

    def __init__(self, row_number, table_widget, main_window=None, parent=None):
        super(ModelDetailsDialog, self).__init__(parent)
        self.ui = Ui_ModelDetailsPopUp()
        self.ui.setupUi(self)
        self.row_number = row_number
        self.table_widget = table_widget
        self.main_window = main_window  # Reference to the main window (or controller class)

        logging.info(f"Initializing ModelDetailsDialog for row: {row_number}")

        # Get the model's name from the table (assuming model name is stored in a column)
        self.model_name = table_widget.item(row_number, 0).text()  # Update column index for name
        logging.info(f"Retrieved model name: {self.model_name}")

        # Retrieve the model email by name from the database
        self.model_email = get_model_email_by_name(self.model_name)

        if self.model_email:
            logging.info(f"Model email retrieved: {self.model_email}")
        else:
            logging.error(f"Failed to retrieve email for model: {self.model_name}")

        self.image_path = None  # Initialize the image path

        # Connect the ModelImageButton to open a file dialog
        self.ui.ModelImageButton.clicked.connect(self.select_image)

        # Connect the save button to emit the save_clicked signal
        self.ui.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.on_save)

        # Connect the discard button to handle model deletion
        self.ui.buttonBox.button(QDialogButtonBox.Discard).clicked.connect(self.on_discard)

    def select_image(self):
        """Open a file dialog to select a PNG image and set it as the button's icon."""
        logging.info("Opening file dialog to select image.")
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "images (*.png *.svg)")
        if file_path:
            logging.info(f"Image selected: {file_path}")
            self.set_image(file_path)
        else:
            logging.warning("No image selected.")

    def set_image(self, image_path):
        """Set the button icon to the provided image path."""
        if image_path:
            logging.info(f"Setting image: {image_path}")
            self.image_path = image_path  # Save the image path
            pixmap = QPixmap(image_path)
            icon = QIcon(pixmap)
            self.ui.ModelImageButton.setIcon(icon)
            self.ui.ModelImageButton.setIconSize(self.ui.ModelImageButton.size())
        else:
            logging.warning("Image path is empty. No image set.")

    def on_save(self):
        """Emit the save_clicked signal with the new name and image path."""
        new_name = self.ui.ModelNameLineEdit.text()
        logging.info(f"Save clicked. New name: {new_name}, Image path: {self.image_path}")
        self.save_clicked.emit(new_name, self.image_path)  # Emit the new name and image path
        self.accept()  # Close the dialog

    def on_discard(self):
        """Handle model removal when the discard button is pressed."""
        logging.info("Discard button clicked.")
        if self.model_email:
            logging.info(f"Attempting to remove model with email: {self.model_email}")
            success = remove_model_by_id_or_email(model_email=self.model_email)
            if success:
                logging.info(f"Model {self.model_email} successfully removed.")
                
                # After successful removal, call the methods in the main window
                if self.main_window:
                    logging.info("Calling load_creators_into_table and load_model_checkboxes.")
                    self.main_window.load_creators_into_table()
                    self.main_window.load_model_checkboxes()
                else:
                    logging.error("Main window reference is missing. Unable to reload creators or model checkboxes.")
            else:
                logging.error(f"Failed to remove model {self.model_email}.")
        else:
            logging.error(f"Model email is missing for model: {self.model_name}")
        
        self.reject()  # Close the dialog after attempting to remove


