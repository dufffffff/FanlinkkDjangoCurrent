from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserModelAssignment, Model, Notification, UserHierarchy, Organisation
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django import forms

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Form for creating users
    form = CustomUserChangeForm        # Form for changing users
    model = User
    list_display = ('email', 'username', 'role', 'organisation', 'is_staff', 'is_active')  # Added 'organisation'
    list_filter = ('is_staff', 'is_active', 'role', 'organisation')  # Added 'organisation' to filter
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'role', 'organisation')}),  # Added 'organisation'
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'last_activity')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'role', 'organisation', 'password1', 'password2', 'is_staff', 'is_active')}  # Added 'organisation'
        ),
    )

# Custom admin form for UserHierarchy to handle organisation automatically
class UserHierarchyAdminForm(forms.ModelForm):
    class Meta:
        model = UserHierarchy
        fields = '__all__'
    
    # Exclude the organisation field from the form if it exists
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'organisation' in self.fields:
            self.fields.pop('organisation')  # Remove the organisation field from the form if it exists

# Custom admin for UserHierarchy
class UserHierarchyAdmin(admin.ModelAdmin):
    form = UserHierarchyAdminForm  # Use the custom form

    # Exclude organisation from fields to display in the admin interface
    exclude = ['organisation']  # Exclude it entirely from the form

    def save_model(self, request, obj, form, change):
        # Automatically assign the organisation based on the supervisor's organisation
        obj.organisation = obj.supervisor.organisation
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Model)
admin.site.register(Notification)
admin.site.register(UserHierarchy, UserHierarchyAdmin)
admin.site.register(Organisation)
admin.site.register(UserModelAssignment)