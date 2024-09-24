from sqlalchemy import create_engine, select, Table, MetaData, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import os
from datetime import datetime, timedelta
from sqlalchemy import select, func
from db_utils import notifications
import logging
from db_utils import dbinitialize
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'my_database.db')
db_url = f'sqlite:///{db_path}'  # SQLite URL with the path to the database
from db_utils import notifications
dbinitialize()
# Function to get the sum of prices for notifications from the last 'days' days and filter by event_type
def get_sum_of_prices_from_last_days(days, event_type=None):
    # Connect to the database
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()

  

    # Calculate the date range based on the number of days
    current_date = datetime.now()
    start_date = current_date - timedelta(days=days)

    # Build the query to sum the prices, filtered by date and optional event_type
    query = select(func.sum(notifications.c.price)).where(notifications.c.created_at >= start_date)
    
    if event_type is not None:
        query = query.where(notifications.c.event_type == event_type)

    # Execute the query and fetch the sum
    result = session.execute(query).scalar()

    # Close the session
    session.close()

    # Return the sum (None if no results found, so we convert to 0)
    return result or 0



from sqlalchemy import func

def get_notifications_for_models_and_time(model_email, days, event_type=None):
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Calculate the date range
    current_date = datetime.now()
    start_date = current_date - timedelta(days=days)

    # Group data by date
    query = select(
        func.date(notifications.c.created_at),  # Group by date
        func.sum(notifications.c.price)
    ).where(
        notifications.c.model_email == model_email,
        notifications.c.created_at >= start_date
    ).group_by(func.date(notifications.c.created_at))

    # If an event_type is provided, add it to the query
    if event_type is not None:
        query = query.where(notifications.c.event_type == event_type)

    # Execute the query and fetch the results
    result = session.execute(query).fetchall()

    # Close the session
    session.close()

    # Return a dictionary of date -> price
    return {row[0]: row[1] / 100 for row in result}  # Dividing prices by 100 to get actual values

# Example usage
# model = 'onlyplusmanagement@gmail.com'
# days = 300  # Example: Get notifications from the last 7 days
# subs = get_notifications_for_models_and_time(model, days, event_type=10)
# purchases = get_notifications_for_models_and_time(model, days, event_type=9)
# tips = get_notifications_for_models_and_time(model, days, event_type=11)
# total = get_notifications_for_models_and_time(model, days)
# # Output the sum of prices
# print(subs)
# print(purchases)
# print(tips)
# print(total)