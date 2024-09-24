import os
import logging
from sqlalchemy import create_engine, Table, Column, Integer, String, Text, MetaData, ForeignKey, func, update, select, Boolean, DateTime, insert
from sqlalchemy.orm import sessionmaker
from PySide6.QtCore import QObject, QThread, Signal, Slot
import sqlite3
from collections import defaultdict

active_user_email = None  # Global variable to store active user
def set_active_user(email):
    global active_user_email
    active_user_email = email
    logging.info(f"Active user set to {email}")

def get_active_user():
    global active_user_email
    if active_user_email:
        return active_user_email
    else:
        logging.warning("No active user set.")
        return None
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path for the SQLite database
db_path = os.path.join(current_dir, 'my_database.db')

# SQLite database setup
DATABASE_URL = f'sqlite:///{db_path}'  # SQLite URL with the path to the database
logging.info(f"Using database at: {db_path}")

# Database connection and session setup
engine = create_engine(DATABASE_URL, echo=False)
metadata = MetaData()
Session = sessionmaker(bind=engine)

# Define the users table
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(100), nullable=False),
              Column('email', String(100), unique=True, nullable=False),
              Column('password', String(255), nullable=True),  # Store plaintext for now (consider hashing later)
              Column('role', String(50), nullable=False),  # Role of the user (e.g., "manager", "employee")
)

user_models = Table('user_models', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
                    Column('model_id', Integer, ForeignKey('models.id'), nullable=False)
)

user_employees = Table('user_employees', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
                       Column('employee_id', Integer, ForeignKey('users.id'), nullable=False)  # Employees are also users
)



# Define the models table
models = Table('models', metadata,
               Column('id', Integer, primary_key=True),
               Column('email', String(100), unique=True, nullable=False),
               Column('name', String(100), nullable=False),
               Column('registered_at', String, server_default=func.current_timestamp()),
               Column('csrf_cookies', Text, nullable=False),
               Column('auth_token', Text, nullable=False),
               Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
               Column('image_path', String(255)))

# Define the notifications table
notifications = Table('notifications', metadata,
                      Column('uuid', String, primary_key=True),
                      Column('created_at', DateTime, nullable=False),
                      Column('event_type', Integer, nullable=False),
                      Column('receiver_uuid', String, nullable=False),
                      Column('price', Integer, nullable=False),
                      Column('model_email', Text, nullable=False)
                      )

# Ensure the tables are created in the SQLite database
def dbinitialize():
    # Create the tables if they don't exist
    metadata.create_all(engine)
    session = Session()

    # Check if the owner user already exists
    owner_exists = session.query(users).filter_by(email='owner@example.com').first()

    if not owner_exists:
        # Insert the owner user with role 'Owner'
        owner = {'name': 'Owner', 'email': 'owner@example.com', 'role': 'Owner', 'password': 'password123'}
        session.execute(insert(users), [owner])
        session.commit()

    # Ensure the owner has the correct role if already present
    if owner_exists and owner_exists.role != 'Owner':
        session.execute(update(users).where(users.c.id == owner_exists.id).values(role='Owner'))
        session.commit()
    session.close()

def print_notifications():
    with Session() as session:
        # Update the select statement to use the correct syntax
        query = select(notifications)
        result = session.execute(query)

        for row in result:
            print(f"UUID: {row.uuid}, Created At: {row.created_at}, Event Type: {row.event_type}, "
                  f"Receiver UUID: {row.receiver_uuid}, Price: {row.price}, Model Email: {row.model_email}")


def fetch_event_data(model_email=None):
    """
    Fetch event data from the notifications table. Optionally filter by model email.
    """
    session = Session()
    try:
        # Correctly construct the select query by passing columns directly to select()
        query = select(notifications.c.created_at, notifications.c.event_type, notifications.c.price)

        if model_email:
            # Add a filter to select records for a specific model email
            query = query.where(notifications.c.model_email == model_email)

        result = session.execute(query).fetchall()

        # Process the result and return the data in a dictionary
        event_data = {}
        for row in result:
            created_at, event_type, price = row
            created_date = created_at.date()  # Convert timestamp to date
            if created_date not in event_data:
                event_data[created_date] = {'subs': [], 'purchases': [], 'tips': []}

            if event_type == 10:  # Assuming event_type 9 is for subscriptions
                event_data[created_date]['subs'].append(price)
            elif event_type == 9:  # Assuming event_type 10 is for purchases
                event_data[created_date]['purchases'].append(price)
            elif event_type == 11: # Assuming other event types are for tips
                event_data[created_date]['tips'].append(price)

        return event_data

    except Exception as e:
        logging.error(f"Error fetching event data: {e}")
        return {}
    finally:
        session.close()

def get_model_email_by_name(model_name):
    """
    Get the model email based on the model's name.
    """
    session = Session()
    try:
        # Query the database to get the model's email by its name
        query = select(models.c.email).where(models.c.name == model_name)
        result = session.execute(query).fetchone()
        
        if result:
            return result.email
        else:
            logging.warning(f"No model found with name: {model_name}")
            return None
    except Exception as e:
        logging.error(f"Error retrieving model email by name: {e}")
        return None
    finally:
        session.close()









def verify_login(email, password):
    conn = sqlite3.connect('my_database.db')  # Ensure this points to the correct database
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = ? AND password = ?"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    print_notifications()
    conn.close()
    return result is not None









def insert_user(name, email, role, password):
    with Session() as session:
        try:
            new_user = users.insert().values(name=name, email=email, role=role, password=password)
            session.execute(new_user)
            session.commit()

            user_id = session.execute(select(users.c.id).where(users.c.email == email)).scalar()
            logging.info(f"User {name} ({email}) added successfully with ID: {user_id}.")
            return user_id
        except Exception as e:
            session.rollback()
            logging.error(f"Error adding user {name} ({email}): {e}")
            return None


def get_user_by_id(user_id):
    with Session() as session:
        try:
            query = select(users).where(users.c.id == user_id)
            result = session.execute(query).fetchone()

            if result:
                user_data = {column.name: getattr(result, column.name) for column in users.columns}
                logging.info(f"User data retrieved for user_id: {user_id}, role: {user_data['role']}")
                return user_data
            else:
                logging.warning(f"No user found with user_id: {user_id}")
                return None
        except Exception as e:
            logging.error(f"Error fetching user data for user_id {user_id}: {e}")
            return None

        
def update_user(user_id, name=None, email=None, password=None, role=None):
    """Update user details like name, email, password, or role based on user_id."""
    with Session() as session:
        try:
            # Fetch the current user data to compare with new inputs
            current_user = session.execute(select(users).where(users.c.id == user_id)).fetchone()
            if not current_user:
                logging.error(f"No user found with id: {user_id}")
                return

            # Collect data only if it has changed
            update_data = {}
            if name and name != current_user.name:
                update_data['name'] = name
            if email and email != current_user.email:
                # Check if the email already exists for another user
                email_exists = session.execute(select(users).where(users.c.email == email, users.c.id != user_id)).scalar()
                if email_exists:
                    logging.error(f"Email {email} is already in use.")
                    return  # Abort the update if email is in use by another user
                update_data['email'] = email
            if password:  # Update password only if it's provided
                update_data['password'] = password  # Optional: Hash the password before storing
            if role and role != current_user.role:
                update_data['role'] = role

            # Only run the update if there are changes to make
            if update_data:
                update_statement = (
                    update(users)
                    .where(users.c.id == user_id)
                    .values(**update_data)
                )
                session.execute(update_statement)
                session.commit()
                logging.info(f"User {user_id} updated successfully with data: {update_data}")
            else:
                logging.info(f"No changes to update for user {user_id}.")
        except Exception as e:
            session.rollback()
            logging.error(f"Error updating user {user_id}: {e}")








def clear_employees_for_user(user_id):
    """Remove all employees assigned to the given user_id (manager)."""
    with Session() as session:
        try:
            # Delete all employee records for the given user_id from the user_employees table
            delete_statement = (
                user_employees.delete().where(user_employees.c.user_id == user_id)
            )
            session.execute(delete_statement)
            session.commit()
            logging.info(f"Cleared all employees for user_id: {user_id}")
        except Exception as e:
            session.rollback()
            logging.error(f"Error clearing employees for user_id {user_id}: {e}")



def clear_models_for_user(user_id):
    """Remove all models assigned to the given user_id."""
    with Session() as session:
        try:
            delete_statement = (
                user_models.delete().where(user_models.c.user_id == user_id)
            )
            session.execute(delete_statement)
            session.commit()
            logging.info(f"Cleared all models for user_id: {user_id}")
        except Exception as e:
            session.rollback()
            logging.error(f"Error clearing models for user_id {user_id}: {e}")






def print_user_employees():
    with Session() as session:
        result = session.execute(select(user_employees)).fetchall()
        for row in result:
            logging.info(f"user_id: {row.user_id}, employee_id: {row.employee_id}")



# Utility functions for models and notifications

def get_models_for_user(user_id):
    with Session() as session:
        try:
            query = select(models).select_from(user_models.join(models)).where(user_models.c.user_id == user_id)
            result = session.execute(query).fetchall()
            
            model_data = [{column.name: getattr(row, column.name) for column in models.columns} for row in result]
            logging.info(f"Model data retrieved successfully for user_id: {user_id}")
            return model_data
        except Exception as e:
            logging.error(f"An error occurred while retrieving model data for user_id {user_id}: {e}")
            return []


def get_user_by_email(email):
    """Fetch user details by their email."""
    with Session() as session:
        try:
            query = select(users).where(users.c.email == email)
            result = session.execute(query).fetchone()

            if result:
                user_data = {column.name: getattr(result, column.name) for column in users.columns}
                logging.info(f"User data retrieved for email: {email}, role: {user_data['role']}")
                return user_data
            else:
                logging.warning(f"No user found with email: {email}")
                return None
        except Exception as e:
            logging.error(f"Error fetching user data for email {email}: {e}")
            return None




        
def get_employees_for_user(manager_id):
    with Session() as session:
        try:
            query = (
                select(users)
                .select_from(user_employees.join(users, user_employees.c.employee_id == users.c.id))
                .where(user_employees.c.user_id == manager_id)
            )
            result = session.execute(query).fetchall()
            employee_data = [{column.name: getattr(row, column.name) for column in users.columns} for row in result]
            logging.info(f"Employee data retrieved successfully for user_id: {manager_id}")
            logging.info(f"Employees under manager: {employee_data}")
            return employee_data
        except Exception as e:
            logging.error(f"An error occurred while retrieving employee data for user_id {manager_id}: {e}")
            return []

def assign_employee_to_user(manager_id, employee_id):
    """Assign an employee to a manager."""
    with Session() as session:
        try:
            user_employee = user_employees.insert().values(user_id=manager_id, employee_id=employee_id)
            session.execute(user_employee)
            session.commit()
            logging.info(f"Employee {employee_id} assigned to user {manager_id} successfully.")
        except Exception as e:
            session.rollback()
            logging.error(f"Error assigning employee {employee_id} to user {manager_id}: {e}")






def assign_model_to_user(model_id, new_user_id):
    with Session() as session:
        try:
            # Check if the model is already assigned to this user
            existing_assignment = session.execute(
                select(user_models.c.user_id)
                .where(user_models.c.model_id == model_id, user_models.c.user_id == new_user_id)
            ).scalar()

            if existing_assignment:
                logging.info(f"Model {model_id} is already assigned to user {new_user_id}.")
                return

            # Insert new assignment for the model to the user
            insert_statement = user_models.insert().values(user_id=new_user_id, model_id=model_id)
            session.execute(insert_statement)
            session.commit()

            logging.info(f"Model {model_id} assigned successfully to user {new_user_id}.")
        except Exception as e:
            session.rollback()
            logging.error(f"Error assigning model {model_id} to user {new_user_id}: {e}")
        finally:
            session.close()

def remove_model_by_id_or_email(model_id=None, model_email=None):
    """
    Remove a model and its associated data (user_models, notifications) from the database.
    
    Args:
    - model_id: The ID of the model to be removed.
    - model_email: The email of the model to be removed.
    
    You can provide either model_id or model_email to identify the model.
    """
    if not model_id and not model_email:
        logging.error("Model ID or email must be provided to remove a model.")
        return False
    
    session = Session()
    try:
        # Step 1: Fetch the model using model_id or model_email
        model_query = select(models.c.id).where(
            models.c.id == model_id if model_id else models.c.email == model_email
        )
        model_result = session.execute(model_query).fetchone()
        
        if not model_result:
            logging.warning(f"Model not found. Unable to remove model_id: {model_id}, model_email: {model_email}")
            return False

        # Model ID to be used for further operations
        model_id_to_remove = model_result.id

        # Step 2: Remove associations from user_models
        session.execute(
            user_models.delete().where(user_models.c.model_id == model_id_to_remove)
        )

        # Step 3: Remove associated notifications
        session.execute(
            notifications.delete().where(notifications.c.model_email == model_email)
        )

        # Step 4: Remove the model from the models table
        session.execute(models.delete().where(models.c.id == model_id_to_remove))

        # Commit all changes
        session.commit()
        logging.info(f"Model {model_id_to_remove} and associated data removed successfully.")
        return True

    except Exception as e:
        session.rollback()
        logging.error(f"Error removing model {model_id} or {model_email}: {e}")
        return False
    finally:
        session.close()




def get_cookies_for_model(model_id):
    with Session() as session:
        try:
            query = select(models.c.csrf_cookies, models.c.auth_token).where(models.c.id == model_id)
            result = session.execute(query).fetchone()
            if result:
                cookies = {'csrf_cookies': result.csrf_cookies, 'auth_token': result.auth_token}
                logging.info(f"Cookies retrieved successfully for model_id: {model_id}")
                return cookies
            else:
                logging.warning(f"No cookies found for model_id: {model_id}")
                return None
        except Exception as e:
            logging.error(f"An error occurred while retrieving cookies for model_id {model_id}: {e}")
            return None

def insert_or_update_data(email, name, csrf_cookies, auth_token, image_path=None):
    email = email.lower()  # Ensure email is always lowercase

    with Session() as session:
        try:
            # Check if the model already exists
            query = select(models.c.id).where(models.c.email == email)
            result = session.execute(query).fetchone()

            if result:
                # If model exists, update it
                logging.info(f"Updating existing model with email: {email}")
                update_statement = (
                    update(models).
                    where(models.c.email == email).
                    values(name=name, csrf_cookies=csrf_cookies, auth_token=auth_token, image_path=image_path)
                )
                session.execute(update_statement)
                logging.info("Model data updated successfully!")
            else:
                # If the model is new, insert it
                if csrf_cookies and auth_token:
                    logging.info(f"Inserting new model with email: {email}")
                    insert_statement = models.insert().values(
                        email=email, name=name, csrf_cookies=csrf_cookies, auth_token=auth_token, user_id=1, image_path=image_path
                    )
                    session.execute(insert_statement)
                    session.commit()  # Commit to get model ID

                    # Fetch the inserted model's ID
                    model_id = session.execute(select(models.c.id).where(models.c.email == email)).scalar()

                    # Link the new model to user_id=1 (owner)
                    user_model_insert = user_models.insert().values(user_id=1, model_id=model_id)
                    session.execute(user_model_insert)
                    logging.info(f"Model {email} associated with owner user_id=1")
                else:
                    logging.error(f"Failed to insert model {email} due to missing cookies or auth token.")

            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f"An error occurred while inserting/updating the model {email}: {e}")
        finally:
            session.close()


def get_all_users():
    with Session() as session:
        try:
            # Fetch all users with their id, name, email, and role
            query = select(users.c.id, users.c.name, users.c.email, users.c.role)
            result = session.execute(query).fetchall()
            
            # Include 'id' in the returned data
            user_data = [{"id": row[0], "name": row[1], "email": row[2], "role": row[3]} for row in result]
            return user_data
        except Exception as e:
            logging.error(f"An error occurred while fetching users: {e}")
            return []
        
def get_all_models():
    with Session() as session:
        try:
            # Fetch all models with their id and name
            query = select(models.c.id, models.c.name)
            result = session.execute(query).fetchall()

            # Convert result to a list of dictionaries
            model_data = [{"id": row[0], "name": row[1]} for row in result]
            return model_data
        except Exception as e:
            logging.error(f"An error occurred while fetching models: {e}")
            return []






# Functions for notifications

from sqlalchemy.exc import IntegrityError

def insert_notification(uuid, created_at, event_type, receiver_uuid, price, model_email):
    with Session() as session:
        try:
            insert_statement = notifications.insert().values(
                uuid=uuid,
                created_at=created_at,
                event_type=event_type,
                receiver_uuid=receiver_uuid,
                price=price,
                model_email=model_email
            )
            session.execute(insert_statement)
            session.commit()
            logging.info(f"Notification {uuid} inserted successfully.")
        except IntegrityError:
            session.rollback()
            logging.warning(f"Notification with UUID {uuid} already exists. Skipping insertion.")
        except Exception as e:
            session.rollback()
            logging.error(f"An error occurred while inserting the notification: {e}")


def get_notifications_for_receiver(receiver_uuid):
    with Session() as session:
        try:
            query = select(notifications).where(notifications.c.receiver_uuid == receiver_uuid)
            result = session.execute(query).fetchall()
            notification_data = [{column.name: getattr(row, column.name) for column in notifications.columns} for row in result]
            logging.info(f"Notifications retrieved successfully for receiver_uuid: {receiver_uuid}")
            return notification_data
        except Exception as e:
            logging.error(f"An error occurred while retrieving notifications for receiver_uuid {receiver_uuid}: {e}")
            return []

def update_notification_as_read(uuid):
    with Session() as session:
        try:
            update_statement = (
                update(notifications).
                where(notifications.c.uuid == uuid).
                values(is_read=True)
            )
            session.execute(update_statement)
            session.commit()
            logging.info("Notification marked as read successfully!")
        except Exception as e:
            session.rollback()
            logging.error(f"An error occurred while updating the notification: {e}")
        finally:
            session.close()



# Worker class for threading (if necessary for your application)
class DBWorker(QObject):
    # Define signals for each function
    initialize_finished = Signal()
    models_for_user_retrieved = Signal(list)
    cookies_for_model_retrieved = Signal(dict)
    data_inserted_or_updated = Signal(bool)
    notifications_for_receiver_retrieved = Signal(list)
    notification_updated = Signal(bool)

    def __init__(self):
        super().__init__()

    @Slot()
    def initialize(self):
        try:
            dbinitialize()  # Call the actual initialize function in db_utils.py
            self.initialize_finished.emit()  # Emit signal when done
        except Exception as e:
            logging.error(f"Error in initialize: {e}")

    @Slot(int)
    def get_models_for_user(self, user_id):
        try:
            models = get_models_for_user(user_id)
            self.models_for_user_retrieved.emit(models)  # Emit signal with result
        except Exception as e:
            logging.error(f"Error in get_models_for_user: {e}")

    @Slot(int)
    def get_cookies_for_model(self, model_id):
        try:
            cookies = get_cookies_for_model(model_id)
            self.cookies_for_model_retrieved.emit(cookies)  # Emit signal with result
        except Exception as e:
            logging.error(f"Error in get_cookies_for_model: {e}")

    @Slot(str, str, str, str, int, str)
    def insert_or_update_data(self, email, name, csrf_cookies, auth_token, user_id, image_path=None):
        try:
            success = insert_or_update_data(email, name, csrf_cookies, auth_token, user_id, image_path)
            self.data_inserted_or_updated.emit(success)  # Emit signal with result
        except Exception as e:
            logging.error(f"Error in insert_or_update_data: {e}")

    @Slot(str)
    def get_notifications_for_receiver(self, receiver_uuid):
        try:
            notifications = get_notifications_for_receiver(receiver_uuid)
            self.notifications_for_receiver_retrieved.emit(notifications)  # Emit signal with result
        except Exception as e:
            logging.error(f"Error in get_notifications_for_receiver: {e}")

    @Slot(str)
    def update_notification_as_read(self, uuid):
        try:
            update_notification_as_read(uuid)
            self.notification_updated.emit(True)  # Emit signal when done
        except Exception as e:
            logging.error(f"Error in update_notification_as_read: {e}")
            self.notification_updated.emit(False)
