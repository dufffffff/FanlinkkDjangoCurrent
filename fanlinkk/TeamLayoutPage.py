import logging
import requests
from django_utils import DjangoUtils
from token_utils import TokenUtils

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeamLayoutPage.ui'
## Created by: Qt User Interface Compiler version 6.7.2
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage, QKeySequence,
                           QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QDialog)

from TeamDetails import Ui_TeamDetailsPopUp  # Assuming this is in a separate file

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(776, 875)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(2, -1, 10, -1)

        # Title Label
        self.label_64 = QLabel(Form)
        self.label_64.setObjectName(u"label_64")
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(24)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet(u"color:#f5f5f5;")
        self.horizontalLayout_38.addWidget(self.label_64)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_38.addItem(self.horizontalSpacer_37)

        # Add Employee Button
        self.AddEmployeeButton = QPushButton(Form)
        self.AddEmployeeButton.setObjectName(u"AddEmployeeButton")
        self.AddEmployeeButton.setMinimumSize(QSize(100, 42))
        font1 = QFont()
        font1.setFamilies([u"Futura PT"])
        font1.setPointSize(11)
        self.AddEmployeeButton.setFont(font1)
        self.AddEmployeeButton.setCheckable(False)
        self.AddEmployeeButton.setFlat(True)
        self.horizontalLayout_38.addWidget(self.AddEmployeeButton)

        self.verticalLayout_48.addLayout(self.horizontalLayout_38)

        # Employees Table
        self.EmployeesTableTeamLayout = QTableWidget(Form)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.EmployeesTableTeamLayout.setSizePolicy(sizePolicy)

        if self.EmployeesTableTeamLayout.columnCount() < 5:
            self.EmployeesTableTeamLayout.setColumnCount(5)
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2)
        self.EmployeesTableTeamLayout.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2)
        self.EmployeesTableTeamLayout.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2)
        self.EmployeesTableTeamLayout.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2)
        self.EmployeesTableTeamLayout.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2)
        self.EmployeesTableTeamLayout.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.EmployeesTableTeamLayout.setObjectName(u"EmployeesTableTeamLayout")
        font3 = QFont()
        font3.setFamilies([u"Futura PT"])
        self.EmployeesTableTeamLayout.setFont(font3)

        header = self.EmployeesTableTeamLayout.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.EmployeesTableTeamLayout.horizontalHeader().setDefaultSectionSize(400)
        self.EmployeesTableTeamLayout.verticalHeader().setDefaultSectionSize(240)
        self.adjust_table_height()


        self.verticalLayout_48.addWidget(self.EmployeesTableTeamLayout)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_48.addItem(self.verticalSpacer)

        self.verticalLayout.addLayout(self.verticalLayout_48)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)


    def adjust_table_height(self):
        """Adjust the height of the table based on the number of rows."""
        row_count = self.EmployeesTableTeamLayout.rowCount()

        if row_count == 0:
            return

        # Calculate the total height: sum of row heights, header height, and margins
        total_height = 0
        for row in range(row_count):
            total_height += self.EmployeesTableTeamLayout.rowHeight(row)
        
        total_height += self.EmployeesTableTeamLayout.horizontalHeader().height()  # Add header height
        total_height += self.EmployeesTableTeamLayout.frameWidth() * 2  # Add frame padding
        
        # Set the table height dynamically based on the content
        self.EmployeesTableTeamLayout.setMaximumHeight(total_height)
        self.EmployeesTableTeamLayout.setMinimumHeight(total_height)





    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"Team Layout", None))
        self.AddEmployeeButton.setText(QCoreApplication.translate("Form", u"Add New Employee", None))
        ___qtablewidgetitem = self.EmployeesTableTeamLayout.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Team Member", None))
        ___qtablewidgetitem1 = self.EmployeesTableTeamLayout.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Role", None))
        ___qtablewidgetitem2 = self.EmployeesTableTeamLayout.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Employees Under Management", None))
        ___qtablewidgetitem3 = self.EmployeesTableTeamLayout.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Models Under Management", None))
        ___qtablewidgetitem4 = self.EmployeesTableTeamLayout.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Edit", None))


class TeamLayout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.django_utils = DjangoUtils()
        self.token_utils = TokenUtils()

        # Set font and style for the table similar to ManageCreators table
        font = QFont()
        font.setFamilies([u"Futura PT"])
        font.setPointSize(13)  # Set default font size for the table items

        # Apply font to table headers and items
        self.ui.EmployeesTableTeamLayout.setFont(font)
        self.ui.EmployeesTableTeamLayout.setStyleSheet("""
            background-color: #373737;
            color: white;
        """)

        # Set header properties for larger text in specific columns
        self.ui.EmployeesTableTeamLayout.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #373737;
                color: white;
                padding: 4px;
            }
        """)

        # Set column-specific fonts for headers
        header_font_large = QFont("Futura PT", 16)  # Larger font for specific columns
        header_font_small = QFont("Futura PT", 12)  # Smaller font for Name, Role, Edit columns

        # Set header font sizes and text
        self.set_header_font(0, header_font_small, "Team Member")
        self.set_header_font(1, header_font_small, "Role")
        self.set_header_font(2, header_font_large, "Employees Under Management")
        self.set_header_font(3, header_font_large, "Models Under Management")
        self.set_header_font(4, header_font_small, "Edit")

        # Adjust column sizes: set the "Edit" button to stretch a little more
        header = self.ui.EmployeesTableTeamLayout.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # Name
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Role
        header.setSectionResizeMode(2, QHeaderView.Stretch)           # Employees Under Management
        header.setSectionResizeMode(3, QHeaderView.Stretch)           # Models Under Management
        header.setSectionResizeMode(4, QHeaderView.Stretch)           # Edit (give it more space)

        # Adjust row and header height 
        self.ui.EmployeesTableTeamLayout.verticalHeader().setDefaultSectionSize(62)

        # Populate the table with the styled data
        self.populate_team_table()
        self.ui.AddEmployeeButton.clicked.connect(self.open_add_employee_dialog)

    def open_add_employee_dialog(self):
        dialog = Ui_TeamDetailsPopUp()

        # Connect the employee_saved signal to the table refresh
        dialog.employee_saved.connect(self.populate_team_table)

        if dialog.exec_() == QDialog.Accepted:
            self.populate_team_table()  # Ensure the table is refreshed

    def add_new_employee(self, name, email, role, selected_employees):
        user_id = self.django_utils.insert_user(name=name, email=email, role=role, password='default_password')
        for employee_id in selected_employees:
            self.django_utils.assign_employee_to_user(user_id, employee_id)

    def set_header_font(self, column, font, text):
        """Helper function to set font and text for a specific table header."""
        item = QTableWidgetItem(text)
        item.setFont(font)
        self.ui.EmployeesTableTeamLayout.setHorizontalHeaderItem(column, item)




    def populate_team_table(self):
        # Fetch the user's organization
        user_email = self.token_utils.get_email()
        organization_id = self.django_utils.get_user_organization(user_email)

        # Fetch users from the same organization
        #print('Trying to get users for organization:', organization_id)
        users = self.django_utils.get_all_employees(organization_id)  #populate the table
        #print(f"THESE ARE THE USERS CUNT {users}")
        if not users:
            logging.error(f"No users found for organization {organization_id}.")
            return

        # Clear existing data in the table
        self.ui.EmployeesTableTeamLayout.setRowCount(0)

        # Add rows dynamically based on fetched users
        for index, user in enumerate(users):
            self.ui.EmployeesTableTeamLayout.insertRow(index)

            # Add data for each column
            name_item = QTableWidgetItem(user['email']) #change to name
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  # Make non-editable
            role_item = QTableWidgetItem(user.get('role', "Role"))
            role_item.setFlags(role_item.flags() & ~Qt.ItemIsEditable)  # Make non-editable

            # Set fonts for table items
            name_item.setFont(QFont("Futura PT", 13))
            role_item.setFont(QFont("Futura PT", 13))

            # Fetch employees and models for the user within the organization
            employees = self.django_utils.get_subordinates_for_supervisor(user['email']) # populate column for users under user 
            models = self.django_utils.get_models_for_user(user['email'])
            print(employees)
            print(models)
            # Add employees under management
            under_management_item = QTableWidgetItem(", ".join([emp['user__email'] for emp in employees]) if employees else "None")
            under_management_item.setFlags(under_management_item.flags() & ~Qt.ItemIsEditable)  # Make non-editable
            under_management_item.setFont(QFont("Futura PT", 13))

            # Add models under management
            models_item = QTableWidgetItem(", ".join([model['model__name'] for model in models]) if models else "None")
            models_item.setFlags(models_item.flags() & ~Qt.ItemIsEditable)  # Make non-editable
            models_item.setFont(QFont("Futura PT", 13))

            # Create the Edit button
            edit_button = QPushButton("Edit")
            edit_button.setFont(QFont("Futura PT", 12))
            edit_button.setStyleSheet("""
                QPushButton {
                    background-color: #373737;
                    color: white;
                    border: none;
                    padding: 5px;
                    min-width: 100px;
                }
                QPushButton:hover {
                    background-color: #141414;
                }
                QPushButton:pressed {
                    background-color: #373737;
                }
            """)
            edit_button.clicked.connect(lambda _, user_email=user['email']: self.open_edit_dialog(user_email))

            # Insert items into the table
            self.ui.EmployeesTableTeamLayout.setItem(index, 0, name_item)
            self.ui.EmployeesTableTeamLayout.setItem(index, 1, role_item)
            self.ui.EmployeesTableTeamLayout.setItem(index, 2, under_management_item)
            self.ui.EmployeesTableTeamLayout.setItem(index, 3, models_item)
            self.ui.EmployeesTableTeamLayout.setCellWidget(index, 4, edit_button)

        # Adjust table height dynamically after populating
        self.ui.adjust_table_height()

            
    def open_edit_dialog(self, user_email):
        """Opens the TeamDetailsPopUp dialog with pre-filled information for editing a user."""
        # Fetch user details from the database
        user = self.django_utils.get_user_by_email(user_email)
        employees = self.django_utils.get_employees_for_user(user_email)
        models = self.django_utils.get_models_for_user(user_email)  # Fetch models assigned to this user
        logging.info(f"Editing user: {user} with employees: {employees} and models: {models}")

        # Open the dialog
        dialog = Ui_TeamDetailsPopUp()

        # Pre-fill user information in the dialog
        dialog.UserNameLineEdit.setText(user['email'])
        dialog.UserEmailLineEdit.setText(user['name'])
        role_index = dialog.RoleBox.findText(user['role'], Qt.MatchFixedString)
        if role_index >= 0:
            dialog.RoleBox.setCurrentIndex(role_index)

        # Pre-check the employee checkboxes
        for checkbox in dialog.team_checkboxes:
            if checkbox.property('user_email') in [emp['email'] for emp in employees]:
                checkbox.setChecked(True)

        # Pre-check the model checkboxes (only those assigned to the user)
        for checkbox in dialog.model_checkboxes:
            if checkbox.property('email') in [model['email'] for model in models]:
                checkbox.setChecked(True)
            else:
                checkbox.setChecked(False)  # Uncheck if not assigned to this user

        # Enable or disable checkboxes based on the role
        dialog.update_checkbox_states()

        # Connect the employee_saved signal to refresh the table after editing
        dialog.employee_saved.connect(self.populate_team_table)

        # If the user saves changes, update the user information
        if dialog.exec_() == QDialog.Accepted:
            name = dialog.UserNameLineEdit.text()
            email = dialog.UserEmailLineEdit.text()
            role = dialog.RoleBox.currentText()

            # Get selected employees
            selected_employees = []
            for checkbox in dialog.team_checkboxes:
                if checkbox.isChecked():
                    selected_employees.append(checkbox.property('user_id'))

            # Get selected models
            selected_models = []
            for checkbox in dialog.model_checkboxes:
                if checkbox.isChecked():
                    selected_models.append(checkbox.property('model_id'))

            # Update the user, their employees, and their models
            self.update_user(user_email, name, email, role, selected_employees, selected_models)

            # Refresh the team table after editing an employee
            self.populate_team_table()




    def update_user(self, user_id, name, email, role, selected_employees, selected_models):
        """Updates the user details, reassigns their employees, and assigns models."""
        # Update user details
        self.django_utils.update_user(user_id, name=name, email=email, role=role)

        # Reassign employees
        self.django_utils.clear_employees_for_user(email)
        for employee_email in selected_employees:
            self.django_utils.assign_employee_to_user(email, employee_email)

        # Reassign models
        self.django_utils.clear_models_for_user(email)
        for model_email in selected_models:
            self.django_utils.assign_model_to_user(model_email, email)

