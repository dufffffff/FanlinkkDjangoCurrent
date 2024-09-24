from django.db import migrations

def assign_default_organisation(apps, schema_editor):
    Organisation = apps.get_model('fls', 'Organisation')
    User = apps.get_model('fls', 'User')

    # Find or create the default user for the organisation
    default_user, created = User.objects.get_or_create(
        username="default_owner",
        defaults={"email": "default_owner@example.com", "password": "securepassword", "role": "owner"}
    )

    # Check if the default organisation already exists
    default_org, created = Organisation.objects.get_or_create(
        name="Default Organisation", 
        defaults={"owner": default_user}  # Assign the default user as owner
    )

    # No need to create a new organisation if it already exists
    if not created:
        print("Default Organisation already exists, skipping creation.")

class Migration(migrations.Migration):

    dependencies = [
        ('fls', '0010_auto_20240923_1044'),
    ]

    operations = [
        migrations.RunPython(assign_default_organisation),
    ]
