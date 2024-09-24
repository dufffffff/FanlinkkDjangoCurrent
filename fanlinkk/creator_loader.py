import logging
import os
import sys
from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QDialog, QApplication
from sqlalchemy import select, update
from db_utils import Session, models  # Assuming db_utils contains your SQLAlchemy setup
from ModelDetails import ModelDetailsDialog  # Replace with the actual name of the file
from PySide6.QtGui import QFont, QFontDatabase, QColor , QBrush, QIcon
from PySide6.QtCore import Qt



image_paths = {}  # Global dictionary to store image paths by row number

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)





def load_creators(table_widget, main_window):
    """Load creators from the database and populate the QTableWidget."""
    placeholder_image_path = "images/user.svg"
    session = Session()  # Create a new session
    
    # Set the Futura font with a larger size (e.g., 14 points)
    futura_font = QFont("Futura PT")
    futura_font.setPointSize(12)  # Set the font size to 14 points (adjust as needed)
      # Set the Futura font for the status (12 points)
    futura_font_status = QFont("Futura PT")
    futura_font_status.setPointSize(12)  # Set the font size for the status to 12 points
    background_color = QColor("#292929")

    try:
        query = select(models.c.name, models.c.image_path).order_by(models.c.name)
        result = session.execute(query).fetchall()

        # Clear existing rows in the table
        table_widget.setRowCount(0)
        
        # Set the number of rows in the table based on the number of creators
        table_widget.setRowCount(len(result))

        for row_number, row_data in enumerate(result):
            logging.info(f"Loading model: {row_data[0]}")  # Log model name being loaded

            # Create a QTableWidgetItem for the model name
            name_item = QTableWidgetItem(row_data[0])  # row_data[0] is the name
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  # Make it non-editable
            name_item.setFont(futura_font)  # Apply Futura PT font to the name item
            name_item.setBackground(QBrush(background_color))  # Set background color

            name_item.setTextAlignment(Qt.AlignCenter)
            
            table_widget.setItem(row_number, 0, name_item)

            # Create a QTableWidgetItem for the status
            status_item = QTableWidgetItem("Active")
            status_item.setFlags(status_item.flags() & ~Qt.ItemIsEditable)  # Make it non-editable
            status_item.setFont(futura_font_status)  # Apply Futura PT font to the status item
            status_item.setTextAlignment(Qt.AlignCenter)
            status_item.setBackground(QBrush(background_color))  # Set background color

            table_widget.setItem(row_number, 1, status_item)

            # Get the image path or use placeholder if not available
            image_path = row_data[1] or placeholder_image_path  # Use placeholder if no image path
            if not os.path.exists(image_path):
                logging.warning(f"Image path not found for model {row_data[0]}, using placeholder.")  # Log missing image path
                image_path = placeholder_image_path  # Fallback to placeholder if path is invalid
            logging.warning(f"Image path === {placeholder_image_path}") 
            image_paths[row_number] = image_path  # Store the image path in the dictionary

            # Create Edit/Delete button with custom style
            edit_button = QPushButton("Edit")
            edit_button.setMinimumSize(200,40)
            edit_button.setMaximumSize(200,80)

            edit_button.setFont(futura_font)  # Apply Futura PT font to the button
            edit_button.setStyleSheet("""
                        QPushButton {
                            border-radius: 14px;  /* Match the rounded corners */
                            background-color: #ffffff;  /* Default background color like LinkAccountButton */
                            color: #373737;  /* Default text color */
                            padding: 6px;  /* Adjusted padding */
                        }
                        QPushButton:hover {
                            background-color: #373737;  /* Inverted background on hover */
                            color: #ffffff;  /* Inverted text color on hover */
                        }
                        QPushButton:pressed {
                            background-color: #ffffff;  /* Same as normal state */
                            color: #373737;  /* Same text color */
                        }
                    """)
            
            edit_button.clicked.connect(lambda _, r=row_number: handle_button_click(r, table_widget, main_window))
            button_widget = QWidget()
            button_widget.setStyleSheet("""
                border: none;  /* Remove border if needed */
            """)   
            button_layout = QHBoxLayout(button_widget)
            button_layout.addWidget(edit_button)
            button_layout.setAlignment(Qt.AlignCenter)  # Center the button
            button_layout.setContentsMargins(0, 0, 0, 0)  # Remove any margins
            button_widget.setLayout(button_layout)
            table_widget.setCellWidget(row_number, 2, button_widget)

        logging.info("Creators loaded successfully into the table.")

        # After loading the creators, adjust the table height dynamically
        adjust_manage_creators_table_height(table_widget)

    except Exception as e:
        logging.error(f"An error occurred while loading creators: {e}")
    finally:
        session.close()  # Ensure the session is closed


def handle_button_click(row_number, table_widget, main_window):
    """Handle the button click event for the specified row."""
    logging.info(f"Button clicked in row {row_number}")

    # Retrieve the current image path from the dictionary
    image_path = image_paths.get(row_number, None)

    # Create an instance of the dialog with the row number and table widget
    dialog = ModelDetailsDialog(row_number, table_widget, main_window)
    dialog.setWindowTitle("Edit Creator")
    dialog.setWindowIcon(QIcon("Icon.ico"))
    
    # Populate the dialog with data from the selected row
    model_name_item = table_widget.item(row_number, 0)  # Assuming the model name is in the first column
    if model_name_item:
        model_name = model_name_item.text()
        logging.info(f"Model name retrieved: {model_name}")
        dialog.ui.ModelNameLineEdit.setText(model_name)
    else:
        logging.error(f"Model name not found for row {row_number}")

    # Set the image in the dialog if image_path exists
    if image_path:
        logging.info(f"Setting image for model in row {row_number}: {image_path}")
        dialog.set_image(image_path)
    else:
        logging.error(f"Image path is missing for row {row_number}")
    
    # Connect the save signal to the save_changes function
    dialog.save_clicked.connect(lambda new_name, new_image_path: save_changes(row_number, new_name, new_image_path, table_widget, main_window))
    
    # Show the dialog
    logging.info(f"Opening ModelDetailsDialog for row {row_number}")
    dialog.exec_()


def save_changes(row_number, new_name, new_image_path, table_widget, main_window):
    """Save the changes made in the dialog to the table widget and database."""
    old_name = table_widget.item(row_number, 0).text()
    logging.info(f"Saving changes for model: {old_name} -> New name: {new_name}")

    # Update the table widget with the new name
    table_widget.item(row_number, 0).setText(new_name)

    # Update the dictionary with the new image path
    image_paths[row_number] = new_image_path

    # Update the database
    session = Session()
    try:
        stmt = (
            update(models).
            where(models.c.name == old_name).
            values(name=new_name, image_path=new_image_path)
        )
        session.execute(stmt)
        session.commit()
        logging.info(f"Model name updated from {old_name} to {new_name} with image path {new_image_path}")
    except Exception as e:
        session.rollback()
        logging.error(f"An error occurred while updating the model name and image path: {e}")
    finally:
        session.close()

    # Refresh the table to show the changes
    logging.info("Refreshing creators table and checkboxes after model changes.")
    main_window.load_creators_into_table()
    main_window.load_model_checkboxes()
    main_window.enable_checkboxes(None)

    logging.info("Checkboxes updated and enabled after model changes.")


def adjust_manage_creators_table_height(table_widget):
    """Adjust the height of the ManageCreators table based on the number of rows."""
    row_count = table_widget.rowCount()

    if row_count == 0:
        return

    # Calculate the total height: sum of row heights, header height, and margins
    total_height = 0
    for row in range(row_count):
        total_height += table_widget.rowHeight(row)
    
    total_height += table_widget.horizontalHeader().height()  # Add header height
    total_height += table_widget.frameWidth() * 2  # Add frame padding
    
    # Set the table height dynamically based on the content
    table_widget.setMaximumHeight(total_height)
    table_widget.setMinimumHeight(total_height)