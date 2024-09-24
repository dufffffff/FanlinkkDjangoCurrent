# your_app/urls.py (App folder)
from django.urls import path, include
from . import views
from .views import login_view, heartbeat, NotificationViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notifications', NotificationViewSet, basename='notification')


urlpatterns = [
    path('api/', include(router.urls)),

    #basic function paths
    path('api/login/', views.login_view, name='login_view'),
    path('api/heartbeat/', views.heartbeat, name='heartbeat'),
    path('api/validate_token/', views.validate_token_view, name='validate_token_view'),
    
    #employee related paths
    path('api/assign_employee/', views.assign_employee_to_user, name = 'assign_employee_to_user'),
    path('api/clear_employees/', views.clear_employees_for_user, name = 'clear_employees_for_user'),
    path('api/employees/<str:user_email>/', views.get_employees_for_user, name='get_employees_for_user'),
    path('api/add_employee', views.insert_chatter_manager, name='insert_chatter_manager'),
 
    #agency related paths
    path('api/organisation/getid/<str:user_email>/', views.get_user_organisation, name='get_user_organisation'),
    path('api/organisation/getusers/<int:organisation_id>/', views.get_users_in_organisation, name='get_users_in_organisation'),

    #model related paths
    path('api/add_model/', views.add_model, name='add_model'),
    path('api/models/user/<str:user_email>/', views.get_models_for_user, name='get_models_for_user'), 
    path('api/models/org/<int:organisation_id>/', views.get_models_for_organisation, name='get_models_for_organisation'),

    #user related paths
    path('add_user/', views.add_user_view, name='add_user'),
    path('api/users/', views.get_all_users, name='get_all_users'),
    path('api/add_user/', views.create_user, name='create_user'),
    path('api/users/email/<str:user_email>/', views.get_user_by_email, name='get_user_by_email'),
    path('api/users/subordinates/<str:supervisor_email>/', views.get_subordinates, name='get_subordinates'),
    #notification related paths
    path('notifications/', views.get_notifications, name='get_notifications'),
    path('notifications/<str:model_email>/', views.get_notifications, name='get_notifications_by_model'),
    
   
    
   

]

    


