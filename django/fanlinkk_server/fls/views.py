# Example in views.py
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import render
from .utils import insert_user, fetch_event_data
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Model, User, Notification, Organisation, UserHierarchy, UserModelAssignment
import json
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout
from rest_framework import viewsets
from .serializers import NotificationSerializer


@csrf_exempt  # This disables CSRF for this view, you may apply it only here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Create JWT tokens
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'token': str(refresh.access_token),  # Send the access token
                'refresh': str(refresh)  # Optionally send refresh token
            })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)


def add_user_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        password = request.POST['password']
        user_id = insert_user(name, email, role, password)
        return render(request, 'success.html', {'user_id': user_id})
    return render(request, 'add_user.html')

@csrf_exempt
@api_view(['GET'])  # Using GET because your PyQt client is sending a GET request
@permission_classes([IsAuthenticated])
def heartbeat(request):
    """
    View to handle heartbeat requests from the PyQt client.
    Updates the user's last activity timestamp.
    """
    user = request.user
    user.last_activity = timezone.now()
    user.save(update_fields=['last_activity'])
    return Response({'status': 'success'})

@permission_classes([IsAuthenticated])
def get_notifications(request, model_email=None):
    if model_email:
        notifications = Notification.objects.filter(model_email=model_email)
    else:
        notifications = Notification.objects.all()
    
    data = list(notifications.values('uuid', 'created_at', 'event_type', 'price', 'receiver_uuid', 'model_email'))
    return JsonResponse({'notifications': data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure only authenticated users can access this
def get_all_users(request):
    try:
        # Query all users
        users = User.objects.all().values('id', 'first_name', 'email', 'role')

        # Return the users in JSON format
        return JsonResponse(list(users), safe=False, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def add_model(request):
    if request.method == 'POST':
        # Parse request data
        print(f"User: {request.user}")
        print(f"Auth Token: {request.META.get('HTTP_AUTHORIZATION')}")

        model_name = request.data.get('model_name')
        model_email = request.data.get('model_email')
        auth_token = request.data.get('auth_token')
        csrf_token = request.data.get('csrf_token')
        print(f"model name = {model_name}, model email = {model_email}")
        # Validate that the required fields are present
        if not model_name:
            return JsonResponse({'error': 'Model name is required.'}, status=400)
        if not model_email:
            return JsonResponse({'error': 'Model email is required.'}, status=400)
        if not auth_token:
            return JsonResponse({'error': 'Auth token is required.'}, status=400)
        if not csrf_token:
            return JsonResponse({'error': 'CSRF token is required.'}, status=400)

        # Check if the model is already registered by another user
        existing_model = Model.objects.filter(email=model_email).first()

        if existing_model:
            if existing_model.user != request.user:
                return JsonResponse({'error': 'Model is already registered by another user.'}, status=400)

            # If it's registered by the same user, skip or update the details if necessary
            return JsonResponse({'error': 'Model is already registered by you.'}, status=400)

        # If not already registered, create a new model entry
        model = Model.objects.create(
            name=model_name,
            email=model_email,
            auth_token=auth_token,
            csrf_cookies=csrf_token,  # Replace with actual CSRF value if needed
            user=request.user
        )

        return JsonResponse({'success': 'Model registered successfully.'})




    

def logout_view(request):
    if request.user.is_authenticated:
        request.user.last_activity = None
        request.user.save(update_fields=['last_activity'])
    logout(request)
    # Redirect to the login page or home page


    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users_in_organisation(request, organisation_id):
    try:
        # Fetch the organisation by ID
        organisation = Organisation.objects.get(id=organisation_id)
    
        # Fetch all users in the organisation
        users = organisation.users.all().values('id', 'first_name', 'email', 'role')
        
        # Return the list of users
        return JsonResponse(list(users), safe=False, status=200)
    except Organisation.DoesNotExist:
        return JsonResponse({'error': 'Organisation not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# Fetches users in the same organisation
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employees_for_user(request, user_email):
    try:
        # Fetch the user by email
        user = User.objects.get(email=user_email)
        
        # Get the organisation for the user
        organisation = user.organisation
        
        # Fetch employees (chatters) in the same organisation
        employees = User.objects.filter(organisation=organisation).exclude(id=user.id).values('id', 'first_name', 'email', 'role')
        
        return JsonResponse(list(employees), safe=False, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure only authenticated users can insert new users
def insert_chatter_manager(request):
    try:
        # Get the role, ensuring it's either 'manager' or 'chatter'
        role = request.data.get('role')

        if role not in ['manager', 'chatter']:
            return JsonResponse({'error': 'Role must be either "manager" or "chatter".'}, status=400)

        # Get the necessary user details
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        organisation_id = request.data.get('organisation_id')

        # Validate that all required fields are present
        if not all([email, first_name, last_name, password, organisation_id]):
            return JsonResponse({'error': 'All fields (email, first_name, last_name, password, organisation_id) are required.'}, status=400)

        # Check if the organisation exists
        organisation = Organisation.objects.get(id=organisation_id)

        # Create the user
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role,
            organisation=organisation
        )

        return JsonResponse({'message': f'User {user.email} created successfully.'}, status=201)

    except Organisation.DoesNotExist:
        return JsonResponse({'error': 'Organisation not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_models_for_organisation(request, organisation_id):
    try:
        # Fetch the models associated with the given organisation
        models = Model.objects.filter(organisation__pk=organisation_id).values('name', 'email')

        # Return the models in JSON format
        return JsonResponse(list(models), safe=False, status=200)
    except Organisation.DoesNotExist:
        return JsonResponse({'error': 'Organisation not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_organisation(request, user_email):
    """
    Returns the organisation of a given user.
    """
    try:
        user = User.objects.get(email=user_email)
        organisation = user.organisation
        organisation_data = {
            'id': organisation.id,
            'name': organisation.name
        }
        return JsonResponse(organisation_data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    """
    Creates a new user with the given name, email, role, and password.
    """
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        role = request.data.get('role')
        password = request.data.get('password')

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'User with this email already exists'}, status=400)

        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.name = name
        user.role = role
        user.save()

        return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_employee_to_user(request):
    """
    Assigns an employee to a user.
    """
    try:
        user_email = request.data.get('user_email')
        employee_email = request.data.get('employee_email')

        # Fetch the user and employee by their IDs
        user = User.objects.get(email=user_email)
        employee = User.objects.get(email=employee_email)

        # Assuming that "chatters" is the related field in User model for employees
        user.chatters.add(employee)

        return JsonResponse({'message': 'Employee assigned successfully'}, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User or employee not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_email(request, user_email):
    """
    Retrieve a user by their email.
    """
    try:
        user = User.objects.get(email=user_email)
        user_data = {
            'id': user.pk,
            'name': user.first_name,
            'email': user.email,
            'role': user.role,
        }
        return JsonResponse(user_data, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def validate_token_view(request):
    return JsonResponse({'status': 'valid'}, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_models_for_user(request, user_email):
    try:
        # Fetch the user by email
        user = User.objects.get(email=user_email)
        
        # Fetch models managed by this user
        models = UserModelAssignment.objects.filter(user=user).values( 'model__name', 'model__email')

        # Return the models in JSON format
        return JsonResponse(list(models), safe=False, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_subordinates(request, supervisor_email):
    try:
        # Fetch the supervisor by email
        supervisor = User.objects.get(email=supervisor_email)
        
        # Fetch all subordinates for this supervisor
        subordinates = UserHierarchy.objects.filter(supervisor=supervisor).values('user__id', 'user__first_name', 'user__email')
        
        # Return the subordinates in JSON format
        return JsonResponse(list(subordinates), safe=False, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Supervisor not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def clear_employees_for_user(request):
    user_email = request.data.get('user_email')
    try:
        user = User.objects.get(email=user_email)
        user.chatters.clear()  # Clear all employees for this user
        return JsonResponse({'success': 'Employees cleared successfully'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing notifications.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get models associated with the user
        user_models = user.models.all()
        # Get notifications for these models
        return Notification.objects.filter(model__in=user_models)