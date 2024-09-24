from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    # One owner per organisation
    owner = models.OneToOneField('User', on_delete=models.CASCADE, related_name='owned_organisation')

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('owner', 'Owner'),
        ('manager', 'Manager'),
        ('chatter', 'Chatter'),
    ]
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    # Each user must belong to an organisation
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.PROTECT,
        null=True,  # Add this to make it nullable temporarily
        blank=True,  # Optional: Allows forms to submit without this field being filled
        related_name='users'
    )
    # A manager can supervise chatters, and this creates a self-referential link to the manager
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='chatters')
    
    last_activity = models.DateTimeField(null=True, blank=True)

    def update_last_activity(self):
        self.last_activity = timezone.now()
        self.save(update_fields=['last_activity'])

    def is_active_user(self):
        if not self.last_activity:
            return False
        now = timezone.now()
        return now - self.last_activity <= timedelta(minutes=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Keep 'username' as it is part of the default Django model

    def __str__(self):
        return self.username


class Model(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)
    csrf_cookies = models.TextField()
    auth_token = models.TextField()
    managed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='managedby')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='organisation')
    def __str__(self):
        return self.name


class Notification(models.Model):
    uuid = models.CharField(max_length=255, primary_key=True)
    created_at = models.DateTimeField()
    event_type = models.IntegerField()
    receiver_uuid = models.CharField(max_length=255)
    price = models.IntegerField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='notifications')

    # Optional field for specifying the type of purchase
    purchase_type = models.CharField(max_length=20, null=True, blank=True)  # 'post', 'message', etc.

    def __str__(self):
        return f"Notification {self.uuid} - {self.purchase_type}"


# Optional AccessLevel model (if needed for custom permissions)
class AccessLevel(models.Model):
    role = models.CharField(max_length=20, choices=User.ROLE_CHOICES)
    permission = models.JSONField()

    def __str__(self):
        return f"AccessLevel for role {self.role}"


# Optional: User hierarchy model for tracking subordinates and supervisors
class UserHierarchy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subordinates')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervisors')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='hierarchies')
    class Meta:
        unique_together = ('user', 'supervisor')

    def save(self, *args, **kwargs):
        # Automatically set organisation based on supervisor's organisation
        if self.supervisor.organisation:
            self.organisation = self.supervisor.organisation
        else:
            raise ValueError("Supervisor must belong to an organisation")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} supervised by {self.supervisor.username} in Organisation {self.organisation.id}"
    
class UserModelAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_models')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='assigned_users')
    assigned_at = models.DateTimeField(auto_now_add=True)  # Optional: to track when the assignment was made
    
    class Meta:
        unique_together = ('user', 'model')  # To ensure a user can't be assigned the same model more than once

    def __str__(self):
        return f"{self.user.email} manages {self.model.name}"