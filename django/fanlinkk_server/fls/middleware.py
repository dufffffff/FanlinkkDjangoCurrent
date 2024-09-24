# middleware.py

from django.utils import timezone
from datetime import timedelta

class UpdateLastActivityMiddleware:
    """
    Middleware to update the last_activity field of authenticated users.
    Updates only if more than 1 minute has passed since the last update.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Update last_activity before processing the view
        if request.user.is_authenticated:
            now = timezone.now()
            last_activity = request.user.last_activity

            # Update only if more than 1 minute has passed
            if not last_activity or (now - last_activity > timedelta(minutes=1)):
                request.user.update_last_activity()

        response = self.get_response(request)
        return response
