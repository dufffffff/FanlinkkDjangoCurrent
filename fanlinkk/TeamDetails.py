import logging
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeamDetailsaVNmhh.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from django_utils import DjangoUtils
from token_utils import TokenUtils




class Ui_TeamDetailsPopUp(QDialog):
    # Define the signal for employee_saved
    employee_saved = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        print("Ui_TeamDetailsPopUp Running")
        self.setupUi(self)
        self.setWindowTitle("Employee Information")
        self.setWindowIcon(QIcon("Icon.ico")) 
        
    
    def setupUi(self, TeamDetailsPopUp):
        if not TeamDetailsPopUp.objectName():
            TeamDetailsPopUp.setObjectName(u"TeamDetailsPopUp")

        TeamDetailsPopUp.setStyleSheet("background-color: #0A0A0A;")  # Example: dark grey background
        TeamDetailsPopUp.resize(536, 210)

        self.verticalLayout_2 = QVBoxLayout(TeamDetailsPopUp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)

        # Name Input
        self.NameLabel = QLabel(TeamDetailsPopUp)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setStyleSheet(u"color: #FFFFFF")
        self.verticalLayout.addWidget(self.NameLabel)

        self.UserNameLineEdit = QLineEdit(TeamDetailsPopUp)
        self.UserNameLineEdit.setObjectName(u"UserNameLineEdit")
        self.UserNameLineEdit.setMinimumSize(QSize(0, 25))
        self.UserNameLineEdit.setPlaceholderText("Enter name")
        self.UserNameLineEdit.setStyleSheet(u"color: #FFFFFF")
        self.verticalLayout.addWidget(self.UserNameLineEdit)

        # Email Input
        self.EmailLabel = QLabel(TeamDetailsPopUp)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setStyleSheet(u"color: #FFFFFF")
        self.verticalLayout.addWidget(self.EmailLabel)

        self.UserEmailLineEdit = QLineEdit(TeamDetailsPopUp)
        self.UserEmailLineEdit.setObjectName(u"UserEmailLineEdit")
        self.UserEmailLineEdit.setMinimumSize(QSize(0, 25))
        self.UserEmailLineEdit.setPlaceholderText("Enter email")
        self.UserEmailLineEdit.setStyleSheet(u"color: #FFFFFF")
        self.verticalLayout.addWidget(self.UserEmailLineEdit)

        # Role Dropdown
        self.RoleBox = QComboBox(TeamDetailsPopUp)
        self.RoleBox.addItem("Chatter")
        self.RoleBox.addItem("Chatter Manager")
        self.RoleBox.setObjectName(u"RoleBox")
        self.RoleBox.setMinimumSize(QSize(0, 31))
        self.RoleBox.setStyleSheet(u"color: #FFFFFF")
        self.verticalLayout.addWidget(self.RoleBox)

        self.horizontalLayout.addLayout(self.verticalLayout)

        # Team Management Section
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TeamManagementLabel = QLabel(TeamDetailsPopUp)
        self.TeamManagementLabel.setObjectName(u"TeamManagementLabel")
        self.TeamManagementLabel.setStyleSheet(u"color: #FFFFFF")
        self.verticalLayout_4.addWidget(self.TeamManagementLabel)

        self.TeamCheckboxLayout = QVBoxLayout()
        self.TeamCheckboxLayout.setObjectName(u"TeamCheckboxLayout")

        # Dynamically populate checkboxes for team members
        self.token_utils = TokenUtils()
        self.django_utils = DjangoUtils()
        user_email = self.token_utils.get_email()
        organization_id = self.django_utils.get_user_organization(user_email)

        users = self.django_utils.get_all_employees(organization_id)
        self.team_checkboxes = []
        for user in users:
            if user['role'] != 'Owner':  # Exclude the Owner
                checkbox = QCheckBox(user['email'])
                checkbox.setProperty('user_email', user['email'])
                checkbox.setEnabled(False)
                checkbox.setStyleSheet("""
                QCheckBox {
                    color: #FFFFFF;  /* Text color */
                }
                QCheckBox::indicator:checked {
                    background-color: #ef910d;  /* Color when checked */
                    border-radius: 4px;
                }
                QCheckBox::indicator:unchecked {
                    background-color: none;  /* Color when unchecked */
                }
            """ ) 
                self.TeamCheckboxLayout.addWidget(checkbox)
                self.team_checkboxes.append(checkbox)


        self.verticalLayout_4.addLayout(self.TeamCheckboxLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_4)

        # Models Section
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ModelManagementLabel = QLabel(TeamDetailsPopUp)
        self.ModelManagementLabel.setObjectName(u"ModelManagementLabel")
        self.ModelManagementLabel.setStyleSheet(u"color: #FFFFFF")
        self.verticalLayout_3.addWidget(self.ModelManagementLabel)

        self.ModelCheckboxLayout = QVBoxLayout()
        self.ModelCheckboxLayout.setObjectName(u"ModelCheckboxLayout")

        # Dynamically populate checkboxes for models from the database
        self.model_checkboxes = []
        self.populate_model_checkboxes(organization_id, user_email)

        self.verticalLayout_3.addLayout(self.ModelCheckboxLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # Buttons
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.setObjectName(u"ButtonLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.ButtonLayout.addItem(self.horizontalSpacer_2)

        self.buttonBox = QDialogButtonBox(TeamDetailsPopUp)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)
        self.buttonBox.setStyleSheet(u"color: #FFFFFF")
        self.ButtonLayout.addWidget(self.buttonBox)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.ButtonLayout.addItem(self.horizontalSpacer)
        self.verticalLayout_2.addLayout(self.ButtonLayout)

        QMetaObject.connectSlotsByName(TeamDetailsPopUp)

        # Connect Save and Cancel buttons
        self.buttonBox.accepted.connect(self.save_changes)
        self.buttonBox.rejected.connect(TeamDetailsPopUp.reject)

        # Connect RoleBox to update checkbox states
        self.RoleBox.currentTextChanged.connect(self.update_checkbox_states)

    def save_changes(self):
        """Handle saving the new employee and emit the employee_saved signal."""
        user_name = self.UserNameLineEdit.text()
        user_email = self.UserEmailLineEdit.text()
        user_role = self.RoleBox.currentText()

        # Retrieve the selected models
        selected_models = []
        for checkbox in self.model_checkboxes:
            if checkbox.isChecked():
                selected_models.append(checkbox.property('model_email'))

        # Retrieve the selected employees
        selected_employees = []
        for checkbox in self.team_checkboxes:
            if checkbox.isChecked():
                selected_employees.append(checkbox.property('user_id'))

        # Get or create user_id for the user
        current_user_id = self.get_current_user_id(user_email)

        if current_user_id:
            self.save_user_and_models(user_name, user_email, user_role, selected_models, current_user_id)
            self.assign_employees_to_user(current_user_id, selected_employees)
            logging.info(f"Changes saved successfully for user {user_name}")

            # Emit the employee_saved signal to notify the table to update
            self.employee_saved.emit()

            # Accept the dialog to close it
            self.accept()
        else:
            logging.error("Failed to get or create user.")

    def get_current_user_id(self, email):
        """Fetch the user ID based on the email. If the user doesn't exist, create a new one."""
        existing_user = self.django_utils.get_user_by_email(email)
        if existing_user:
            logging.info(f"User {email} found with ID: {existing_user['id']}")
            return existing_user['id']
        else:
            logging.info(f"User {email} not found, inserting new user.")
            new_user_id = self.django_utils.insert_user(self.UserNameLineEdit.text(), email, self.RoleBox.currentText(), 'default_password')
            if new_user_id:
                logging.info(f"New user created with ID: {new_user_id}")
                return new_user_id
            else:
                logging.error(f"Failed to create new user with email: {email}")
                return None

    def save_user_and_models(self, name, email, role, model_ids, user_id=None):
        """Save user and associate selected models with the user."""
        
        if not user_id:
            logging.error(f"No valid user ID for {name} ({email}). Aborting save.")
            return

        # Update user data (name, email, role)
        self.django_utils.update_user(user_id, name=name, email=email, role=role)
        logging.info(f"User {user_id} updated with new data: {name}, {email}, {role}")

        # Clear the existing models for this user
        self.django_utils.clear_models_for_user(user_id)

        # Assign the selected models to the user
        for model_id in model_ids:
            self.django_utils.assign_model_to_user(model_id, user_id)
        logging.info(f"Models assigned successfully to user {user_id}")

    def assign_employees_to_user(self, manager_id, selected_employees):
        """Assign the selected employees to the manager (user)."""
        # Clear existing employees assigned to this manager
        self.django_utils.clear_employees_for_user(manager_id)

        # Assign the selected employees to the manager
        for employee_id in selected_employees:
            self.django_utils.assign_employee_to_user(manager_id, employee_id)
        logging.info(f"Assigned employees {selected_employees} to manager {manager_id}")

    def update_checkbox_states(self):
        """Enable/disable employee checkboxes based on the selected role."""
        selected_role = self.RoleBox.currentText()

        if selected_role == "Chatter Manager":
            for checkbox in self.team_checkboxes:
                checkbox.setEnabled(True)  # Enable if Chatter Manager
        else:
            for checkbox in self.team_checkboxes:
                checkbox.setEnabled(False)  # Disable if Chatter

    def populate_model_checkboxes(self, org_id, user_email):
        """Fetch models assigned to the user and update the checkboxes."""
        # Fetch models from the organisation
        models = self.django_utils.get_models_for_organisation(org_id)
        print(f"Fetched models for organisation {org_id}: {models}")
        
        # Fetch assigned models for the user
        assigned_models = self.django_utils.get_models_for_user(user_email)
        print(f"Assigned models for user {user_email}: {assigned_models}")

        # Clear existing checkboxes
        for checkbox in self.model_checkboxes:
            self.ModelCheckboxLayout.removeWidget(checkbox)
            checkbox.deleteLater()
        self.model_checkboxes.clear()

        if not models:
            print(f"No models found for organisation {org_id}")
            models = []  # Handle case where no models are returned

        # Repopulate with all models and check the ones assigned to the user
        for model in models:
            checkbox = QCheckBox(model['name'])
            checkbox.setProperty('model_email', model['email'])

            # Check if the model is assigned to the user
            is_checked = any(m['email'] == model['email'] for m in assigned_models)
            checkbox.setChecked(is_checked)
            
            checkbox.setStyleSheet("""
                QCheckBox {
                    color: #FFFFFF;  /* Text color */
                }
                QCheckBox::indicator:checked {
                    background-color: #ef910d;  /* Color when checked */
                    border-radius: 4px;
                }
                QCheckBox::indicator:unchecked {
                    background-color: none;  /* Color when unchecked */
                }
            """)

            # Add checkbox to layout
            self.ModelCheckboxLayout.addWidget(checkbox)
            self.model_checkboxes.append(checkbox)

    def retranslateUi(self, TeamDetailsPopUp):
        TeamDetailsPopUp.setWindowTitle(QCoreApplication.translate("TeamDetailsPopUp", u"Add New Employee", None))
        self.NameLabel.setText(QCoreApplication.translate("TeamDetailsPopUp", u"Name:", None))
        self.EmailLabel.setText(QCoreApplication.translate("TeamDetailsPopUp", u"Email:", None))
        self.TeamManagementLabel.setText(QCoreApplication.translate("TeamDetailsPopUp", u"Team Under Management", None))
        self.ModelManagementLabel.setText(QCoreApplication.translate("TeamDetailsPopUp", u"Models Under Management", None))