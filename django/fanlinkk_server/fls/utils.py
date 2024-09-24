from .models import User, Model, Notification
def insert_user(name, email, role, password):
    try:
        user = User.objects.create(name=name, email=email, role=role, password=password)
        return user.id
    except Exception as e:
        print(f"Error adding user: {e}")
        return None
    

def fetch_event_data(model_email=None):
    query = Notification.objects.all()

    if model_email:
        query = query.filter(model_email=model_email)

    event_data = {}
    for notification in query:
        created_date = notification.created_at.date()
        if created_date not in event_data:
            event_data[created_date] = {'subs': [], 'purchases': [], 'tips': []}

        if notification.event_type == 10:
            event_data[created_date]['subs'].append(notification.price)
        elif notification.event_type == 9:
            event_data[created_date]['purchases'].append(notification.price)
        elif notification.event_type == 11:
            event_data[created_date]['tips'].append(notification.price)

    return event_data



def get_cookies_for_model(model_id):
    try:
        model = Model.objects.get(id=model_id)
        return {
            'csrf_cookies': model.csrf_cookies,
            'auth_token': model.auth_token,
        }
    except Model.DoesNotExist:
        return None